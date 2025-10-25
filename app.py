import os
import json
from flask import Flask, render_template, abort

# Set up the Flask application instance
app = Flask(__name__, template_folder='templates', static_folder='images')

# Define the path to the content JSON file
CONTENT_PATH = os.path.join(os.path.dirname(__file__), 'content.json')

def load_data():
    """Load the content data from content.json."""
    try:
        with open(CONTENT_PATH, 'r') as f:
            data = json.load(f)
            # Ensure the current year is available for the footer
            data['current_year'] = 2025 # Placeholder/default year
            return data
    except FileNotFoundError:
        print(f"Error: {CONTENT_PATH} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {CONTENT_PATH}.")
        return {}

@app.route('/')
def index():
    """Route for the home page."""
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/article/<slug>')
def article(slug):
    """Route for specific articles, using the slug for routing."""
    data = load_data()
    # Check if the requested article slug exists in the articles dictionary in content.json
    if slug in data.get('articles', {}):
        template_name = data['articles'][slug].get('template', f'article_{slug}.html')
        
        # Check if the specific template file exists
        if not os.path.exists(os.path.join(app.template_folder, template_name)):
            # If the template file is missing, return 404
            return abort(404) 

        return render_template(template_name, data=data)
    else:
        # If the slug is not found in content.json, return 404
        return abort(404)

@app.errorhandler(404)
def page_not_found(e):
    """Custom error handler for 404 Not Found errors."""
    data = load_data()
    return render_template('404.html', data=data), 404

# Vercel requires this standard handler in a file named 'api/index.py'
# However, based on your file structure, 'app.py' seems to be the main entry point 
# which Vercel will wrap if 'api/index.py' is missing or points to it.
# If you are using 'api/index.py', the content of that file should simply be:
# from app import app
# 
# Otherwise, for local testing:
if __name__ == '__main__':
    app.run(debug=True)
