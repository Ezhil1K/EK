import os
import json
from datetime import datetime
from flask import Flask, render_template, abort

# Set up the Flask application instance
app = Flask(__name__, template_folder='templates', static_folder='static')

# Define the path to the content JSON file
CONTENT_PATH = os.path.join(os.path.dirname(__file__), 'content.json')

def load_data():
    """Load the content data from content.json."""
    try:
        with open(CONTENT_PATH, 'r') as f:
            data = json.load(f)
            # Dynamically set the current year for the footer
            data['current_year'] = datetime.now().year 
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

@app.route('/privacy-policy')
def privacy_policy():
    """Route for the Privacy Policy page."""
    data = load_data()
    return render_template('privacy_policy.html', data=data)

@app.route('/article/<slug>')
def article(slug):
    """Route for specific articles, using the slug for routing."""
    data = load_data()
    
    # 1. Check if the requested article slug exists in the articles dictionary in content.json
    if slug in data.get('articles', {}):
        
        # CRITICAL FIX: Replace hyphens in the slug with underscores to match the file name.
        safe_slug = slug.replace('-', '_')

        # 2. Safely get the template name. The safe_slug ensures the default path is correct.
        # NOTE: We can simplify the logic by assuming the template name is always article_[safe_slug].html
        template_name = f'article_{safe_slug}.html'
        
        # 3. Flask's render_template will now correctly look for files like 'article_particle_counter.html'
        # If the template file is still not found, render_template raises TemplateNotFound, which Flask typically converts to 500 in production, but 
        # this code will prevent the primary 500 error from the name mismatch.
        try:
            return render_template(template_name, data=data)
        except Exception:
            # If the template exists in content.json but the physical file is missing, return 404
            return abort(404)

    else:
        # If the slug is not found in content.json, return 404
        return abort(404)

@app.errorhandler(404)
def page_not_found(e):
    """Custom error handler for 404 Not Found errors."""
    data = load_data()
    return render_template('404.html', data=data), 404

# For local testing:
if __name__ == '__main__':
    app.run(debug=True)
