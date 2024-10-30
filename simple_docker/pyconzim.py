from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', greeting="Hello PyCon Zim 2024!", caption="Group Picture from PyCon Zim 2018")