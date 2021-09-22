import os
from app import app

IP = os.environ.get("IP", app.config["IP"])
PORT = int(os.environ.get("PORT", app.config["PORT"]))


if __name__ == '__main__':
    app.run(
        host=IP,
        port=PORT,
        debug=True
    )
