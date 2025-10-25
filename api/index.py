# This file serves as the mandatory entry point for Vercel deployment when using the Python runtime.
# Vercel looks for a file inside the 'api' directory to handle incoming requests.

from app import app
# The 'app' variable holds the initialized Flask application instance from app.py.
# Vercel needs this exposed variable to execute the application code.

# You can optionally define a custom handler function if needed, 
# but simply exposing the app object is often sufficient.
# handler = app 
