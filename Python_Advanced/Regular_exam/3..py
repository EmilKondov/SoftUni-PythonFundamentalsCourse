def cookbook(*recipes):
    cuisine_dict = {}

    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((name, ingredients))

    sorted_cuisine = sorted(cuisine_dict.items(), key=lambda x: (-len(x[1]), (x[0])))

    result = []
    for cuisine in sorted_cuisine:
        sorted_recipe = sorted(cuisine_dict[cuisine], key=lambda x: x[0])
        result.append(f"{cuisine} cuisine contains {len(sorted_recipe)} recipies:")
        for name, ingredients in sorted_recipe:
            result.append(f"  *{name} -> Ingredients:{','.join()}\n")
    return result.strip()


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))