from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def get_main():
    return render_template("hello.html")

@app.route("/",methods=["POST"])
def upload():
    return render_template("hello.html")

if __name__=='__main__':
    app.run()