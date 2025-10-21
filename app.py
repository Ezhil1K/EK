# app.py

from flask import Flask, render_template
import json
import os
import sys
import socket

# Initialize Flask App
app = Flask(__name__)

# --- Load Content Data using Flask's open_resource ---
# This method uses paths relative to the application root and is the 
# most reliable way to access included files in Vercel/serverless environments.
site_data = {}
try:
    # 'data/content.json' is a path relative to the app's root folder.
    with app.open_resource('data/content.json') as f:
        site_data = json.load(f)
    print("DEBUG: Data loaded successfully using app.open_resource.")

except FileNotFoundError:
    print("-" * 50)
    print("FATAL ERROR: DATA FILE NOT FOUND!")
    print("The application could not find the file: data/content.json")
    print("Ensure the 'data' folder is in the project root.")
    print("-" * 50)
    sys.exit(1) # Exit immediately upon file path error

except json.JSONDecodeError:
    print("-" * 50)
    print("FATAL ERROR: CONTENT DECODE FAILURE!")
    print("Please review the JSON structure of content.json carefully.")
    print("-" * 50)
    sys.exit(1) # Exit immediately upon JSON error
    
# ... (The rest of your app.py remains the same, including @app.route('/') and if __name__ == '__main__')
