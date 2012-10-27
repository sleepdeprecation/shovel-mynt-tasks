from shovel import task
from subprocess import call
#from lessc import compile

import os, glob, subprocess

@task
def update(message="update script"):
	'''
		Update the site, including pushing a git repo to wherever...
		
		Yeah, that's right, just update stuffs and whatever...

		If you include a message using 
		`shovel update "message"`, that'll be the commit message.
		If you don't include a message, it'll just be "update script"
	'''

	# pull, to make sure that everything is hunky-dory
	call(["shovel", "pull"])

	# add source git...
	os.chdir("source")
	call(["git", "add", "."])
	call(["git", "commit", "-m", message])
	call(["git", "push"])

	# generate
	os.chdir("../")
	call(["mynt", "gen", "-f", "source", "generated"])

	# add gen git
	cp = subprocess.Popen("cp generated/* git/ -r", shell=True)
	result, err = cp.communicate()
	print "copying error" if err else "copying fine"

	os.chdir("git")
	call(["git", "add", "."])
	call(["git", "commit", "-m", message])
	call(["git", "push"])

