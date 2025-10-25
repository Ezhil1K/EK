# This file is the required entry point for Vercel deployment using the Python runtime.
# Vercel automatically routes requests to the exposed 'app' object in this directory.

from app import app
# Import the initialized Flask application instance (named 'app') from the main 'app.py' file.
# Vercel uses this specific object to serve the web application.

# You can optionally define a custom handler function if needed, 
# but simply exposing the 'app' object is the standard practice for Flask.
# handler = app 
