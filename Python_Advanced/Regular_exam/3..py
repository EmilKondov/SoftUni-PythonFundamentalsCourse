def cookbook(*elements):
    sorted_cuisine = {}

    for recipe, cuisine, ingredients in elements:
        if cuisine not in sorted_cuisine:
            sorted_cuisine[cuisine] = []
        sorted_cuisine[cuisine].append(recipe)
        sorted_cuisine[cuisine].append(ingredients)

    sorted_cuisine = dict(sorted(sorted_cuisine.items(), key=lambda x: (-len(x[1]), (x[0]))))

    result = ''
    for cuisine, recipe in sorted_cuisine.items():
        sorted_recipe = sorted(recipe, key=lambda x: x[0])
        result += f"{cuisine} - {len(recipe)}\n"
        for name in sorted_recipe:
            result += f"  *{name} -> Ingredients:{','.join(recipe[1])}\n"
    return result.strip()


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))