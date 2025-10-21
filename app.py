# app.py

# ... (imports)

# Initialize Flask App
app = Flask(__name__)

# --- FINAL GUARANTEED PATH FIX ---
# The file is now inside the 'templates' folder.
# We will use the simplest path relative to the app's root.
DATA_PATH = 'templates/content.json' 

# --- Load Content Data ---
site_data = {}
try:
    # Use standard Python open() with the simple relative path
    # NOTE: You could also use app.open_resource(DATA_PATH) here
    with open(DATA_PATH, 'r') as f:
        site_data = json.load(f)
    print("DEBUG: Data loaded successfully.")
# ... (rest of the try/except block remains the same)
