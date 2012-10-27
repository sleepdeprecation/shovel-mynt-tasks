# mynt shovel tasks

**IMPORTANT**: Most of the information hasn't been updated in a
while, and probably won't be. The most accurate information can
be found in the task files themselves, or by calling `shovel help`
or `shovel help [task]` for specific information.

Also, some of these tasks may no longer exist. Don't rely on this
for documenation...

This is a collection of mynt shovel tasks used modify and update
[http://dkuntz2.com](http://dkuntz2.com).

## Requrements

- [Shovel](https://github.com/seomoz/shovel)
- [mynt](https://github.com/Anomareh/mynt)
- SASS, installed by gem (or something called `sass` in your path that 
  has the same switches and such as the sass gem)


## Installation

Really, it's quite simple. 

Pretty much follow the following guide, it'll get you the basis of a 
mynt project located at `~/mynt`

	mkdir mynt
	cd mynt
	git clone git://github.com/dkuntz2/mynt-tasks.git shovel
	shovel create
	shovel new "Hello World!"
	shovel generate

The output of `ls -p ~/mynt` should be:

	generated/  shovel/  source/

Huzzah! You've got most of a mynt project ready to go...

## Git integration

Because I've been writing these for myself, and I like to keep my site
updated with git (it's so much nicer than using FTP, you have no idea if
you haven't done so before, really, just try it out), there is some built
in git functionality.

That said, you have to manually mess with the directories to get started
with the git tasks.

Basically, just head into `./source`, run `git init`, add a remote (`git
remote add [url to remote repository] origin`.

After you've got the source directory setup you'll need to create the git
directory (as of when this is written, mynt deletes the genereated
directory on each call of `mynt gen`, which means you'll need a third
directory). It's pretty much `mkidr git`, followed by running the same
commands for the source setup.

When that's done, you can start using the git tasks.

## Usage and list of normal tasks

If you're not sure what a shovel task does, you can run `shovel help [task name]` for a specific task, or `shovel help` for all tasks.

### create

Build your basic mynt site. Runs `init` for your too.

### init

Prompts you for the basic information about your site and places them inside your `./source/config.yml` file.

Does some *basic* processing on the `domain` and `base_url` variables.

### draft "[name of post]"

Create a new draft with the name [name of post].

The draft will be located in `./source/_draft/[name of post].md`. You can
freely edit and adjust your draft as you will...

### publish "[name of post]"

Moves the draft you have named `[name of post]` (located in the `_drafts`
directory, and having all of the non-alphanumeric characters replaced with
underscores for the name (it turns
`Something~something-something.something` into
`something-something-something-something`, but it knows that the file has a
different name, it's moderatly smart)) to the current date/time location,
as if you used the `new` command with "[name of post]" instead, but it
already has content.

### new "[name of post]"

Create a new post with the name [name of post].

Post will be located in `./source/_posts/[yyyy]/[mm]/[dd]/[yyyy]-[mm]-[dd]-[hh]-[min]-[name of post, replacing all special characters with _].md`

### generate

Generates your mynt site using `./source` as the source and `./generated` as the output.i

## Git tasks

### pull

Update the `source` and `git` git repositories from the server (just runs
`git pull` on the two directories)

### update

Runs generate, copies the stuff in `generated/` to `git/` and pushes
`source/` and `git/` to their remote repos.
