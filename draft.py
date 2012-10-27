from shovel import task

@task
def draft(title):
    '''
    Create a new draft.

    Call: `shovel new "title of draft"`
    New file: ./source/_drafts/[title-of-draft].md
    With the contents:

        ---
        title: "title of draft"
        layout: post.html
        tags: ['']
        ---

    The difference between draft and new is that new creates an
    immediately visible blog post, where draft creates a draft,
    inside of the _drafts directory, which isn't payed attention
    to while mynt generates the site.

    If you're finished with a draft, you'll need to call
    `publish "title of draft"`, which will make the draft an
    actual post, and will move it to the
    `./source/_posts/[yyyy]/[mm]/[dd]/` directory, and give it
    a timestamp before the name, which is what you want (and is
    similar to what calling new does).
    '''

    import os, re

    dirn = "source/_drafts/"
    if not os.path.exists(dirn):
        os.makedirs(dirn)

    filename = dirn + re.sub(r'\W+', '-', title.lower()) + ".md"

    filecont =  "---\ntitle: \"" + title + "\""
    filecont += "\nlayout: post.html"
    filecont += "\ntags: ['']\n---\n\n"

    writer = open(filename, "w")
    writer.write(filecont)


