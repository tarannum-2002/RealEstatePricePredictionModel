
from re import A
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/tara")
def tara():
    return "<p>Hello, tara!</p>"
    
app.run(debug=True)

