from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(port=5001)
