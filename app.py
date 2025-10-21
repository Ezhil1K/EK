from flask import Flask, render_template
import json
import os
import sys
import socket # Added for network error handling

app = Flask(__name__)

# Define the path to the JSON data file
# This variable uses absolute paths based on where app.py is located.
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'content.json')

# --- Load Content Data ---
site_data = {}
try:
    print(f"DEBUG: Attempting to load data from: {DATA_PATH}")
    with open(DATA_PATH, 'r') as f:
        site_data = json.load(f)
    print("DEBUG: Data loaded successfully.")
except FileNotFoundError:
    print("-" * 50)
    print("FATAL ERROR: DATA FILE NOT FOUND!")
    print(f"The application could not find the file: {DATA_PATH}")
    print("Please check your folder structure:")
    print(" - Is the 'data' folder next to 'app.py'?")
    print(" - Is 'content.json' inside the 'data' folder?")
    print("-" * 50)
    sys.exit(1) # Exit immediately upon file path error
except json.JSONDecodeError:
    print("-" * 50)
    print("FATAL ERROR: CONTENT DECODE FAILURE!")
    print(f"The file {DATA_PATH} contains a syntax error (e.g., missing comma, unclosed bracket).")
    print("Please review the JSON structure carefully.")
    print("-" * 50)
    sys.exit(1) # Exit immediately upon JSON error

@app.route('/')
def index():
    """Renders the main page, passing all content data to the Jinja2 template."""
    return render_template('index.html', 
                           data=site_data) 
    # Flask will automatically look for 'index.html' inside the 'templates/' folder.

if __name__ == '__main__':
    # *** WRAPPED app.run() IN TRY...EXCEPT TO CATCH SYSTEM/NETWORK ERRORS ***
    try:
        print("\nStarting Flask server...")
        app.run(debug=True, host='127.0.0.1', port=5001)
    except socket.error as e:
        print("-" * 50)
        print("CRITICAL NETWORK/SYSTEM ERROR!")
        print(f"Flask failed to bind to the port 5001. Error: {e}")
        print("This usually means:")
        print("1. Another program is already using port 5001 (Port Conflict).")
        print("2. Your firewall or antivirus software is blocking Python's network access (Security Block).")
        print("Please check these external factors.")
        print("-" * 50)
    except Exception as e:
        print(f"An unexpected error occurred during server startup: {e}")
        
