from flask import Blueprint, render_template, request, jsonfiy, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name=" Hello, VST")

@views.route("/profile")
def profile():
    return render_template("profiel.html")


@views.route("/json")
def get_json():
    return jsonify({'name': 'size', 'of your shirt': 10})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))


