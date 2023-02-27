"""
Dereck Watters flask app
"""
from datetime import datetime

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


def get_date():
    """
    This function gets the current date (e.g. April 24, 2020).
    :return: date
    """
    today = datetime.today()
    date = today.strftime("%B %d, %Y")  # Month, day and year

    return date


@app.route("/")
def index():
    """
    renders index .html
    """
    date = get_date()

    return render_template("index.html", content=[date])


@app.route("/about")
def about():
    """
    renders the about page
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """
    renders contact page
    """
    return render_template("contact.html")


@app.route("/admin")
def admin():
    """
    redirects to the index page
    """
    return redirect((url_for("index")))

if __name__ == "__main__":
    app.run()
