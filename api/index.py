"""
Serverless entrypoint for Django on Vercel.
- Uses Vercel-provided environment variables (already injected at runtime).
- Boots Django with settings module `japhestech.settings`.
- Exposes a WSGI app named `app` (what the Vercel Python runtime expects).
- Serves collected static files from STATIC_ROOT via WhiteNoise when path starts with /static/.
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Resolve project root (one level above this api/ directory) and add to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Configure Django settings from env (Vercel injects env vars automatically)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "japhestech.settings")

# Initialize the standard Django WSGI application
django_app = get_wsgi_application()

# Wrap with WhiteNoise to serve files from STATIC_ROOT at /static/...
static_root = os.getenv("STATIC_ROOT", str(BASE_DIR / "staticfiles"))
whitenoise_app = WhiteNoise(django_app, root=static_root, prefix="static/")

# Vercel looks for a callable named `app`
app = whitenoise_app
