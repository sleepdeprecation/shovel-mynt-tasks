from shovel import task

@task
def new(title):
	'''
		Create a new post.

		Call: `shovel new "title of post"`
		New file: ./source/_posts/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[HH]-[MM]-title-of-post.md
		With the contents:

		---
		title: "title of post"
		layout: post.html
		singlecol: false
		tags: ['']
		---

		If you would prefer a different layout as the default, change the variable
		`layout` in ./shovel/new.py

		For additional options, checkout `./shovel/new.py`, there's some fun stuff
		in there...
	'''

	# This is the layout mentioned in the help:
	layout = "post.html"

	import datetime, os, re
	now = datetime.datetime.now()

	dirn = "source/_posts/" + now.strftime("%Y/%m/%d/")
	if not os.path.exists(dirn):
		os.makedirs(dirn)

	filename =  dirn + now.strftime("%Y-%m-%d-%H-%M-") 
	filename += re.sub(r'\W+', '-', title.lower()) + ".md"

	filecont =  "---\ntitle: \"" + title + "\""
	filecont += "\nlayout: " + layout
	filecont += "\nsinglecol: false"
	filecont += "\ntags: ['']\n---\n\n"

	writer = open(filename, "w")
	writer.write(filecont)

	#
	# ADVANCED: Open editor after calling
	#
	# If you'd like to have your favorite text editor open the newly created
	# post, comment out the next two lines and replace `subl` with the terminal
	# call for your editor.
	#
	#from subprocess import call
	#call(["subl"], filename)