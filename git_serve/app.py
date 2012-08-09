import random
from flask import Flask, render_template
from repo import GitServeRepo

app = Flask(__name__)

git_repo = GitServeRepo()

@app.route("/")
def home():
	return render_template("index.html",data=git_repo.get_frontpage_data())

def run_app():
	print "Starting app"
	app.run(debug=True)

