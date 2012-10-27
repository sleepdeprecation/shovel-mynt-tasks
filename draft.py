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
    '''

    import os, re

    dirn = "source/_drafts/"
    if not os.path.exists(dirn):
        os.makedirs(dirn)

    filename = dirn + re.sub(r'\W+', '-', title.lower()) + ".md"

    filecont =  "---\ntitle: \"" + title + "\""
    filecont += "\nlayout: post.html"
    filecont += "\nsinglecol: false"
    filecont += "\ntags: ['']\n---\n\n"

    writer = open(filename, "w")
    writer.write(filecont)


