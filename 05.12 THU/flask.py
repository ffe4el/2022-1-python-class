import flask

app = flask.Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Hello, World! sola so cute</p>"

app.run(debug=True, host="0.0.0.0")