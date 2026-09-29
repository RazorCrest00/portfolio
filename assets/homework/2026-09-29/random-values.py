# CODE_RUNNER: 3.15 Homework - Randomized QA simulator
import random


def apply_action(part, action, existing_specs):
    """Simulate an action against an in-memory set; return status and explanation."""
    spec = part["spec_number"]
    if action == "GET/search":
        if spec in existing_specs:
            return 200, "Record found"
        return 404, "Record not found"
    elif action == "POST/create":
        if spec in existing_specs:
            return 409, "Duplicate spec rejected"
        existing_specs.add(spec)
        return 201, "Record created"
    elif action == "PUT/update":
        if spec in existing_specs:
            return 200, "Existing record update accepted"
        return 404, "Cannot update missing record"
    elif action == "DELETE/remove":
        if spec in existing_specs:
            existing_specs.remove(spec)
            return 204, "Record removed"
        return 404, "Cannot remove missing record"
    else:
        return 400, "Unknown action"

def simulate_qa(parts, actions, existing_spec_numbers, test_count, seed):
    if type(test_count) is not int or test_count < 0:
        raise ValueError("test_count must be a nonnegative whole number")
    if test_count and (not parts or not actions):
        raise ValueError("Nonempty records and actions are required for positive runs")
    rng = random.Random(seed)
    existing = set(existing_spec_numbers)
    transcript = []
    for trial in range(1, test_count + 1):
        part = rng.choice(parts)
        action = rng.choice(actions)
        status, message = apply_action(part, action, existing)
        transcript.append({"trial": trial, "product_name": part["product_name"],
                           "category": part["category"], "spec_number": part["spec_number"],
                           "action": action, "status": status, "message": message})
    return transcript, sorted(existing)
parts = [
    {"product_name": "Replacement Flywheels", "category": "Auto Racing", "spec_number": "1.1"},
    {"product_name": "Multiple Disc Clutch Assemblies", "category": "Drag Racing", "spec_number": "1.2"},
    {"product_name": "Racing Flywheel Record", "category": "Auto Racing", "spec_number": "2.1"},
]

actions = ["GET/search", "POST/create", "PUT/update", "DELETE/remove"]
existing_spec_numbers = ["1.1", "2.1"]
test_count = 12
seed = 315
transcript, final_specs = simulate_qa(parts, actions, existing_spec_numbers, test_count, seed)
for row in transcript:
    print(str(row["trial"]) + ": " + row["action"] + " | " + row["product_name"] +
          " | " + row["category"] + " | " + row["spec_number"] +
          " -> " + str(row["status"]) + " " + row["message"])
print("Final existing specs:", final_specs)
print("Original input specs:", existing_spec_numbers)
