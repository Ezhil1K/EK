# This file is the entry point for Vercel deployment.
# It simply imports the Flask application instance from app.py.

from app import app as application 

# Vercel's Python runtime looks for an 'application' variable (a WSGI app)
# to handle all incoming web requests. All logic remains in 'app.py'.
