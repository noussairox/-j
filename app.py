from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/flash")
def flash():
    return render_template('flash.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
