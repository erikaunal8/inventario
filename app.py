from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/promociones")
def productos():
    return "<h1>Las mejores promociones</h1>"

if __name__ == "__main__":
    app.run(debug=True)

