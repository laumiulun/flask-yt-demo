from app import app
import os
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename


# app.config["IMAGE_UPLOADS"] = "/Users/andy/projects/crystalGUI/flask-app/upload"
app.config["UPLOAD_FOLDER"] = "/Users/andy/projects/crystal_GUI/flask-app/upload"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


@app.route("/upload-data", methods=["GET", "POST"])
def upload_data():
    filename = "Please select STL file"
    if request.method == "POST":

        if request.files:

            data = request.files["file"]
            if data.filename  == "":
                print("No filename")
                return redirect(request.url)
            if allowed_data(data.filename):
                filename = secure_filename(data.filename)

                basedir = os.path.abspath(os.path.dirname(__file__))
                file_path = os.path.join(basedir,app.config["UPLOAD_FOLDER"],filename)
                data.save(file_path)
                print("Data Saved")

                return redirect(request.url)
            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("public/upload_data.html",filename = filename)

def allowed_data(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

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
