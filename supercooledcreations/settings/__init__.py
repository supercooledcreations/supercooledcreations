# Imports
import json

# Excluded from base settings DEBUG, SECRET_KEY, and DATABASES

# Attempt to find production settings
try:
    with open('/opt/supercooledcreations/production_settings.json') as file:
        production_settings = json.load(file)
    DEBUG = production_settings['DEBUG']
    SECRET_KEY = production_settings['SECRET_KEY']
    DATABASES = production_settings['DATABASES']
    from .base_settings import *
    use_production_settings = True

except FileNotFoundError:
    use_production_settings = False

# If no produciton settings attempt to load local settings
if not use_production_settings:
    try:
        from .local_settings import *
        from .base_settings import *
    except ImportError:
        print("No settings found")



