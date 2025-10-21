from flask import Flask, render_template
import json
import os
import sys
import socket

# Initialize Flask App
app = Flask(__name__)

# --- FINAL ROBUST PATH LOGIC FOR VERCEL ---
# Use the simplest relative path. This works because the Vercel 
# Python function executes from the project's root directory.
DATA_PATH = 'data/content.json' 

# --- Load Content Data ---
site_data = {}
try:
    # We use a context manager to ensure the file is closed
    with open(DATA_PATH, 'r') as f:
        site_data = json.load(f)
    print("DEBUG: Data loaded successfully.")
# ... (rest of the try/except block remains the same)
