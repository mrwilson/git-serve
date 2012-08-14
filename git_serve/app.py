# -*- coding: utf-8 -*-
import random
from flask import Flask, render_template
from repo import GitServeRepo

app = Flask(__name__)

git_repo = GitServeRepo()

name = git_repo.name

@app.route("/")
def home():
	return render_template("index.html",data=git_repo.get_frontpage_data(),name=name)

@app.route("/history")
def commits():
	return render_template("history.html",commits=git_repo.get_commits(),name=name)

@app.route("/commit/<commit_id>")
def commit(commit_id):
	if git_repo.commit_exists(commit_id):
		return render_template("commit.html",commit_data=git_repo.get_data_from_commit(commit_id),name=name)
	else:
		return error("No such commit exists in this repository")

def error(errormsg):
	return render_template("index.html",error=errormsg,data=git_repo.get_frontpage_data(),name=name)

def run_app():
	app.run()
