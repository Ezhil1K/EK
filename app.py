import json
import os
from flask import Flask, render_template
from datetime import datetime

# Initialize Flask App
# Note: For Vercel deployment, the application entry point should remain 'app'
app = Flask(__name__)

# Define the path to the data file
DATA_PATH = 'templates/content.json'

# --- Safe Default Data Structure ---
# This dictionary ensures that the Jinja templates always have values for the keys
# they expect, preventing KeyErrors even if content.json fails to load.
def get_safe_default_data(error_msg="Check content.json"):
    return {
        "logo_url": "https://placehold.co/32x32/10b981/ffffff?text=EK", # New safe default
        "hero_video_url": "",
        "about_me": f"Data Loading Error: {error_msg}. Please update content.json.",
        "casestudies": [],
        "skills": [],
        "projects": [],
        "articles": [],
        "email_address": "ezhil.1ek@hotmail.com", # Safe default for template rendering
        "linkedin_url": "#",
        "phone_number": "+91-99-786-45456", # Safe default for template rendering
        "current_year": datetime.now().year, # Safe default for footer
        "error_message": error_msg
    }

# --- Data Loading Logic ---
# Load data globally once when the application starts
site_data = get_safe_default_data("Initialising...")
try:
    # Use app.open_resource for a path guaranteed to work by Flask/Vercel
    # Added 'encoding' for safety
    with app.open_resource(DATA_PATH, 'r', encoding='utf-8') as f:
        site_data = json.load(f)
        # Ensure current_year is available in loaded data if not explicitly set in JSON
        if 'current_year' not in site_data:
             site_data['current_year'] = datetime.now().year

    print("DEBUG: Data loaded successfully using app.open_resource.")
except FileNotFoundError:
    error_msg = f"File not found at {DATA_PATH}. Current working directory: {os.getcwd()}"
    print(f"ERROR: {error_msg}")
    site_data = get_safe_default_data(error_msg)
except json.JSONDecodeError as e:
    error_msg = f"Failed to decode JSON from {DATA_PATH}: {e}"
    print(f"ERROR: {error_msg}")
    site_data = get_safe_default_data(error_msg)
except Exception as e:
    error_msg = f"CRITICAL ERROR during data loading: {e}"
    print(f"CRITICAL ERROR: {error_msg}")
    site_data = get_safe_default_data(error_msg)


# --- Flask Routes ---
@app.route('/')
def home():
    # Defensive check: ensure the data object being passed is always a dictionary,
    # even if an unexpected error occurred during global loading.
    final_data = site_data if isinstance(site_data, dict) else get_safe_default_data("Route-level Data Fail")
    
    # Pass the loaded data (which is guaranteed to have the minimum required keys)
    return render_template('index.html', data=final_data)

# If running locally (not strictly necessary for Vercel, but good practice)
if __name__ == '__main__':
    app.run(debug=True)
