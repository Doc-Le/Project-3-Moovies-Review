from app import app

IP = os.environ.get("IP", app.config["FLASK_RUN_HOST"])
PORT = int(os.environ.get("PORT", app.config["FLASK_RUN_PORT"]))


if __name__ == '__main__':
    app.run(
        host=IP,
        port=PORT,
        debug=True
    )
