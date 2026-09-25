"""Verify the submitted notebook cells, without copying their algorithms.

Run from any directory: python3 scripts/test_iterations_homework.py
Only the Python standard library is required.
"""

import ast
from contextlib import redirect_stdout
import io
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "_notebooks/homework/2026-09-25-iterations-hw.ipynb"
MAIN_DATA = [18, 39, 40, 66, 27, 89, 90, 45, 12, 99]
# Expected values were worked out independently: checked, skipped, actions,
# total action latency, critical found, uninspected.
CASES = [
    ("main", MAIN_DATA, 40, 90, (7, 3, 4, 285, True, 3)),
    ("empty", [], 40, 90, (0, 0, 0, 0, False, 0)),
    ("all safe", [0, 10, 39], 40, 90, (3, 3, 0, 0, False, 0)),
    ("no critical", [40, 55, 89], 40, 90, (3, 0, 3, 184, False, 0)),
    ("critical first", [90, 40, 99], 40, 90, (1, 0, 1, 90, True, 2)),
    ("boundaries", [39, 40, 89, 90, 41], 40, 90, (4, 1, 3, 219, True, 1)),
    ("critical last", [20, 40, 60, 90], 40, 90, (4, 1, 3, 190, True, 0)),
    ("two critical", [45, 95, 90], 40, 90, (2, 0, 2, 140, True, 1)),
    ("zero", [0, 40, 90], 40, 90, (3, 1, 2, 130, True, 0)),
    ("repeated", [40, 40, 39, 90], 40, 90, (4, 1, 3, 170, True, 0)),
    ("new thresholds", [10, 20, 30, 40, 50], 20, 40, (4, 1, 3, 90, True, 1)),
]


def execute(source, replacements=None):
    """Replace only named top-level initializers; execute the actual loop body."""
    tree = ast.parse(source)
    replacements = replacements or {}
    replaced = set()
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in replacements:
                node.value = ast.parse(repr(replacements[target.id]), mode="eval").body
                replaced.add(target.id)
    assert replaced == set(replacements), f"Missing initializer: {set(replacements) - replaced}"
    namespace = {}
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        exec(compile(ast.fix_missing_locations(tree), str(NOTEBOOK), "exec"), namespace)
    return namespace, stdout.getvalue()


def verify_case(source, case):
    name, data, safe, critical, expected = case
    state, output = execute(source, {
        "match_latencies_ms": data,
        "safe_cutoff": safe,
        "critical_cutoff": critical,
    })
    keys = ("checked_count", "skipped_count", "action_count",
            "total_action_latency_ms", "critical_found")
    actual = tuple(state[key] for key in keys) + (len(data) - state["checked_count"],)
    assert actual == expected, (name, expected, actual)
    assert state["match_latencies_ms"] == data, f"Input changed: {name}"
    checked, skipped, actions, total, found, uninspected = expected
    assert checked == skipped + actions
    assert checked + uninspected == len(data)
    report = (
        "UESL Match Latency - Final Report\n"
        f"Checked readings: {checked}\n"
        f"Skipped safe readings: {skipped}\n"
        f"Action readings: {actions}\n"
        f"Total action latency (ms): {total}\n"
        f"Critical found: {found}\n"
        f"Uninspected readings: {uninspected}\n"
    )
    assert output.endswith(report), f"Incorrect report: {name}\n{output}"
    inspected = [int(line.split()[0]) for line in output.splitlines() if " ms: " in line]
    assert inspected == data[:checked], f"Wrong inspected prefix: {name}"
    assert output.count("Critical match latency found.") == int(found)


def main():
    notebook = json.loads(NOTEBOOK.read_text())
    cells = {c["id"]: c for c in notebook["cells"] if c["cell_type"] == "code"}
    assert len(cells) == 4
    sources = {key: "".join(cell["source"]) for key, cell in cells.items()}
    for key, source in sources.items():
        assert source.startswith("# CODE_RUNNER:")
        assert "____" not in source and "TODO" not in source
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom))
                       for node in ast.walk(ast.parse(source)))
        _, actual_output = execute(source)
        assert all(o["output_type"] == "stream" for o in cells[key]["outputs"])
        saved_output = "".join("".join(o["text"]) for o in cells[key]["outputs"])
        assert actual_output == saved_output, f"Stale saved output: {key}"
    popcorn, _ = execute(sources["iterations-popcorn"])
    assert tuple(popcorn[k] for k in ("checked_count", "safe_count", "action_count",
                                     "total_action_score", "critical_found")) == (6, 2, 4, 25, True)

    homework = sources["iterations-homework"]
    for case in CASES:
        verify_case(homework, case)
        print(f"PASS homework: {case[0]}")

    while_source = sources["iterations-while"]
    for data, ticks, queue in [({}, 3, 10), ({"queued_frames": 8}, 0, 8),
                               ({"queued_frames": 32}, 4, 4)]:
        state, _ = execute(while_source, data)
        assert (state["ticks"], state["queued_frames"]) == (ticks, queue)
    for data, message in [({"frames_per_tick": 0}, "positive"),
                          ({"target_queue": -1}, "nonnegative"),
                          ({"queued_frames": -1}, "nonnegative")]:
        try:
            execute(while_source, data)
        except ValueError as error:
            assert message in str(error)
        else:
            raise AssertionError(f"Invalid queue settings must be rejected: {data}")

    fixed = sources["iterations-fixed"]
    for count in (0, 1, 3, 5):
        state, output = execute(fixed, {"checks_needed": count})
        assert state["completed_checks"] == count
        lines = [f"UESL readiness check: {i}" for i in range(1, count + 1)]
        assert output == "\n".join(lines + [f"Completed checks: {count}"]) + "\n"

    mutations = [
        ("safe boundary", "latency_ms < safe_cutoff", "latency_ms <= safe_cutoff"),
        ("critical boundary", "latency_ms >= critical_cutoff", "latency_ms > critical_cutoff"),
        ("missing checked update", "checked_count += 1", "checked_count += 0"),
        ("no early exit", "        break", "        continue"),
    ]
    for name, before, after in mutations:
        assert homework.count(before) == 1
        mutant = homework.replace(before, after)
        try:
            for case in CASES:
                verify_case(mutant, case)
        except AssertionError:
            print(f"PASS regression detected: {name}")
        else:
            raise AssertionError(f"Tests failed to detect {name}")
    print("PASS: 4 saved outputs, 11 homework datasets, Popcorn totals, 10 extension cases, 4 mutation checks")


if __name__ == "__main__":
    main()
