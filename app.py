from flask import Flask
from server import server

app = Flask(__name__, static_folder='static')
app.register_blueprint(server, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=5500)