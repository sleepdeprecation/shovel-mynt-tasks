from shovel import task
from subprocess import call

@task
def generate(source="source", dest="generated"):
	'''
		Create a generated version/update your mynt site.

		Call: `shovel generate "source" "dest"
		# => Generate a mynt site to `./dest`
			   using `./source` as the source

		Call: `shovel generate "source"`
		# => Generate a mynt site to `./generated`
			   using `./source` as the source

		Call: `shovel generate --dest "destination"
		# => Generate a mynt site to `./destination"
			   using `./source` as the source

		Call: `shovel generate`
		# => Generate a mynt site to `./generated`
			   using `./source` as the source
	'''

	call(["mynt", "gen", source, dest, "-f"])