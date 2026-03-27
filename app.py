import streamlit as st
import random

st.title("💪 Fitness Planner")

goal = st.selectbox("Goal", ["lose", "gain", "maintain"])
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0)
age = st.number_input("Age", min_value=10, max_value=100)
activity = st.selectbox("Activity Level", ["low", "moderate", "high"])
diet = st.selectbox("Diet Preference", ["vegetarian", "non-vegetarian"])


def calculate_calories():
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    multipliers = {"low": 1.2, "moderate": 1.55, "high": 1.9}
    calories = bmr * multipliers[activity]

    if goal == "lose":
        calories -= 500
    elif goal == "gain":
        calories += 500

    return int(calories)


def generate_workout():
    workouts = {
        "lose": ["HIIT", "Running", "Cycling", "Jump Rope"],
        "gain": ["Weight Lifting", "Strength Training", "Push/Pull Split"],
        "maintain": ["Yoga", "Bodyweight Training", "Light Cardio"]
    }
    return random.sample(workouts[goal], 3)


def generate_meals(calories):
    meals = {
        "vegetarian": ["Oatmeal", "Quinoa Salad", "Lentil Soup"],
        "non-vegetarian": ["Chicken & Rice", "Egg Omelette", "Grilled Fish"]
    }
    return random.sample(meals[diet], 3)


if st.button("Generate Plan"):
    calories = calculate_calories()
    workout = generate_workout()
    meals = generate_meals(calories)

    st.subheader("🔥 Calories")
    st.write(calories)

    st.subheader("🏋️ Workout Plan")
    st.write(workout)

    st.subheader("🍽️ Meal Plan")
    st.write(meals)
