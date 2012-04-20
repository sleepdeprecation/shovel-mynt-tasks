from shovel import task

@task
def init(dirn="source"):
	'''
		Generate a config file for a By The Bay mynt install.

		Call `shovel init "directory"`
		# => generate config.yml for mynt site in "directory"

		Call `shovel init`
		# => generate config.yml for mynt site in "./source/"

		init will ask for the domain, base_url, author, email, title, subtitle,
		and description settings for the config.yml file.
	'''

	config = {}

	#
	# Get the domain name of the new site
	#
	print ("Domain name (for http://example.com/mynt/, put 'example.com') ")
	config["domain"] = raw_input()

	if config["domain"][0:8] == "https://":
		config["domain"] = config["domain"][8:]
	elif config["domain"][0:7] == "http://":
		config["domain"] = config["domain"][7:]

	if config["domain"][len(config["domain"]) - 1:] == "/":
		config["domain"] = config["domain"][:len(config["domain"]) - 1]

	#
	# Get the base url of the site
	#
	print ("\nBase URL (for http://example.com/mynt/, put '/mynt/') ")
	config["base"] = raw_input()

	if len(config["base"]) == 0 :
		config["base"] = "/"
	elif len(config["base"]) == 1 and config["base"] != "/":
		config["base"] = "/" + config["base"] + "/"
	else:
		if config["base"][0:1] != "/":
			config["base"] = "/" + config["base"]
		if config["base"][len(config["base"]) - 1:] != "/":
			config["base"] += "/"

	#
	# Get author's name
	#
	print ("\nSite's author's name (most likely your name) ")
	config["author"] = raw_input()

	#
	# get email
	#
	print ("\nSite's email account (most likely your own. Can be left blank...) ")
	config["email"] = raw_input()

	#
	# Get site's title
	#
	print ("\nSite's name (I like 'By The Bay' myself) ")
	config["title"] = raw_input()

	#
	# get subtitle
	#
	print ("\nSite's subtitle (maybe 'Where the watermelon grow' ?) ")
	config["subtitle"] = raw_input()

	#
	# Get description
	#
	print ("\nSite's description (I think 'a mynt-y fresh blog' works fairly well) ")
	config["description"] = raw_input()

	#
	# Now for the magic
	#

	import os

	oldconf = False
	if os.path.exists(dirn + '/config.yml'):
		import shutil

		oldconf = True
		shutil.copy(dirn + "/config.yml", dirn + "/config.yml.old")

	# start writing file
	filecont = '''#
# CONFIG FROM INPUT
#
# Received from what you typed...
'''

	filecont += "domain: " + config["domain"] + "\n"
	filecont += "base_url: " + config["base"] + "\n"
	filecont += "\n"
	filecont += "title: \"" + config["title"] + "\"\n"
	filecont += "subtitle: \"" + config["subtitle"] + "\"\n" 
	filecont += "description: \"" + config["description"] + "\"\n"
	filecont += "\n"
	filecont += "author: \"" + config["author"] + "\"\n"
	filecont += "email: \"" + config["email"] + "\"\n"
	filecont += "\n"
	filecont += "\n"
	filecont += '''
# 
# THIRD PARTY SETTINGS
#
# Basically anything that isn't mynt specific. There's some good stuffs too...

# If you'd like to enable Google Analytics, set this to your tracking code:
analytics: 

# Set this to true to enable an Atom feed.
#	Must also have `author`, `domain`, and `title` set to get a valid feed
feed: true

# Link to various social networking sites.
#	To enable, just put in your username or id.
social:
    dribbble: 
    facebook: 
    github:
    google_plus:
    lastfm:
    stack_overflow:
    steam:
    twitter:


#
# USEFUL THINGS
#
# You probably won't need to change any of these things, but they're here
# on the off chance...

archive_layout: archive.html
archives_url: /archives/
jinja:
    extensions:
        - jinja2.ext.loopcontrols
tag_layout: tag.html
tags_url: /tags/
'''
	writer = open(dirn + "/config.yml", "w")
	writer.write(filecont)

	print ("\n\nYour new config file has been written to `source/config.yml`!")
	if oldconf:
		print ("Your old config file has been moved to `source/config.yml.old`.")
