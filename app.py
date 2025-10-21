# app.py - FINAL ATTEMPT PATH LOGIC

# ... (rest of imports)

# Initialize Flask App
app = Flask(__name__)

# --- Load Content Data using Flask's open_resource ---
site_data = {}
try:
    # Use the full path with a leading slash to ensure Vercel looks from the root.
    with app.open_resource('/data/content.json') as f: 
        site_data = json.load(f)
    print("DEBUG: Data loaded successfully using app.open_resource.")

# ... (rest of the try/except block remains the same)
