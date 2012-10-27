from shovel import task
from subprocess import call

@task
def create(dirn="source"):
	'''
		Create a new mynt site at the specified directory.

		Moves config.yml to config.mynt.yml. Calls `shovel init` afterwards
		
		Call: `shovel create "name of directory"
		# => create new By The Bay mynt site at "name of directory"

		Call: `shovel create`
		# => create new By The Bay mynt site at "source"
	'''

	call(["mynt", "init", "-f", dirn])	
	call(["mv", dirn + "/config.yml", dirn + "/config.mynt.yml"])
	call(["shovel", "init", "\"" + dirn + "\""])
