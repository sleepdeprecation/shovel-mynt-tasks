# mynt shovel tasks

This is a collection of [shovel](https://github.com/seomoz/shovel) tasks for
working with a [mynt](https://github.com/Anomareh/mynt) website (provided
your local setup is similar to mine).

**Contents**

- [Background Information](#background-information)
- [What do these tasks do?](#what-do-these-tasks-do)
- [Workflow](#workflow)
- [Workflow Alterations](#alterations)
- [Local Development](#local-development)


## Background Information

My [website](http://dkuntz2.com) runs on mynt, because I really like it for a
variety of reasons. That said, because mynt is a static-site generator, there
isn't really anything to easily manage basic tasks built in (this is the same
for jekyll and most likely other static-site generators).

In jekyll's case, Brandon Mathis created Octopress, which, along with
providing users with an easy to implement theme and a collection of nice
plugins, gives them a set of rake tasks.

I created these tasks to make managing my site easier.


## What do these tasks do?

There are three basic things these tasks do

1.  Help you create new blog drafts and posts. Which is the most basic thing
    you want to be able to do with your website.

2.  Update your site, by generating the site and pushing git repositories 
    (again, these tasks presume you have a setup akin to mine, there are
    setup instructions below).

3.  Locally develop your site.


## Workflow

My typical workflow goes something like this:

1.  Create a new draft for a post, generally because I either have a full post
    that I want to write, or because I have an idea and I want to work on it.

    Creating a draft is fairly easy, just call

      shovel draft "Name of your draft"

    Doing that will create a new file in `./source/_drafts` with 
    "name-of-your-draft.md" as the filename (in lowercase, with all 
    non-alphanumeric characters converted into dashes).

2.  After finishing the draft, it's time to publish it, which can be done by
    calling

      shovel publish "Name of your draft"

    Where "Name of your draft" is the same thing you used when calling draft.

    This will move the file from your drafts directory to 
    `./source/_posts/[yyyy]/[mm]/[dd]/[yyyy]-[mm]-[dd]-[hh]-[mm]-[previous file name].md`, 
    which is what you want for it to become visible on the blog.

    Because `publish` uses the same system for converting the title string
    into a filename, you can use all lowercase characters, and convert all
    non-alphanumeric characters into other non-alphanumeric characters. It's
    suggested that you just use the same string as when you called draft.

3.  Now that the source files have been modified, and there's an update to be
    made to the site, the site can be updated by calling

      shovel update

    Or, if you want a commit message other than `update script`, 

    ```
      shovel update "commit message"
    ```

    This will update the git repository in the `./source` directory, generate
    the mynt site (by calling `mynt gen -f source generated`), copy everything
    in the `./generated` directory into the `./git` directory, and update the
    git repository in the `./git` directory.

    It will also call `git push` on the two git repositories.

### Alterations

If you have a new blog entry you want to immediately post, you can call

  shovel new "name of post"

Which will skip having the initial file in the `./source/_drafts` directory
and place it in the corresponding `./source/_posts` year-month-day directory,
with the timestamped filename.

## Local Development

If you want to locally develop your mynt site, you can call

  shovel server

The server task does three things:

1.  It watches the scss file
    `./source/_assets/css/style.scss` and compiles it into 
    `./source/_assets/css/style.css`

2.  It watches your `./source` directory for changes and automatically
    generates them into the `./generated` directory, setting `site.base_url`
    to `http://127.0.0.1:8000/` (which is what the next thing serves it to).

3.  It runs a `SimpleHTTPServer` in the `./generated` directory, serving
    it to localhost port 8000.

Calling `shovel server` provides you with a local instance of your site, and
serves it to a different `base_url` than the one set in your site's 
`config.yml` file (which means you don't have to change that).

After starting the server, you can open your browser to 
[`http://127.0.0.1:8000/`](http://127.0.0.1:8000). You can than make changes
to your source files and see what happens.

To kill the server, just kill the process.

If you want to see exactly what it does, you can check out `server.py`. Or, if
you don't use an scss file to control your styles, you can comment out line
65.
