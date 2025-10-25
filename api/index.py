# This file is the required entry point for Vercel deployment.

# Import the initialized Flask application instance from app.py
from app import app

# Explicitly define 'handler' for Vercel to reliably execute the application
handler = app
