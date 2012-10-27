from shovel import task
from subprocess import call

import os

@task
def pull():
	'''
	Pull the source and git repositories to keep them up to date

	Seriously, it's an issue sometimes...
	'''
	
	os.chdir("source")
	call(["git", "pull"])
	os.chdir("../git")
	call(["git", "pull"])
