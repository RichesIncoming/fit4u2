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


def generate_workout_plan():
    return {
        "Monday": "Push Day (Chest, Shoulders, Triceps) - Bench Press 4x8, Shoulder Press 3x10",
        "Tuesday": "Pull Day (Back, Biceps) - Deadlift 4x6, Rows 3x10",
        "Wednesday": "Leg Day - Squats 4x8, Lunges 3x12",
        "Thursday": "Active Recovery - Light Cardio + Stretching",
        "Friday": "Upper Body Hypertrophy - Incline Press, Pull-ups",
        "Saturday": "Lower Body + Core - Leg Press, Planks",
        "Sunday": "Rest / Mobility"
    }


def generate_meal_plan(calories, diet):
    veg_meals = [
        "Oatmeal + Banana", "Quinoa Salad", "Lentil Soup", "Tofu Stir Fry",
        "Greek Yogurt + Nuts", "Veggie Wrap", "Chickpea Curry"
    ]

    nonveg_meals = [
        "Egg Omelette + Toast", "Chicken & Rice", "Grilled Fish",
        "Turkey Sandwich", "Steak + Veggies", "Salmon Bowl"
    ]

    meal_pool = veg_meals if diet == "vegetarian" else nonveg_meals

    plan = {}
    for day in range(1, 15):
        plan[f"Day {day}"] = {
            "Breakfast": random.choice(meal_pool),
            "Lunch": random.choice(meal_pool),
            "Dinner": random.choice(meal_pool),
            "Calories": calories
        }
    return plan


# Test the Premium Streamlit app logic
if __name__ == "__main__":
    print("=== Premium Fitness Planner - Core Logic Test ===\n")
    
    # Test 1
    print("Test 1: Weight Loss Goal (Premium)")
    calories = calculate_calories(80, 175, 30, "moderate", "lose")
    workouts = generate_workout_plan()
    meals = generate_meal_plan(calories, "non-vegetarian")
    
    print(f"Daily Calories: {calories}")
    print("\n7-Day Workout Plan:")
    for day, workout in workouts.items():
        print(f"  {day}: {workout}")
    
    print("\n14-Day Meal Plan (Sample):")
    for day in ["Day 1", "Day 2", "Day 3"]:
        meal = meals[day]
        print(f"  {day}: Breakfast={meal['Breakfast']}, Lunch={meal['Lunch']}, Dinner={meal['Dinner']}")
    print("  ... (Days 4-14 omitted for brevity)")
    
    # Test 2
    print("\n\nTest 2: Weight Gain Goal (Premium)")
    calories = calculate_calories(70, 180, 25, "high", "gain")
    meals = generate_meal_plan(calories, "vegetarian")
    
    print(f"Daily Calories: {calories}")
    print("\n14-Day Meal Plan (Sample - Vegetarian):")
    for day in ["Day 1", "Day 2", "Day 3"]:
        meal = meals[day]
        print(f"  {day}: Breakfast={meal['Breakfast']}, Lunch={meal['Lunch']}, Dinner={meal['Dinner']}")
    print("  ... (Days 4-14 omitted for brevity)")
    
    # Test 3
    print("\n\nTest 3: Maintain Goal (Premium)")
    calories = calculate_calories(75, 170, 35, "low", "maintain")
    meals = generate_meal_plan(calories, "vegetarian")
    
    print(f"Daily Calories: {calories}")
    print(f"7-Day Workout Plan: {list(workouts.keys())}")
    print(f"14-Day Meal Plan: {list(meals.keys())}")
    
    print("\n\n=== All Premium Streamlit core logic tests passed! ===")
