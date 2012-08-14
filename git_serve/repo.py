# -*- coding: utf-8 -*-
from git import Repo
from git.exc import InvalidGitRepositoryError, BadObject
import os, sys, datetime

class GitServeRepo(object):
	
	def __init__(self,path=os.getcwd()):
		self.setup(path)
	
	def setup(self, path):
		try:
			self.repo = Repo(os.getcwd())
			self.name = self.repo.index.path
		except InvalidGitRepositoryError:
			print "Not a git repo, exiting"
			sys.exit(-1)
						
	def get_frontpage_data(self):
		data = {}
		data['files'] = self.index_to_tree(self.repo.index.entries)
		return data

	def get_commits(self):
		data = []
		for commit in self.repo.iter_commits():
			retval = {}
			retval["author"] = "%s <%s>" % (commit.author.name, commit.author.email)
			retval["date"] = datetime.datetime.fromtimestamp(commit.committed_date)
			retval["message"] = commit.summary
			retval["id"] = commit.hexsha
			data.append(retval)
		return data
		
	def commit_exists(self,commit_id):
		try:
			self.repo.commit(commit_id)
		except BadObject:
			return False
		return True
	
	def get_data_from_commit(self,commit_id):
		return self.repo.commit(commit_id).stats.files
	
	def index_to_tree(self,filelist):
		file_tree = {}
		for file in filelist:
		
			#split into directory levels
			parts = file[0].split('/')
			
			current_level = file_tree
			
			#check each level to see where present
			while parts:
			
				level = parts.pop(0)
				
				if level in current_level:
					current_level = current_level[level]
				else:
					parts.reverse()
					new_layer = {}
					
					for i in parts:
						new_layer = { i : new_layer }
					
					current_level[level] = new_layer
					
					break
		return file_tree