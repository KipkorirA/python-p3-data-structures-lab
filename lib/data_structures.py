spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Returns a list of food names
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Returns the foods with the highest heat levels (over 5)
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Prints all foods with heat levels represented by 🌶 emojis
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Returns the food that matches the given cuisine
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

def print_spiciest_foods(spicy_foods):
    # Prints foods with heat levels over 5 with 🌶 emojis
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    # Returns the average heat level of the foods
    return sum(food["heat_level"] for food in spicy_foods) // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # Returns the list of spicy foods with the new spicy food added
    return spicy_foods + [spicy_food]
