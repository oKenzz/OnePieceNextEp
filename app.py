from flask import Flask
from server import server

app = Flask(__name__, static_folder='static')
app.register_blueprint(server, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")