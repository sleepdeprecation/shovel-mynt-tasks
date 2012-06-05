from shovel import task
from subprocess import call
#from lessc import compile

import os, glob, shutil

@task
def update():
	'''
		Update the site, including pushing a git repo to wherever...

		Will call lessc on `./source/_assets/css/style.less`, and turn it
		into standard css.
	'''

	# compile less
	#compile("style.less", path="./source/_assets/css")

	# add source git...
	os.chdir("source")
	call(["git", "add", "."])
	call(["git", "commit", "-m", "'update script'"])
	call(["git", "push"])

	# add gen git
	os.chdir("../generated")
	recCopy()

	os.chdir("../git")
	call(["git", "add", "."])
	call(["git", "commit", "-m", "'update script'"])
	call(["git", "push"])

def recCopy(path='./'):
	for i in glob.iglob(path + "*.*"):
		shutil.copy(i, 'git/' + path)

	for i in glob.iglob(path + "/*/"):
		recCopy(path)

