# -*- coding: utf-8 -*-
import random
from flask import Flask, render_template
from repo import GitServeRepo

app = Flask(__name__)

git_repo = GitServeRepo()

@app.route("/")
def home():
	return render_template("index.html",data=git_repo.get_frontpage_data(),name=git_repo.name)

@app.route("/history")
def commits():
	return render_template("history.html",commits=git_repo.get_commits(),name=git_repo.name)

@app.route("/commit/<commit_id>")
def commit(commit_id):
	if git_repo.commit_exists(commit_id):
		render_template("commit.html",commit_data=git_repo.get_data_from_commit(commit_id),name=git_repo.name)
	else:
		error("No such commit exists in this repository")

def error(errormsg):
	render_template("error.html",error=errormsg)

def run_app():
	app.run(debug=True)
