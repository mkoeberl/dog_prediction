from flask import Flask, render_template, request, flash, redirect
from pathlib import Path
from werkzeug.utils import secure_filename


app=Flask(__name__)

#https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
app.secret_key="192&as{)@(?as,"

UPLOAD_PATH = Path.cwd()/'upload'
UPLOAD_PATH.mkdir(parents=True, exist_ok=True)
ALLOWED_EXTENSIONS = {"jpg","jpeg","png","gif"}

def allowed_file(filename, allowed_extensions = ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route("/")
def get_main():
    return render_template("hello.html")

@app.route("/",methods=["POST"])
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
            filename = secure_filename(file.filename)
            file.save(UPLOAD_PATH/filename)
            flash("Image successfully uploaded")
            return redirect(request.url)
    return render_template("hello.html")

if __name__=='__main__':
    app.run()


