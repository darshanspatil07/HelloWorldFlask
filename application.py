#!/usr/bin/python3
from flask import Flask, render_template

application = app = Flask(__name__)
app.secret_key = "Secret Key"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
    