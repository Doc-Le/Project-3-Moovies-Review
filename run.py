import os
from app import app

IP = os.environ.get("IP", "0.0.0.0")
PORT = int(os.environ.get("PORT", 5000))


if __name__ == '__main__':
    app.run(
        host=IP,
        port=PORT,
        debug=True
    )
