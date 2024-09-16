import pandas as pd
import os

# Collect user profile information
def collect_user_profile():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    skills = input("Enter your skills (comma-separated): ")
    experience = input("Enter your experience (e.g., years): ")
    career_goals = input("Enter your career goals: ")

    return {
        "Name": name,
        "Age": age,
        "Email": email,
        "Skills": skills,
        "Experience": experience,
        "Career Goals": career_goals
    }

# Save user profile to a CSV file
def save_user_profile(profile):
    file_path = 'user_profiles.csv'
    df = pd.DataFrame([profile])
    
    # If the file does not exist, create it and write the header
    if not os.path.isfile(file_path):
        df.to_csv(file_path, mode='w', header=True, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)

# Load and display all user profiles
def load_user_profiles():
    file_path = 'user_profiles.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print("All user profiles:")
        print(df)
    else:
        print("No profiles found. Please add some profiles first.")

# Main function
if __name__ == "__main__":
    action = input("Enter 'add' to add a profile or 'view' to view all profiles: ").strip().lower()
    if action == 'add':
        user_profile = collect_user_profile()
        save_user_profile(user_profile)
        print("User profile saved successfully!")
    elif action == 'view':
        load_user_profiles()
    else:
        print("Invalid action. Please enter 'add' or 'view'.")
