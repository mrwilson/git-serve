import random
from flask import Flask, render_template
from repo import GitServeRepo

app = Flask(__name__)

git_repo = GitServeRepo()

@app.route("/")
def home():
	return render_template("index.html",data=git_repo.get_frontpage_data(),name=git_repo.name)

@app.route("/commits")
def commits():
	return render_template("commits.html",commits=git_repo.get_commits(),name=git_repo.name)
		
def run_app():
	app.run(debug=True)
