import json
from datetime import datetime
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

# --- Load Content Data ---
def load_data():
    """Loads content from JSON file, using a safe fallback."""
    try:
        # Assuming content.json is in the same directory as app.py
        with open('content.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Warning: content.json not found. Using default dummy data.")
        data = {} # Will be merged with defaults below
    except json.JSONDecodeError:
        print("Warning: content.json is corrupted. Using default dummy data.")
        data = {} # Will be merged with defaults below
    
    # Comprehensive Dummy Data for safety (matches index.html structure)
    default_data = {
        "title": "Technical Specialist Portfolio - Ezhil K",
        "email_address": "ezhil.k.contact@example.com",
        "linkedin_url": "https://linkedin.com/in/ezhilk",
        "logo_url": "images/logo.png",
        "current_year": datetime.now().year,
        "hero": {
            "subtitle": "Precision Engineering for Quality (Chemical Specialist)",
            "tagline": "Expertise in industrial cleaning, corrosion control, and chemical management."
        },
        "about": {
            "description": "Over 10 years experience optimizing manufacturing processes for technical cleanliness and corrosion control in the automotive sector."
        },
        "casestudies": [
            {
                "title": "Fluid Life Extension Project", 
                "summary": "Implemented a new filtration regime that doubled the life span of cutting fluids, reducing waste disposal costs by 45%.", 
                "tags": ["Sustainability", "Cost Reduction", "Filtration"]
            },
            {
                "title": "VDA 19.1 Cleanliness Audit", 
                "summary": "Led the certification process, achieving 100% compliance across three major assembly lines.", 
                "tags": ["Quality Control", "VDA 19.1", "Auditing"]
            },
            {
                "title": "New Chemical Dosing System", 
                "summary": "Designed and commissioned an automated dosing system, eliminating manual error and stabilizing bath concentrations.", 
                "tags": ["Automation", "Process Control", "Six Sigma"]
            }
        ],
        "projects": [
            {"name": "IoT Process Monitor Dashboard", "description": "Developed a real-time Power BI dashboard for remote process control and anomaly detection."},
            {"name": "Rust Prevention Protocol", "description": "Authored global standard operating procedures for VCI packaging and volatile corrosion inhibitor application."},
            {"name": "Microscopy Lab Setup", "description": "Established an in-house lab for particle analysis and residue identification using SEM/EDX."}
        ],
        "articles": {
            "cleanliness-risks": {"title": "The Hidden Costs of Technical Cleanliness Risks", "summary": "An analysis of how particle contamination affects warranty costs and component failure rates."},
            "vci-vs-oil": {"title": "VCI vs. Oil-Based Rust Prevention: A Comparative Review", "summary": "Detailed pros and cons of modern corrosion control methods in storage and transit."}
        }
    }

    # Merge data, prioritizing loaded content but ensuring structure from defaults
    merged_data = default_data.copy()
    merged_data.update(data)
    
    return merged_data

# --- Routes ---

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/article/<slug>')
def article(slug):
    data = load_data()
    # Simple article detail page placeholder
    if slug in data.get('articles', {}):
        article_data = data['articles'][slug]
        # In a real app, you would fetch the full content here.
        return render_template('article_template.html', data=data, article=article_data)
    
    return render_template('404.html', data=data), 404

# Route for Vercel deployment of static files (CSS/images)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.errorhandler(404)
def page_not_found(e):
    data = load_data()
    return render_template('404.html', data=data), 404

if __name__ == '__main__':
    app.run(debug=True)
