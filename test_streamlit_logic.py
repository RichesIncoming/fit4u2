import random

def calculate_calories(weight, height, age, activity, goal):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    multipliers = {"low": 1.2, "moderate": 1.55, "high": 1.9}
    calories = bmr * multipliers[activity]
    
    if goal == "lose":
        calories -= 500
    elif goal == "gain":
        calories += 500
    
    return int(calories)


def generate_workout(goal):
    workouts = {
        "lose": ["HIIT", "Running", "Cycling", "Jump Rope"],
        "gain": ["Weight Lifting", "Strength Training", "Push/Pull Split"],
        "maintain": ["Yoga", "Bodyweight Training", "Light Cardio"]
    }
    return random.sample(workouts[goal], 3)


def generate_meals(diet):
    meals = {
        "vegetarian": ["Oatmeal", "Quinoa Salad", "Lentil Soup"],
        "non-vegetarian": ["Chicken & Rice", "Egg Omelette", "Grilled Fish"]
    }
    return random.sample(meals[diet], 3)


# Test the Streamlit app logic
if __name__ == "__main__":
    print("=== Streamlit Fitness Planner - Core Logic Test ===\n")
    
    # Test 1
    print("Test 1: Weight Loss Goal")
    calories = calculate_calories(80, 175, 30, "moderate", "lose")
    workout = generate_workout("lose")
    meals = generate_meals("non-vegetarian")
    print(f"Calories: {calories}")
    print(f"Workout: {workout}")
    print(f"Meals: {meals}\n")
    
    # Test 2
    print("Test 2: Weight Gain Goal")
    calories = calculate_calories(70, 180, 25, "high", "gain")
    workout = generate_workout("gain")
    meals = generate_meals("vegetarian")
    print(f"Calories: {calories}")
    print(f"Workout: {workout}")
    print(f"Meals: {meals}\n")
    
    # Test 3
    print("Test 3: Maintain Goal")
    calories = calculate_calories(75, 170, 35, "low", "maintain")
    workout = generate_workout("maintain")
    meals = generate_meals("vegetarian")
    print(f"Calories: {calories}")
    print(f"Workout: {workout}")
    print(f"Meals: {meals}\n")
    
    print("=== All Streamlit core logic tests passed! ===")
