from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "My firt post",
        "body": "Here is text of post",
        "author": "Oliveira",
        "created": datetime(2022,7,25)
    },
    {
        "title": "My second post",
        "body": "Here is text of post",
        "author": "Ikaro",
        "created": datetime(2022,7,26)
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)
