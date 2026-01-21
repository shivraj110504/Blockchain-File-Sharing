import os
from app import app

port = int(os.environ.get("PORT", 9000))
debug_mode = os.environ.get("FLASK_ENV", "development") != "production"
app.run(host='0.0.0.0', port=port, debug=debug_mode)