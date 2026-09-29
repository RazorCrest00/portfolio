# CODE_RUNNER: 3.13 Exercise 3 - Decompose and verify
def validate_servings(servings):
    if type(servings) is not int or servings <= 0:
        raise ValueError("Servings must be a positive whole number")

def scale_ingredients(recipe, base_servings, requested_servings):
    validate_servings(base_servings)
    validate_servings(requested_servings)
    multiplier = requested_servings / base_servings
    scaled = {}
    for ingredient, cups in recipe.items():
        scaled[ingredient] = cups * multiplier
    return scaled

def format_recipe(ingredients, servings):
    lines = ["Dessert servings: " + str(servings)]
    for ingredient, cups in ingredients.items():
        lines.append(ingredient + ": " + str(cups) + " cups")
    return lines

def prepare_scaled_recipe(recipe, base_servings, requested_servings):
    ingredients = scale_ingredients(recipe, base_servings, requested_servings)
    return format_recipe(ingredients, requested_servings)

recipe = {"flour": 2, "milk": 1}
for line in prepare_scaled_recipe(recipe, 4, 8):
    print(line)
assert scale_ingredients(recipe, 4, 8) == {"flour": 4.0, "milk": 2.0}
assert scale_ingredients(recipe, 4, 2) == {"flour": 1.0, "milk": 0.5}
assert recipe == {"flour": 2, "milk": 1}
assert format_recipe({"flour": 4.0}, 8) == ["Dessert servings: 8", "flour: 4.0 cups"]
for invalid in [0, -1, 2.5, True]:
    try:
        validate_servings(invalid)
    except ValueError:
        print("Rejected invalid servings:", invalid)
    else:
        raise AssertionError("Invalid serving count was accepted")
print("Scaling, formatting, unchanged input, and validation checks: PASS")
