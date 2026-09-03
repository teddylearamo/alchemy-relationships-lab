import importlib.util
import sys
from pathlib import Path

server_dir = Path(__file__).resolve().parent / "server"

sys.path.insert(0, str(server_dir))

spec = importlib.util.spec_from_file_location("server_app", server_dir / "app.py")
server_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server_app)

app = server_app.app
Event = server_app.Event
Session = server_app.Session
Speaker = server_app.Speaker
Bio = server_app.Bio

events = Event
