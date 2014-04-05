# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "fosas"

# Descriptive title of project
TITLE = "Fosas"

# Google spreadsheet key
SPREADSHEET_KEY = "0Ak3IIavLYTovdHUybFZleWdTTGNVM3ZZb05rWmJ6WlE"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "tarbell.recoveredfactory.net/fosas",
    "staging": "tarbell.recoveredfactory.net/fosas",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'fosas',
    'title': 'Fosas'
}
