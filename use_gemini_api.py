import requests
import json

# Set up Gemini AI API credentials
api_key = "your API key"  # Replace with your new API key from GCP Console
model_name = "text-bison-001"
api_url = f"https://generativelanguage.googleapis.com/v1/models/{model_name}:generateText?key={api_key}"
# Define the user profile data structure
user_profile = {
    "aptitudes": ["problem-solving", "communication"],
    "aspirations": ["software engineering", "data science"],
    "abilities": ["python", "machine learning"],
    "experiences": ["internship", "project management"]
}

# Create the prompt
prompt_text = f"""
User Profile:
Aptitudes: {', '.join(user_profile['aptitudes'])}
Aspirations: {', '.join(user_profile['aspirations'])}
Abilities: {', '.join(user_profile['abilities'])}
Experiences: {', '.join(user_profile['experiences'])}

Based on this profile, provide personalized career recommendations.
"""

# Prepare the request payload
payload = {
    "prompt": {
        "text": prompt_text
    },
    "temperature": 0.7,         # Optional: Adjust temperature for response variability
    "maxOutputTokens": 150      # Adjust the number of tokens as needed
}

# Send a request to the Gemini AI API
response = requests.post(
    api_url,
    headers={
        "Content-Type": "application/json"
    },
    json=payload
)

# Parse the API response
if response.status_code == 200:
    response_json = response.json()
    ai_response = response_json.get('candidates', [{}])[0].get('output', '')  # Correct field for output text
    print("Personalized Career Recommendations:")
    print(ai_response)
else:
    print(f"Error: {response.status_code} - {response.text}")
