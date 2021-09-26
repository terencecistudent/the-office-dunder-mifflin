from flask import Flask, render_template, request, flash
import json
import os
import env

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    data = []
    with open("data/recent_news.json") as json_data:
        data = json.load(json_data)

    return render_template("index.html", recent_news=data)


@app.route("/news/<title>")
def news(title):
    news = {}

    with open("data/recent_news.json") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == title:
                single_news = obj

    return render_template("news.html", single_news=single_news)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/staff")
def staff():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

    return render_template("staff.html", company=data)


# @app.route("/about/<member_name>")
@app.route("/staff/<member_name>")
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            # if url in that particular element of array is equal to member_name, then member obj should equal our obj
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member)


@app.route("/careers")
def careers():
    return render_template("careers.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]), "success")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
