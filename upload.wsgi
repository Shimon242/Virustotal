# add to the /var/www/html/upload_app directory
import sys
import logging

logging.basicConfig(stream=sys.stderr)

# Add app directory to path
sys.path.insert(0, '/var/www/html/upload_app')

from app import app as application
