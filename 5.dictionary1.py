
'''
Write the dictionaty structure for storing recipes for food.
Hardcode your own data.
User input is any ingredient. List all the recipes that include the ingredient
Input : Rice
Output : You can make Idli and Yogurt rice with rice.
'''

recipes = {
    "Idli": {
        "ingredients": ["Rice", "Urad dal", "Salt", "Water"],
    },
    "Yogurt Rice": {
        "ingredients": ["Rice", "Yogurt", "Salt", "Curd Rice Mix"],
    },
    "Pasta": {
        "ingredients":["Pasta", "Tomato Sauce", "Olive Oil", "Parmesan Cheese"],
    },
    "Chicken Curry":{
      "ingredients":["Chicken", "Onion", "Tomato", "Spices"]
    }
}

user_input = input("Enter an ingredient: ")

matching_recipes = []


for recipe, ingredients in recipes.items():
    if user_input in ingredients['ingredients']:
        matching_recipes.append(recipe)

if matching_recipes:
    print(f"You can make the following recipes with {user_input}: {', '.join(matching_recipes)}")
else:
    print(f"No recipes found that include {user_input}.")