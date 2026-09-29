from fitness_utils import (
    calculate_bmi,
    calculate_daily_calories,
    calculate_water_intake,
    generate_workout_plan,
)


GOALS = {
    "1": "to stay fit",
    "2": "to improve stamina",
    "3": "build strength",
}

MEAL_PLANS = {
    "vegetarian": {
        "Breakfast": "Poha or upma with vegetables and a little fruit",
        "Lunch": "Dal and rice with salad and curd",
        "Dinner": "Roti with vegetables, paneer or beans, and soup",
        "Snack": "Fruit and a handful of nuts",
    },
    "non-vegetarian": {
        "Breakfast": "Eggs with poha or whole-wheat toast",
        "Lunch": "Chicken or fish with brown rice and vegetables",
        "Dinner": "Roti with chicken, salad, and green vegetables",
        "Snack": "Fruit and a boiled egg",
    },
}


def get_user_details():
    """Ask for the basic information needed to build a plan."""
    name = input("Your name: ").strip()
    age = int(input("Your age: "))
    gender = input("Gender (male/female): ").strip().lower()
    weight = float(input("Weight in kg: "))
    height = float(input("Height in cm: "))

    print("\nWhat's your main goal?")
    print("1. Stay fit\n2. Improve stamina\n3. Build strength")
    goal = GOALS.get(input("Choose 1-3: ").strip(), "not specified")

    print("\nWhat's your food preference?")
    print("1. Vegetarian\n2. Non-vegetarian")
    diet_choice = input("Choose 1-2: ").strip()
    diet_plan = {"1": "vegetarian", "2": "non-vegetarian"}.get(
        diet_choice, "not specified"
    )

    print("\nWhat's your current workout level?")
    print("1. Beginner\n2. Intermediate")
    level_choice = input("Choose 1-2: ").strip()
    workout_level = {"1": "beginner", "2": "intermediate"}.get(
        level_choice, "beginner"
    )

    has_health_issue = input(
        "Do you have a health issue or medical condition? (yes/no): "
    ).strip().lower() == "yes"

    return name, age, gender, weight, height, goal, diet_plan, workout_level, has_health_issue


def show_profile(name, age, gender, goal, diet_plan, bmi, bmi_category):
    """Print a short summary of the user's profile."""
    status_messages = {
        "Underweight": "Your BMI is below the usual range.",
        "Healthy weight": "Your BMI is in the usual range.",
        "Overweight": "Your BMI is above the usual range.",
        "Obese": "Your BMI is high; consider getting advice from a health professional.",
    }

    print("\nYOUR PROFILE")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Goal:", goal)
    print("Diet:", diet_plan)
    print(f"BMI: {bmi} ({bmi_category})")
    print("BMI status:", status_messages[bmi_category])


def show_weekly_plan(exercises, reps):
    """Lay out the first four suggested exercises across the week."""
    print("\nWEEKLY PLAN")
    for day, exercise in zip(("Monday", "Tuesday"), exercises[:2]):
        print(f"{day}: {exercise} - {reps}")
    print("Wednesday: Rest day; try a recovery walk or some stretching.")
    for day, exercise in zip(("Thursday", "Friday"), exercises[2:4]):
        print(f"{day}: {exercise} - {reps}")
    print("Saturday: Light activity and a short core routine.")
    print("Sunday: Rest day.")


def show_bmi_advice(category):
    advice = {
        "Underweight": "Focus on strength training and nourishing, calorie-rich foods.",
        "Healthy weight": "Keep a balanced routine and stay consistent.",
        "Overweight": "Walking, cardio, and balanced portions may be helpful.",
        "Obese": "Start gently and consider discussing a suitable plan with a professional.",
    }
    print("BMI advice:", advice[category])


def show_meal_plan(diet_plan):
    meals = MEAL_PLANS.get(diet_plan, MEAL_PLANS["non-vegetarian"])
    print("\nMEAL SUGGESTION")
    for meal, suggestion in meals.items():
        print(f"{meal}: {suggestion}")
    print("Meal note: Include protein and a variety of foods in balanced portions.")
    print("Hydration tip: Drink regularly throughout the day.")


def main():
    print("FAT 2 FIT — GYM AND DIET PLANNER")
    print("Let's put together a simple fitness plan.\n")

    (
        name,
        age,
        gender,
        weight,
        height,
        goal,
        diet_plan,
        workout_level,
        has_health_issue,
    ) = get_user_details()

    bmi, bmi_category = calculate_bmi(weight, height)
    calories = calculate_daily_calories(
        age, gender, weight, height, activity_level="moderate"
    )
    water_intake = calculate_water_intake(weight, gender)

    walking_minutes = {
        "to stay fit": 25,
        "to improve stamina": 35,
        "build strength": 30,
    }.get(goal, 30)
    exercises, walking_plan, goal_note, reps = generate_workout_plan(
        gender, goal, workout_level, walking_minutes
    )

    health_note = (
        "Please check with your doctor before starting strenuous exercise. "
        "Keep activity light until you know what's appropriate for you."
        if has_health_issue
        else "Start at a comfortable pace and adjust the plan to how you feel."
    )

    show_profile(name, age, gender, goal, diet_plan, bmi, bmi_category)

    print("\nYOUR WORKOUT PLAN")
    print("Level:", workout_level)
    print(goal_note)
    print("Rep pattern:", reps)
    print(walking_plan)
    print("Health note:", health_note)
    print("Exercises:")
    for exercise in exercises:
        print("-", exercise)

    show_weekly_plan(exercises, reps)

    goal_tips = {
        "to improve stamina": "Keep a steady pace and build up gradually.",
        "build strength": "Focus on good form and give yourself time to recover.",
    }
    print("\nTip:", goal_tips.get(
        goal, "Consistency matters more than trying to do everything at once."
    ))

    print("\nDAILY NEEDS")
    print(f"Estimated daily calories: {calories} kcal")
    print(f"Suggested daily water intake: {water_intake} L")
    show_bmi_advice(bmi_category)
    show_meal_plan(diet_plan)

    print("\nYour plan is ready. All the best,", name + "!")
    print("Stay consistent, and take care.")


if __name__ == "__main__":
    main()