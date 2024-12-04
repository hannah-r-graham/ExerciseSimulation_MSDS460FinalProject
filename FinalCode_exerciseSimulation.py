# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Starting variables for model to build off and constant constraints

#constants 
moderate_exercise_met = 3.5
rigorous_exercise_met = 7
goal_weight = 165
timeSpentExercising = 30
height = 64 # inches
gender = 'female'

#variables
current_weight = 218 # lbs
age = 27
day = 1

# dataframes to store results
moderate_exercise_df = pd.DataFrame(columns=['day', 'case', 'weight', 'calories_burned', 'bmr'])
rigorous_exercise_df = pd.DataFrame(columns=['day', 'case', 'weight', 'calories_burned', 'bmr'])

# calculate BMR
def calculate_bmr_lbs(weight, height, age, gender):
    if gender == 'female':
        return (4.536 * weight) + (15.88 * height) - (5 * age) - 161
    else:
        return (4.536 * weight) + (15.88 * height) - (5 * age) + 5

# calculate calories burned
def calculate_calories_burned(met, weight, time):
    weight_kg = weight / 2.20462
    return (time * met * 3.5 * weight_kg) / 200

# %%
#### run the simulation for both moderate exercise and rigorous exercise separately

# %%
while current_weight > goal_weight:
    # Calculate BMR
    bmr = calculate_bmr_lbs(current_weight, height, age, gender)
    
    # Calculate calories burned for moderate exercise
    calories_burned_moderate = calculate_calories_burned(moderate_exercise_met, current_weight, timeSpentExercising)
    new_weight_moderate = current_weight - (calories_burned_moderate / 3500)
    
    # Append results to dataframe
    moderate_exercise_df = pd.concat([moderate_exercise_df, pd.DataFrame([{'day': day, 'case': 'moderate exercise', 'weight': new_weight_moderate, 'calories_burned': calories_burned_moderate, 'bmr': bmr}])], ignore_index=True)
    
    # Update current weight and day
    current_weight = new_weight_moderate
    day += 1
    
    # Update age every 365 days
    if day % 365 == 0:
        age += 1

# Reset current weight and day for next simulation
current_weight = 218 # lbs
day = 1

# %%
while current_weight > goal_weight:
    # Calculate BMR
    bmr = calculate_bmr_lbs(current_weight, height, age, gender)
    
    # Calculate calories burned for rigorous exercise
    calories_burned_rigorous = calculate_calories_burned(rigorous_exercise_met, current_weight, timeSpentExercising)
    new_weight_rigorous = current_weight - (calories_burned_rigorous / 3500)
    
    # Append results to dataframe 
    rigorous_exercise_df = pd.concat([rigorous_exercise_df, pd.DataFrame([{'day': day, 'case': 'rigorous exercise', 'weight': new_weight_rigorous, 'calories_burned': calories_burned_rigorous, 'bmr': bmr}])], ignore_index=True)
    
    # Update current weight and day
    current_weight = new_weight_rigorous
    day += 1

    # Update age every 365 days
    if day % 365 == 0:
        age += 1

# Combine dataframes for comparison
comparison_df = pd.concat([moderate_exercise_df, rigorous_exercise_df], ignore_index=True)
print(comparison_df)

# %%
moderate_exercise_df.info()
rigorous_exercise_df.info()

# %%
plt.figure(figsize=(12, 6))

# Plot moderate exercise data
plt.plot(moderate_exercise_df['day'], moderate_exercise_df['weight'], label='Moderate Exercise')

# Plot rigorous exercise data
plt.plot(rigorous_exercise_df['day'], rigorous_exercise_df['weight'], label='Rigorous Exercise')


plt.xlabel('Day')
plt.ylabel('Weight (lbs)')
plt.title('Weight Over Days for Moderate and Rigorous Exercise')
plt.legend()


plt.show()

# %%
plt.figure(figsize=(12, 6))

# Plot calories burned for moderate exercise
plt.plot(moderate_exercise_df['day'], moderate_exercise_df['calories_burned'], label='Moderate Exercise')

# Plot calories burned for rigorous exercise
plt.plot(rigorous_exercise_df['day'], rigorous_exercise_df['calories_burned'], label='Rigorous Exercise')


plt.xlabel('Day')
plt.ylabel('Calories Burned')
plt.title('Calories Burned Over Days for Moderate and Rigorous Exercise')
plt.legend()


plt.show()

# %%
# moderate_exercise_df.to_csv('moderate_exercise.csv', index=False)
# rigorous_exercise_df.to_csv('rigorous_exercise.csv', index=False)

# %%
#summary statistics for both cases

# %%
sum(moderate_exercise_df['calories_burned'])

# %%
sum(rigorous_exercise_df['calories_burned'])

# %%
plt.figure(figsize=(12, 6))

# Plot BMR for moderate exercise
plt.plot(moderate_exercise_df['day'], moderate_exercise_df['bmr'], label='Moderate Exercise')

# Plot BMR for rigorous exercise
plt.plot(rigorous_exercise_df['day'], rigorous_exercise_df['bmr'], label='Rigorous Exercise')

plt.xlabel('Day')
plt.ylabel('BMR')
plt.title('BMR Over Days for Moderate and Rigorous Exercise')
plt.legend()

plt.show()


