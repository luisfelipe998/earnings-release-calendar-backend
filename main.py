import os
from earnings_release.server import app

if __name__ == "__main__":
    if os.getenv("PORT"):
        app.run(host="0.0.0.0", port=int(os.getenv("PORT")))
    else:
        app.run(host="0.0.0.0", port=8000)
