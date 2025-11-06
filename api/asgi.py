import os
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = ROOT_DIR / "backend"


# Add backend to Python path
sys.path.insert(0, str(BACKEND_DIR))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


from django.core.asgi import get_asgi_application
app = get_asgi_application()
