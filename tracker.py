# ------------------------------------------
# Author: Hiya
# Date: Automatically uses current system date
# Project Title: Daily Calorie Tracker
# ------------------------------------------

from datetime import date

# Get today's date
today = date.today()

# Welcome message and program intro
print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you log the food you eat and track your daily calorie intake.")
print("Use it to stay consistent with your health and nutrition goals.")
print(f"Date: {today}\n")

# Lists to store meal names and calorie amounts
meal_names = []
calorie_amounts = []

# Ask how many meals the user wants to enter
num_meals = int(input("How many meals do you want to enter? "))

# Loop to get meal data
for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calorie amount: "))
    
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Display entered data
print("\n--- Meal Log ---")
for i in range(num_meals):
    print(f"{meal_names[i]}: {calorie_amounts[i]} calories")

# Task 3: Calorie Calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / num_meals

print("\n--- Calorie Summary ---")
print(f"Total calories consumed: {total_calories}")
print(f"Average calories per meal: {average_calories:.2f}")

# Ask for user's daily calorie limit
daily_limit = float(input("\nEnter your daily calorie limit: "))

# Compare total intake to limit
if total_calories > daily_limit:
    print(" You have exceeded your daily calorie limit.")
elif total_calories < daily_limit:
    print(" You are within your daily calorie limit.")
else:
    print(" You have exactly met your daily calorie limit.")

# Print a neatly formatted summary table of meals, calories, total, and average

print("\n--- Daily Calorie Summary ---")
print(f"{'Meal Name':<15}\t{'Calories'}")
print("-" * 30)

for i in range(num_meals):
    print(f"{meal_names[i]:<15}\t{calorie_amounts[i]}")

print("-" * 30)
print(f"{'Total:':<15}\t{total_calories}")
print(f"{'Average:':<15}\t{average_calories:.2f}")

from datetime import datetime
# Ask user if they want to save the report
save_report = input("\nDo you want to save the session summary to a file? (yes/no): ").strip().lower()

if save_report == 'yes':
    # Get current date and time for timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    filename = "calorie_tracker_log.txt"
    
    with open(filename, "w") as file:
        file.write(f"Calorie Tracker Session Log\n")
        file.write(f"Timestamp: {timestamp}\n\n")
        
        file.write(f"{'Meal Name':<15}\t{'Calories'}\n")
        file.write("-" * 30 + "\n")
        
        for i in range(num_meals):
            file.write(f"{meal_names[i]:<15}\t{calorie_amounts[i]}\n")
        
        file.write("-" * 30 + "\n")
        file.write(f"{'Total:':<15}\t{total_calories}\n")
        file.write(f"{'Average:':<15}\t{average_calories:.2f}\n\n")
        
        # Calorie limit status
        if total_calories > daily_limit:
            file.write("Status: You have exceeded your daily calorie limit.\n")
        elif total_calories < daily_limit:
            file.write("Status: You are within your daily calorie limit.\n")
        else:
            file.write("Status: You have exactly met your daily calorie limit.\n")
    
    print(f"Session summary saved to '{filename}'.")
else:
    print("Session summary not saved.")
