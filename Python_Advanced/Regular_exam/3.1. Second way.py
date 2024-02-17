def cookbook(*recipes):
    # Create a dictionary to store recipes by cuisine and count the number of recipes per cuisine
    cuisine_dict = {}
    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((name, ingredients))

    # Sort cuisines by the number of recipes (descending) and alphabetically
    sorted_cuisines = sorted(cuisine_dict.keys(), key=lambda c: (-len(cuisine_dict[c]), c))

    # Display the count of recipes and ingredients for each cuisine
    output = []
    for cuisine in sorted_cuisines:
        recipes_in_cuisine = sorted(cuisine_dict[cuisine], key=lambda r: r[0])
        output.append(f"{cuisine} cuisine contains {len(recipes_in_cuisine)} recipes:")
        for recipe_name, ingredients in recipes_in_cuisine:
            output.append(f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}")

    # Return the formatted output
    return "\n".join(output)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))