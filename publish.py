from shovel import task

@task
def publish(title):
    '''
    Publish a draft.

    Call: `shovel publish "title of draft"`

    Looks to see if `./source/_drafts/[title-of-draft].md` is a file,
    and if it is, it will move it to the ready-to-publish location of
    `./source/_posts/[yyyy]/[mm]/[dd]/[yyyy]-[mm]-[dd]-[hh]-[mm]-[title-of-draft].md`
    because that's where it's supposed to go.

    Pretty much, it just makes a draft ready to print. It can't tell you
    if the draft is fit to print, that's something you have to determine
    on your own.
    '''

    import datetime, os, re, shutil
    from subprocess import call

    draft = "source/_drafts/" + re.sub(r'\W+', '-', title.lower()) + ".md"

    if os.path.isfile(draft):
        now = datetime.datetime.now()
        pubd =  "source/_posts/" + now.strftime("%Y/%m/%d/")

        if not os.path.exists(pubd):
            os.makedirs(pubd)

        pub = pubd + now.strftime("%Y-%m-%d-%H-%M-")
        pub += re.sub(r'\W+', '-', title.lower()) + ".md"

        print(pubd + " : " + pub)

        shutil.move(draft, pub)
        os.chdir("source")
        call(["git", "mv", draft, pub])

        #if shutil.move(draft, pub): print("moved") else: print("issue moving")
    else:
        print(str(title) + " could not be found. Looking for\n" + str(draft))
