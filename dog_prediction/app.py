from pathlib import Path

from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename, escape

app = Flask(__name__,)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
app.secret_key = "192&as{)@(?as,"

UPLOAD_PATH = Path.cwd()/'uploads'
UPLOAD_PATH.mkdir(parents=True,exist_ok=True)
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}
app.config['UPLOAD_FOLDER'] = str(UPLOAD_PATH)


def allowed_file(filename, allowed_extensions=ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route("/")
def get_main():
    return render_template("hello.html")


@app.route("/", methods=["POST"])
def upload():
    # https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files
    if request.method == "POST":
        if "myfile" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files['myfile']
        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash(f"Please upload an image file with one of the following types: {', '.join(list(ALLOWED_EXTENSIONS))}."
                  f"The file {file.filename} doesn't seem to be of this type.")
            return redirect(request.url)
        else:
            filename = escape(secure_filename(file.filename))
            file.save(Path(app.config['UPLOAD_FOLDER']) / filename)
            flash("Image successfully uploaded")
            return redirect(url_for('predict', filename=filename))
    return render_template("hello.html")


@app.route('/predict/<filename>')
def predict(filename):
    filepath = 'http://127.0.0.1:5000/uploads/' + filename
    return render_template("predict.html", filepath=filepath)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run()
