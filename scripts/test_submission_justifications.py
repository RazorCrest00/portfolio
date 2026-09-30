"""Verify each September submission's written reviewer challenge against its source.

Run from the portfolio: python3 scripts/test_submission_justifications.py
Only the standard library is required. No copied solution or network is used.
"""
import ast
from contextlib import redirect_stdout
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def execute(source, replacements=None):
    tree = ast.parse(source)
    remaining = dict(replacements or {})
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in remaining:
                node.value = ast.parse(repr(remaining.pop(target.id)), mode="eval").body
    assert not remaining, f"Missing input assignments: {remaining}"
    namespace = {"__name__": "__main__"}
    output = io.StringIO()
    with redirect_stdout(output):
        exec(compile(ast.fix_missing_locations(tree), "actual-submission", "exec"), namespace)
    return namespace, output.getvalue()


def homework(token, replacements=None):
    paths = list((ROOT / "_notebooks/homework").glob(f"*{token}*.ipynb"))
    assert len(paths) == 1, paths
    notebook = json.loads(paths[0].read_text())
    candidates = ["".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code"
                  and ("homework" in "".join(c["source"]).splitlines()[0].lower()
                       or c.get("id") == "313-homework")]
    assert len(candidates) == 1, token
    evidence = [c for c in notebook["cells"] if c.get("id", "").startswith("credit-evidence-")]
    assert len(evidence) == 1
    return execute(candidates[0], replacements)


def printed(function, *args, **kwargs):
    output = io.StringIO()
    with redirect_stdout(output):
        result = function(*args, **kwargs)
    return result, output.getvalue()


def main():
    _, out = homework("math-expressions", {"sessions_per_week": 2, "enrollment_fee": 0})
    assert out == "Weekly Cost: $70.00\nMonthly Cost: $280.00\nTotal Cost with Fee: $280.00\nAverage Daily Cost: $9.33\n"
    print("PASS 3.03: changed sessions and zero fee")

    raw = "  2030-01-02,ECHO,WAIT-UNTIL-NOON,0  "
    ns, _ = homework("strings", {"raw_transmission": raw})
    assert (ns["year"], ns["year_check"], ns["message"], ns["found_dawn"]) == (
        "2030", False, "WAIT UNTIL NOON", False)
    assert json.loads(ns["json_line"]) == {"date": "2030-01-02", "agent": "ECHO",
        "message": "WAIT UNTIL NOON", "confidence": 0, "contains_dawn": False}
    assert ns["raw_transmission"] == raw
    print("PASS 3.04: different year, absent keyword, and zero confidence")

    ns, _ = homework("boolean")
    record = {"product_name": "Practice Clutch", "category": "Auto Racing",
              "spec_number": "9.1", "effective_date": "2026-09-30"}
    categories = ["Auto Racing", "Drag Racing"]
    assert ns["validate_record"](record, ["1.1"], categories) is True
    assert ns["validate_record"](dict(record, effective_date="   "), ["1.1"], categories) is False
    assert ns["validate_record"](record, ["1.1", "9.1"], categories) is False
    print("PASS 3.05: separate blank-field and duplicate causes")

    ns, _ = homework("2026-09-29-conditionals")
    for amount, score, expected in [(100, 4, "Be a little careful, but this is probably fine.\n"),
                                    (101, 7, "This looks risky. Check with someone you trust before replying.\n")]:
        assert ns["score_message"]("gift cards", amount, True) == score
        assert printed(ns["report_risk"], score)[1] == expected
    print("PASS 3.06: 100/101 changes both score and reporting band")

    ns, _ = homework("nested-conditionals")
    student = {"logged_in": False, "homework_finished": True, "lunch_packed": True, "practice_today": True}
    assert ns["daily_routine"](student) == ["Log in first to view the student schedule."]
    assert ns["daily_routine"](dict(student, logged_in=True)) == [
        "Account ready: review today's schedule.", "Homework finished: attend practice, then dinner.",
        "Bring packed lunch and an extra practice snack."]
    print("PASS 3.07: login guard suppresses otherwise-ready recommendations")

    ns, _ = homework("iterations", {"match_latencies_ms": [39, 40, 90, 99]})
    assert tuple(ns[x] for x in ["checked_count", "skipped_count", "action_count",
                                 "total_action_latency_ms", "critical_found"]) == (3, 1, 2, 130, True)
    assert len(ns["match_latencies_ms"]) - ns["checked_count"] == 1
    print("PASS 3.08: skip, count-before-break, and uninspected suffix")

    ns, _ = homework("developing-algorithms")
    result, out = printed(ns["restock_report"], ["A", "B"], [5, 5], [10, 10])
    assert result == (["A", "B"], [5, 5], 10, 0)
    assert out == "Restock needed:\nA: need 5\nB: need 5\nTotal items needed: 10\nMost urgent: A (short by 5)\n"
    result, out = printed(ns["restock_report"], ["A", "B"], [10, 10], [10, 10])
    assert result == ([], [], 0, None) and out == "Fully stocked!\n"
    print("PASS 3.09: tie rule and exact-target stock")

    votes = ["granola", "granola", "granola", "fruit"]
    prices = [3, 4, 5, 6]
    ns, out = homework("lists", {"votes": votes, "prices": prices})
    assert ns["rounded_average"] == 4.5
    assert ns["votes"] == votes and ns["prices"] == prices
    assert out == "4\nfruit\nTotal: 18\nAverage: 4\n{'granola': 3, 'fruit': 1}\n['granola']\n"
    print("PASS 3.10: unseen category, qualifying threshold, and display truncation")

    ns, _ = homework("calling-procedures")
    for incident, label in [("Medical Emergency", "PRIORITY"), ("medical emergency", "STANDARD")]:
        assert printed(ns["dispatch_response"], incident_type=incident, location="Practice Zone E")[1] == (
            f"{label} RESPONSE: {incident} reported in Practice Zone E\n")
    print("PASS 3.12: keyword binding and exact-match rule")

    ns, _ = homework("developing-procedures")
    recipe = {"flour": 2, "milk": 1}
    assert ns["prepare_scaled_recipe"](recipe, 4, 6) == [
        "Dessert servings: 6", "flour: 3.0 cups", "milk: 1.5 cups"]
    assert recipe == {"flour": 2, "milk": 1}
    try:
        ns["prepare_scaled_recipe"](recipe, 4, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Zero servings accepted")
    print("PASS 3.13: new scaling ratio, preserved recipe, and invalid request")

    ns, _ = homework("libraries")
    games = [{"date": "2026-09-01", "opponent": "Comets", "points": 0},
             {"date": "2026-09-02", "opponent": "Comets", "points": 10}]
    assert ns["summarize_season"](games) == {"total_points": 10, "average_points": 5,
        "best_game": 10, "points_by_opponent": {"Comets": 10}}
    assert ns["summarize_season"]([]) == {"total_points": 0, "average_points": None,
        "best_game": None, "points_by_opponent": {}}
    print("PASS 3.14: zero-point observation versus missing data")

    ns, _ = homework("random")
    part = {"product_name": "Practice Clutch", "category": "Auto Racing", "spec_number": "9.1"}
    transcript, final = ns["simulate_qa"]([part], ["POST/create"], [], 3, 315)
    assert [row["status"] for row in transcript] == [201, 409, 409] and final == ["9.1"]
    print("PASS 3.15: state changes when random choices are held constant")

    ns, _ = homework("algorithmic-efficiency")
    efficiency = json.loads((ROOT / "_notebooks/homework/2026-09-30-algorithmic-efficiency-hw.ipynb").read_text())
    code = ["".join(c["source"]) for c in efficiency["cells"] if c["cell_type"] == "code"]
    for source, filename in zip(code, ["algorithmic-efficiency-popcorn.py", "algorithmic-efficiency.py"]):
        assert source.strip() == (ROOT / "assets/homework/2026-09-29" / filename).read_text().strip()
    search, _ = execute(code[0])
    for n, pairs, binary in [(7, 49, 3), (14, 196, 4)]:
        assert ns["catalog_work"](n) == {"books": n, "visits": n, "ordered_pairs": pairs}
        assert search["search_counts"](n) == (n, binary)
    assert "Full-credit justification and extension evidence" in (ROOT / "navigation/homework/3-17.md").read_text()
    print("PASS 3.17: three distinct growth patterns on changed sizes")
    print("PASS: all 13 written reviewer challenges match actual submitted code")


if __name__ == "__main__":
    main()
