from app import app

from flask import render_template, request, redirect


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            return redirect(request.url)

    return render_template("public/upload_image.html")


@app.route("/")
def index():

    args = None

    if request.args:

        args = request.args

        return render_template("public/index.html", args=args)

    return render_template("public/index.html", args=args)



@app.route("/jinja")
def jinja():
    return render_template("public/jinja.html")


@app.route("/about")
def about():
    return render_template("public/about.html")
