import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

def run_app():
	app.run(debug=True)

if __name__ == "__main__":
	run_app()
