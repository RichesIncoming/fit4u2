import streamlit as st
import random

st.set_page_config(page_title="Fitness Pro Planner", layout="wide")

st.title("💪 Fitness Pro Planner (Premium)")
st.caption("AI-powered fitness & nutrition planning")

# --- Subscription Gate ---
if "subscribed" not in st.session_state:
    st.session_state.subscribed = False

if not st.session_state.subscribed:
    st.subheader("🔒 Premium Access Required")
    st.write("Subscribe for a 1-month personalized fitness & meal plan.")
    if st.button("Subscribe - $9.99/month"):
        st.session_state.subscribed = True
        st.success("Subscription active! 🎉")
    st.stop()

# --- User Inputs ---
goal = st.selectbox("Goal", ["lose", "gain", "maintain"])
weight = st.number_input("Weight (kg)", 30.0, 200.0)
height = st.number_input("Height (cm)", 100.0, 250.0)
age = st.number_input("Age", 10, 100)
activity = st.selectbox("Activity Level", ["low", "moderate", "high"])
diet = st.selectbox("Diet Preference", ["vegetarian", "non-vegetarian"])

# --- Calorie Calculation ---
def calculate_calories():
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    multipliers = {"low": 1.2, "moderate": 1.55, "high": 1.9}
    calories = bmr * multipliers[activity]

    if goal == "lose":
        calories -= 500
    elif goal == "gain":
        calories += 500

    return int(calories)

# --- Workout Generator (7 Days Detailed) ---
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

# --- Meal Generator (14 Days) ---
def generate_meal_plan(calories):
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

# --- Generate Plan ---
if st.button("Generate Premium Plan"):
    calories = calculate_calories()
    workouts = generate_workout_plan()
    meals = generate_meal_plan(calories)

    st.subheader("🔥 Daily Calories Target")
    st.write(calories)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏋️ 7-Day Workout Plan")
        for day, workout in workouts.items():
            st.write(f"**{day}:** {workout}")

    with col2:
        st.subheader("🍽️ 14-Day Meal Plan")
        for day, meal in meals.items():
            st.write(f"**{day}**")
            st.write(meal)

    st.success("Your premium fitness plan is ready! 💥")
