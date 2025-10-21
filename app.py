import json
import os
from flask import Flask, render_template

# Initialize Flask App
app = Flask(__name__)

# --- FINAL GUARANTEED PATH FIX: Use Flask's built-in Resource Loader ---
# Assuming 'content.json' is now in the 'templates' folder.
DATA_PATH = 'templates/content.json' 

site_data = {}
try:
    # Use app.open_resource for a path guaranteed to work by Flask/Vercel
    with app.open_resource(DATA_PATH, 'r') as f:
        site_data = json.load(f)
    # The print statement *should* appear in Vercel's Runtime Logs if successful
    print("DEBUG: Data loaded successfully using app.open_resource.")
except FileNotFoundError:
    # If this still fails, the file was not bundled or the path is wrong.
    print(f"ERROR: File not found at {DATA_PATH}. Current working directory: {os.getcwd()}")
    site_data = {"error": "data file missing"}
except json.JSONDecodeError as e:
    print(f"ERROR: Failed to decode JSON from {DATA_PATH}: {e}")
    site_data = {"error": "JSON decode failed"}
except Exception as e:
    print(f"CRITICAL ERROR during data loading: {e}")
    site_data = {"error": "Unknown data loading error"}

# --- Flask Routes ---
@app.route('/')
def home():
    # Pass the loaded data to the template
    return render_template('index.html', data=site_data)

# ... (other routes)
