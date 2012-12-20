from shovel import task
from subprocess import call

import os, threading, SimpleHTTPServer, SocketServer

class SASScompile (threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    call([
      "sass", 
      "--watch", 
      "source/_assets/_scss:source/_assets/css"
    ])

class PythonServer (threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    os.chdir("generated")
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    self.httpd = SocketServer.TCPServer(("", 8000), handler)
    self.httpd.serve_forever()

  def shutdown(self):
    self.httpd.shutdown()

class MyntWatcher (threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    call(["mynt", "gen", "--base-url=http://127.0.0.1:8000/", "-f", "source", "generated"])
    
    # okay, now watch it...
    call(["mynt", "-v", "watch", "--base-url=http://127.0.0.1:8000/", "-f", "source", "generated"])
    


@task
def server():
  '''
    Run a simple server on port 8000, watching the scss and source

    Yes, it's that simple.

    This is mostly for local development purposes. If you use the same
    setup that I use (and, considering that I've written these mostly
    for myself, because it makes life easier for me, but I thought that
    others might like them too), it watches and compiles the scss file,
    watches the source, and serves up the generated files, using the
    base_url of `http://127.0.0.1:8000/` (which is where it's served to).

    It suddenly turns three terminal windows into one.

    Also, all messages are output provided you don't bring it to
    the background.

    Ctrl-c does work. It took some time to get that working, but the
    SimpleHTTPServer now shutsdown, which is good.
  '''

  threads = []

  sass = SASScompile()
  threads.append(sass)
  sass.start()

  myntwatch = MyntWatcher()
  threads.append(myntwatch)
  myntwatch.start()

  serv = PythonServer()
  threads.append(serv)
  serv.start();

  try:
    while True:
      pass

  except KeyboardInterrupt, SystemExit:
    print "\nCtrl-c received! killing threads..."
    serv.shutdown()
    print "server killed"
    for t in threads:
      #t.interrupt_main()
      t.kill_received = True