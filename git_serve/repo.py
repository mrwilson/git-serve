from git import Repo
from git.exc import InvalidGitRepositoryError
import os, sys

class GitServeRepo(object):
	
	def __init__(self):
		try:
			self.repo = Repo(os.getcwd())
		except InvalidGitRepositoryError:
			print "Not a git repo, exiting"
			sys.exit(-1)

	def get_frontpage_data(self):
		data = {}
		files = []
		for k, v in self.repo.index.entries:
			files.append(k)
		
		data['files'] = files
		data['name'] =  self.repo.index.path
		return data

		

