
from re import A
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/tara")
def tara():
    return "<p>Hello, tara!</p>"
    
app.run(debug=True)

