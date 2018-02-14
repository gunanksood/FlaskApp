import os, time, sqlite3
import speech_recognition as sr

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/speech_to_text/<name>")
def profile(name):
    return render_template("speech_to_text.html", name=name)

@app.route("/web_api/<name>")
def web_api(name):
    return render_template("web_api.html", name=name)


if __name__ == "__main__":
    app.run()






