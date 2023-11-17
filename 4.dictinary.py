
'''
Write the dictionaty structure for storing recipes for food.
Hardcode your own data.
Get user input for the name of the recipe, and then print the recipe. 
Eg: Input : Idli
Output : Here is the recipe for idli. 
You need ingrediants Rice and Dal.
 The procedure to cook is grind rice and dal, ferment and steam.
Input : Yogurt rice
Output :  Here is the recipe for Yogurt rice. 
You need ingrediants Rice and yogurt.
The procedure to cook is cook rice first and then add yogurt.
'''

recipes = {
    "Idli": {
        "ingredients": ["Rice", "Dal"],
        "procedure": "Grind rice and dal, ferment and steam."
    },
    "Yogurt rice": {
        "ingredients": ["Rice", "Yogurt"],
        "procedure": "Cook rice first and then add yogurt."
    }
}

user_input = input("Enter the name of the recipe: ")

if user_input in recipes:
    recipe = recipes[user_input]
    print(f"Here is the recipe for {user_input}.")
    print("You need ingredients:", ", ".join(recipe["ingredients"]))
    print("The procedure to cook is", recipe["procedure"])
else:
    print(f"Recipe for {user_input} not found.")