from flask import Flask, render_template
import json
import os
import sys
import socket 

# Initialize Flask App
app = Flask(__name__)

# --- REVISED PATH LOGIC ---
# Use Flask's root_path to reliably locate the 'data' directory 
# relative to the app's location, which is robust on Vercel.
DATA_PATH = os.path.join(app.root_path, 'data', 'content.json')

# --- Load Content Data ---
site_data = {}
try:
    # We use a context manager to ensure the file is closed
    with open(DATA_PATH, 'r') as f:
        site_data = json.load(f)
    print("DEBUG: Data loaded successfully.")

except FileNotFoundError:
    print("-" * 50)
    print("FATAL ERROR: DATA FILE NOT FOUND!")
    print(f"The application could not find the file: {DATA_PATH}")
    print("Ensure the 'data' folder is in the project root next to app.py.")
    print("-" * 50)
    sys.exit(1) # Exit immediately upon file path error

except json.JSONDecodeError:
    print("-" * 50)
    print("FATAL ERROR: CONTENT DECODE FAILURE!")
    print(f"The file {DATA_PATH} contains a syntax error.")
    print("Please review the JSON structure carefully.")
    print("-" * 50)
    sys.exit(1) # Exit immediately upon JSON error

@app.route('/')
def index():
    """Renders the main page, passing all content data to the Jinja2 template."""
    # The presence of site_data implies the file loaded, but we can double-check
    if not site_data:
        return "Internal Server Error: Application data failed to load.", 500
        
    return render_template('index.html', data=site_data) 

if __name__ == '__main__':
    # *** LOCAL RUNNER (ignored by Vercel) ***
    try:
        print("\nStarting Flask server...")
        app.run(debug=True, host='127.0.0.1', port=5001)
    except socket.error as e:
        print("-" * 50)
        print("CRITICAL NETWORK/SYSTEM ERROR!")
        print(f"Flask failed to bind to the port 5001. Error: {e}")
        print("Check if port 5001 is already in use.")
        print("-" * 50)
    except Exception as e:
        print(f"An unexpected error occurred during server startup: {e}")
