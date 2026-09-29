"""Verify the September 29 homework from its actual submitted source.

Run: python3 scripts/test_remaining_python_homework.py
The Libraries route exercise requires Flask==3.1.3. No other third-party
package is required by this verifier. No network or live backend is used.
"""

import ast
from contextlib import redirect_stdout
import copy
import io
import itertools
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "reports/python-homework-2026-09-29.json"


def execute(source, definitions_only=False):
    tree = ast.parse(source)
    if definitions_only:
        tree.body = [node for node in tree.body
                     if isinstance(node, (ast.FunctionDef, ast.Import, ast.ImportFrom))]
    namespace = {"__name__": "__main__"}
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        exec(compile(tree, "submitted-homework", "exec"), namespace)
    return namespace, stdout.getvalue()


def call(function, *args):
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        result = function(*args)
    return result, stdout.getvalue()


def check_boolean(namespace):
    validate = namespace["validate_record"]
    base = {"product_name": "Clutch", "category": "Auto Racing",
            "spec_number": "9.1", "effective_date": "Sep. 29, 2026"}
    categories = ["Auto Racing", "Drag Racing"]
    for category, expected in [("Auto Racing", True), ("Drag Racing", True),
                               ("Street Car", False), ("", False)]:
        actual = validate(dict(base, category=category), ["1.1"], categories)
        assert type(actual) is bool and actual is expected
    for field in ["product_name", "spec_number", "effective_date"]:
        for value in ["", "  "]:
            assert validate(dict(base, **{field: value}), [], categories) is False
        missing = base.copy()
        del missing[field]
        assert validate(missing, [], categories) is False
    for duplicate in ["1.1", " 1.1 "]:
        assert validate(dict(base, spec_number=duplicate), ["1.1"], categories) is False
    assert validate(base, [], categories) is True


MESSAGES = ["Nothing suspicious in this message.\n",
            "Be a little careful, but this is probably fine.\n",
            "This looks risky. Check with someone you trust before replying.\n",
            "Do not reply. This is almost certainly a scam.\n"]


def check_conditionals(namespace):
    score = namespace["score_message"]
    for gift, large, unknown in itertools.product([False, True], repeat=3):
        actual = score("GIFT CARDS" if gift else "Hello", 101 if large else 100, not unknown)
        assert actual == 4 * gift + 3 * large + 2 * unknown
    for value, band in [(0, 0), (2, 0), (3, 1), (5, 1), (6, 2), (8, 2), (9, 3), (12, 3)]:
        _, output = call(namespace["report_risk"], value)
        assert output == MESSAGES[band], (value, output)


SCHEDULE = {
    (False, False): "Finish homework before dinner and free time.",
    (False, True): "Finish homework before practice; leave time for dinner.",
    (True, False): "Homework finished: enjoy free time before dinner.",
    (True, True): "Homework finished: attend practice, then dinner.",
}
MEALS = {
    (False, False): "Buy lunch; plan dinner after homework.",
    (False, True): "Buy lunch and an extra practice snack.",
    (True, False): "Bring packed lunch; plan dinner after homework.",
    (True, True): "Bring packed lunch and an extra practice snack.",
}


def check_nested(namespace):
    for values in itertools.product([False, True], repeat=4):
        logged, done, packed, practice = values
        student = dict(zip(["logged_in", "homework_finished", "lunch_packed", "practice_today"], values))
        before = student.copy()
        expected = (["Account ready: review today's schedule.", SCHEDULE[done, practice], MEALS[packed, practice]]
                    if logged else ["Log in first to view the student schedule."])
        assert namespace["daily_routine"](student) == expected, values
        assert student == before


def check_algorithms(namespace):
    cases = [
        (["Toothbrushes", "Blankets", "Socks", "Shampoo", "Notebooks"],
         [40, 8, 25, 5, 30], [30, 20, 25, 15, 30],
         (["Blankets", "Shampoo"], [12, 10], 22, 0),
         "Restock needed:\nBlankets: need 12\nShampoo: need 10\nTotal items needed: 22\nMost urgent: Blankets (short by 12)\n"),
        (["A"], [10], [10], ([], [], 0, None), "Fully stocked!\n"),
        ([], [], [], ([], [], 0, None), "Fully stocked!\n"),
        (["A", "B"], [9, 0], [10, 10], (["A", "B"], [1, 10], 11, 1), None),
        (["A", "B"], [5, 5], [10, 10], (["A", "B"], [5, 5], 10, 0), None),
        (["A"], [12], [10], ([], [], 0, None), "Fully stocked!\n"),
    ]
    for names, stock, target, expected, printed in cases:
        before = copy.deepcopy((names, stock, target))
        result, output = call(namespace["restock_report"], names, stock, target)
        assert result == expected
        assert (names, stock, target) == before
        if printed is not None:
            assert output == printed
    try:
        namespace["restock_report"](["A"], [], [1])
    except ValueError:
        pass
    else:
        raise AssertionError("Parallel list mismatch was accepted")


def check_procedures(namespace):
    recipe = {"flour": 2, "milk": 1}
    for servings, expected in [(2, {"flour": 1.0, "milk": 0.5}),
                               (4, {"flour": 2.0, "milk": 1.0}),
                               (8, {"flour": 4.0, "milk": 2.0})]:
        assert namespace["scale_ingredients"](recipe, 4, servings) == expected
    assert recipe == {"flour": 2, "milk": 1}
    assert namespace["prepare_scaled_recipe"](recipe, 4, 8) == [
        "Dessert servings: 8", "flour: 4.0 cups", "milk: 2.0 cups"]
    for value in [0, -1, 2.5, True]:
        try:
            namespace["validate_servings"](value)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid servings accepted")


def check_libraries(namespace):
    games = [{"date": "2026-09-10", "opponent": "A", "points": 6},
             {"date": "2026-09-18", "opponent": "A", "points": 8},
             {"date": "2026-09-26", "opponent": "B", "points": 4}]
    before = copy.deepcopy(games)
    actual = namespace["summarize_season"](games)
    assert actual == {"total_points": 18, "average_points": 6.0, "best_game": 8,
                      "points_by_opponent": {"A": 14, "B": 4}}
    assert games == before
    assert namespace["summarize_season"]([]) == {"total_points": 0, "average_points": None,
                                                 "best_game": None, "points_by_opponent": {}}
    assert namespace["summarize_season"](games[:1])["best_game"] == 6


def check_random(namespace):
    part = {"product_name": "Practice part", "category": "Auto Racing", "spec_number": "9.1"}
    for exists, action, expected_status, present_after in [
        (False, "GET/search", 404, False), (True, "GET/search", 200, True),
        (False, "POST/create", 201, True), (True, "POST/create", 409, True),
        (False, "PUT/update", 404, False), (True, "PUT/update", 200, True),
        (False, "DELETE/remove", 404, False), (True, "DELETE/remove", 204, False),
        (False, "UNKNOWN", 400, False),
    ]:
        state = {"9.1", "untouched"} if exists else {"untouched"}
        status, message = namespace["apply_action"](part, action, state)
        assert status == expected_status and message
        assert ("9.1" in state) is present_after and "untouched" in state
    parts = [part, dict(part, spec_number="2.1", product_name="Another part")]
    actions = ["GET/search", "POST/create", "PUT/update", "DELETE/remove"]
    before = copy.deepcopy(parts)
    for seed in range(10):
        transcript, final = namespace["simulate_qa"](parts, actions, ["2.1"], 20, seed)
        assert len(transcript) == 20
        assert (transcript, final) == namespace["simulate_qa"](parts, actions, ["2.1"], 20, seed)
        for row in transcript:
            fields = {key: row[key] for key in part}
            assert fields in parts and row["action"] in actions
        assert set(final) <= {"9.1", "2.1"}
    assert parts == before
    assert namespace["simulate_qa"]([], [], ["2.1"], 0, 1) == ([], ["2.1"])


def check_efficiency(namespace):
    for n, pairs in [(0, 0), (1, 1), (7, 49), (12, 144), (24, 576)]:
        assert namespace["catalog_work"](n) == {"books": n, "visits": n, "ordered_pairs": pairs}
    for invalid in [-1, 1.5, True]:
        try:
            namespace["catalog_work"](invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid catalog size accepted")


CHECKS = {"305": check_boolean, "306": check_conditionals, "307": check_nested,
          "309": check_algorithms, "313": check_procedures, "314": check_libraries,
          "315": check_random, "317": check_efficiency}


def main():
    manifest = json.loads(MANIFEST.read_text())
    assert len(manifest) == 8
    sources, cells_by_topic = {}, {}
    saved_count = 0
    for item in manifest:
        key = item["key"]
        if item["format"] == "notebook":
            notebook = json.loads((ROOT / item["file"]).read_text())
            cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
            assert notebook["cells"][0]["cell_type"] == "raw"
            assert "local_python: true" in "".join(notebook["cells"][0]["source"])
            # The existing converter assigns fenced blocks to runners in order.
            # Static translations must not consume a later Python runner slot.
            last_code = max(i for i, cell in enumerate(notebook["cells"])
                            if cell["cell_type"] == "code")
            for cell in notebook["cells"][:last_code]:
                if cell["cell_type"] == "markdown":
                    assert "```" not in "".join(cell["source"]), cell["id"]
            cells_by_topic[key] = {c["id"]: c for c in cells}
            for cell in cells:
                source = "".join(cell["source"])
                assert source.startswith("# CODE_RUNNER:")
                assert "TODO" not in source and "____" not in source
                _, actual = execute(source)
                saved = "".join("".join(o["text"]) for o in cell["outputs"])
                assert actual == saved, "Stale output: " + cell["id"]
                saved_count += 1
        source = (ROOT / item["export"]).read_text()
        sources[key] = source
        namespace, expected_output = execute(source)
        # A real file launch catches module-name collisions such as random.py.
        script = ROOT / item["export"]
        process = subprocess.run([sys.executable, str(script)], cwd=script.parent,
                                 capture_output=True, text=True, timeout=30, check=True)
        assert process.stdout == expected_output and not process.stderr, item["export"]
        CHECKS[key](namespace)
        print("PASS", item["title"], "saved outputs and independent behavior")

    # Additional task-specific exercises are checked outside the homework export.
    search_source = "".join(cells_by_topic["305"]["305-popcorn-3"]["source"])
    search, _ = execute(search_source)
    records = search["records"]
    assert [r["spec_number"] for r in search["search_records"](records, "FLYWHEEL", search["valid_categories"])] == ["1.1", "2.1"]
    assert search["search_records"](records, "1", search["valid_categories"]) == []
    flask_source = "".join(cells_by_topic["314"]["314-popcorn-2"]["source"])
    flask, _ = execute(flask_source)
    client = flask["app"].test_client()
    assert client.get("/score").get_json() == {"home": 6, "away": 4, "period": 2}
    assert client.get("/roster").get_json() == {"players": ["Adhvay", "Ishan", "Rohan"]}
    assert client.get("/record").get_json() == {"team": "UESL Practice Team", "wins": 3, "losses": 1}
    assert client.get("/missing").status_code == 404
    calculator, _ = execute((ROOT / "assets/homework/2026-09-29/algorithmic-efficiency-popcorn.py").read_text())
    for n, expected in [(0, (0, 0)), (1, (1, 1)), (8, (8, 4)), (16, (16, 5)), (1000, (1000, 10))]:
        assert calculator["search_counts"](n) == expected
    for key in ["306", "309"]:
        tree = ast.parse(sources[key])
        calls = {node.func.id for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)}
        assert not ({"sum", "max"} & calls) if key == "309" else "input" not in calls
        if key == "306":
            assert not any(isinstance(node, (ast.Import, ast.ImportFrom, ast.IfExp, ast.Match)) for node in ast.walk(tree))

    mutations = [
        ("305", "and not duplicate_spec", "or not duplicate_spec"),
        ("306", "amount_requested > 100", "amount_requested >= 100"),
        ("307", 'if student["logged_in"]:', 'if not student["logged_in"]:'),
        ("309", "in_stock[i] < target[i]", "in_stock[i] <= target[i]"),
        ("313", "requested_servings / base_servings", "base_servings / requested_servings"),
        ("314", 'by_opponent.get(opponent, 0) + game["points"]', 'game["points"]'),
        ("315", 'return 409, "Duplicate spec rejected"', 'return 201, "Duplicate spec rejected"'),
        ("317", '"ordered_pairs": n * n', '"ordered_pairs": n + n'),
    ]
    for key, before, after in mutations:
        assert sources[key].count(before) == 1
        namespace, _ = execute(sources[key].replace(before, after), definitions_only=True)
        try:
            CHECKS[key](namespace)
        except AssertionError:
            print("PASS detected intentional regression:", key)
        else:
            raise AssertionError("Missed regression: " + key)
    print(f"PASS: {saved_count} saved notebook outputs, 8 homework exports, "
          "8 regression checks, Flask responses, and search-count models")


if __name__ == "__main__":
    main()
