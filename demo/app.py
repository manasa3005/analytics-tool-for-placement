from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inner-page")
def inner_page():
    return render_template("inner-page.html")

@app.route("/portfolio-details")
def portfolio():
    return render_template("portfolio-details.html")

if __name__ == "__main__":
    app.run(debug=False, port=4000)
