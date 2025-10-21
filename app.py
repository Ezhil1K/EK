# app.py

# ... (rest of the file)

# --- FINAL PATH LOGIC ---
# Using the simple relative path 'data/content.json' 
# combined with the explicit include in vercel.json is the most reliable method.
DATA_PATH = 'data/content.json' 

# --- Load Content Data ---
site_data = {}
try:
    # Use standard Python open() with the simple relative path
    with open(DATA_PATH, 'r') as f:
        site_data = json.load(f)
    print("DEBUG: Data loaded successfully.")
    
# ... (rest of the try/except block using DATA_PATH)
