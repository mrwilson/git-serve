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
		print self.repo.bare

