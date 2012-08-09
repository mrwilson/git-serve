from git import Repo
from git.exc import InvalidGitRepositoryError
import os, sys

class GitServeRepo(object):
	
	def __init__(self,path=os.getcwd()):
		self.setup(path)
	
	def setup(self, path):
		try:
			self.repo = Repo(path)
		except InvalidGitRepositoryError:
			print "Not a git repo, exiting"
			sys.exit(-1)

	def get_frontpage_data(self):
		data = {}
		data['files'] = self.index_to_tree(self.repo.index.entries)
		data['name'] =  self.repo.index.path
		return data

	def index_to_tree(self,filelist):
		file_tree = {}
		for k in filelist:
		
			#split into directory levels
			parts = k[0].split('/')
			
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