# mynt shovel tasks

This is a collection of mynt shovel tasks used modify and update [http://dkuntz2.com](http://dkuntz2.com). Some of which are based off of another one of my projects, [By The Bay](https://github.com/dkuntz2/bythebay).

## Requrements

- [Shovel](https://github.com/seomoz/shovel)
- [mynt](https://github.com/Anomareh/mynt)
- [lesscss-python](https://github.com/metalshark/lesscss-python)

## Installation

Really, it's quite simple. 

Pretty much follow the following guide, it'll get you the basis of a mynt project located at `~/mynt`

	mkdir mynt
	cd mynt
	git clone git://github.com/dkuntz2/mynt-tasks.git shovel
	shovel create
	shovel new "Hello World!"
	shovel generate

The output of `ls -p ~/mynt` should be:

	generated/  shovel/  source/

Huzzah! You've got most of a mynt project ready to go...

## Usage and list of tasks

If you're not sure what a shovel task does, you can run `shovel help [task name]` for a specific task, or `shovel help` for all tasks.

### create

Build your basic mynt site. Runs `init` for your too.

### init

Prompts you for the basic information about your site and places them inside your `./source/config.yml` file.

Does some *basic* processing on the domain and base_url variables.

### new "[name of post]"

Create a new post with the name [name of post].

Post will be located in `./source/_posts/[yyyy]/[mm]/[dd]/[yyyy]-[mm]-[dd]-[hh]-[min]-[name of post, replacing all special characters with _].md`

### generate

Generates your mynt site using `./source` as the source and `./generated` as the output.