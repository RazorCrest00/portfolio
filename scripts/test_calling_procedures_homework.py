"""Check the actual 3.12 notebook functions and saved outputs.

Run from any directory: python3 scripts/test_calling_procedures_homework.py
Only the Python standard library is required.
"""

import ast
from contextlib import redirect_stdout
import inspect
import io
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "_notebooks/homework/2026-09-28-calling-procedures-hw.ipynb"
CASES = [
    ("Medical Emergency", True),
    ("Power Outage", False),
    ("Road Blockage", False),
    ("Training Drill", False),
    ("medical emergency", False),
    ("MEDICAL EMERGENCY", False),
    ("Medical Emergency ", False),
    ("", False),
]


def execute(source, definitions_only=False):
    tree = ast.parse(source)
    if definitions_only:
        tree.body = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    namespace, stdout = {}, io.StringIO()
    with redirect_stdout(stdout):
        exec(compile(tree, str(NOTEBOOK), "exec"), namespace)
    return namespace, stdout.getvalue()


def capture(function, *args, **kwargs):
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        result = function(*args, **kwargs)
    return result, stdout.getvalue()


def check_helper(helper):
    assert list(inspect.signature(helper).parameters) == ["incident_type"]
    for incident, expected in CASES:
        result, output = capture(helper, incident)
        assert type(result) is bool, f"Expected a Boolean, got {result!r}"
        assert result is expected, (incident, result, expected)
        assert output == "", "A helper must return its result without printing it"


def check_outer(namespace, outer_name, helper_name, prefixes):
    """Trace the real helper, without substituting a test implementation."""
    outer, helper = namespace[outer_name], namespace[helper_name]
    assert list(inspect.signature(outer).parameters) == ["location", "incident_type"]
    for index, (incident, expected) in enumerate(CASES + CASES[:2]):
        location = "Zone É " + str(index)
        events = []

        def profile(frame, event, argument):
            if frame.f_code is helper.__code__ and event in ("call", "return"):
                value = frame.f_locals["incident_type"] if event == "call" else argument
                events.append((event, value))

        previous_profile = sys.getprofile()
        try:
            sys.setprofile(profile)
            # Reordered keywords exercise binding independently of source order.
            if index % 2:
                result, output = capture(outer, incident_type=incident, location=location)
            else:
                result, output = capture(outer, location, incident)
        finally:
            sys.setprofile(previous_profile)
        assert events == [("call", incident), ("return", expected)], events
        assert result is None, "The outer procedure displays a message"
        prefix = prefixes[0] if expected else prefixes[1]
        assert output == f"{prefix}: {incident} reported in {location}\n", output


def verify_homework(source):
    namespace, output = execute(source, definitions_only=True)
    assert output == "", "Definitions alone must not run the procedures"
    check_helper(namespace["check_priority"])
    check_outer(namespace, "dispatch_response", "check_priority",
                ("PRIORITY RESPONSE", "STANDARD RESPONSE"))


def main():
    notebook = json.loads(NOTEBOOK.read_text())
    cells = {c["id"]: c for c in notebook["cells"] if c["cell_type"] == "code"}
    assert len(cells) == 3
    sources = {key: "".join(cell["source"]) for key, cell in cells.items()}
    required_calls = {
        "procedures-popcorn-1": ("report_status", 2),
        "procedures-popcorn-2": ("process_report", 2),
        "procedures-homework": ("dispatch_response", 4),
    }
    for key, source in sources.items():
        assert source.startswith("# CODE_RUNNER:")
        assert "TODO" not in source and "____" not in source
        tree = ast.parse(source)
        assert not any(isinstance(n, (ast.Import, ast.ImportFrom, ast.Global, ast.Pass))
                       for n in ast.walk(tree))
        name, count = required_calls[key]
        calls = [n.value for n in tree.body if isinstance(n, ast.Expr)
                 and isinstance(n.value, ast.Call)]
        assert len(calls) == count
        assert all(isinstance(c.func, ast.Name) and c.func.id == name for c in calls)
        if key == "procedures-homework":
            arguments = [[ast.literal_eval(a) for a in call.args] for call in calls]
            assert len({a[0] for a in arguments}) == 4
            assert len({a[1] for a in arguments}) == 3
        _, actual = execute(source)
        outputs = cells[key]["outputs"]
        assert outputs and all(o["output_type"] == "stream" and o["name"] == "stdout"
                               for o in outputs)
        saved = "".join("".join(o["text"]) for o in outputs)
        assert actual == saved, f"Stale saved output: {key}"
        _, defined_output = execute(source, definitions_only=True)
        assert defined_output == ""

    status, _ = execute(sources["procedures-popcorn-1"], definitions_only=True)
    report = status["report_status"]
    assert list(inspect.signature(report).parameters) == ["location", "status"]
    for location, message in [("New Zone", "Ready"), ("", ""),
                              ("Zone É", "Equipment ✓"), ("Zone B", "")]:
        result, output = capture(report, status=message, location=location)
        assert result is None
        assert output == f"Status update from {location}: {message}\n"

    popcorn, _ = execute(sources["procedures-popcorn-2"], definitions_only=True)
    check_helper(popcorn["is_priority"])
    check_outer(popcorn, "process_report", "is_priority",
                ("PRIORITY", "STANDARD REPORT"))
    homework = sources["procedures-homework"]
    verify_homework(homework)

    mutations = [
        ("string Boolean", 'return incident_type == "Medical Emergency"', 'return "True"'),
        ("bypassed helper", "priority = check_priority(incident_type)", "priority = True"),
        ("wrong helper argument", "check_priority(incident_type)", "check_priority(location)"),
        ("reversed branch", "if priority:", "if not priority:"),
    ]
    for name, before, after in mutations:
        assert homework.count(before) == 1
        try:
            verify_homework(homework.replace(before, after))
        except AssertionError:
            print(f"PASS regression detected: {name}")
        else:
            raise AssertionError(f"Tests failed to detect {name}")
    print("PASS: 3 saved outputs, 16 helper cases, 20 traced outer calls, "
          "4 status cases, 4 mutation checks")


if __name__ == "__main__":
    main()
