"""
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meter_test.settings')

application = get_wsgi_application()
"""

import os
import sys

# Add the project directory to the sys.path (Uncomment this and set the correct path)
sys.path.append('C:/Apache24/htdocs/meter_test')  # Make sure this path is correct

# Set the settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meter_test.settings')

# Import and get the WSGI application for serving the Django project
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
