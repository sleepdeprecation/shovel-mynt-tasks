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
      "source/_assets/css/style.scss:source/_assets/css/style.css"
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
    call(["mynt", "watch", "-f", "--base-url=http://127.0.0.1:8000/", "source/", "generated"])
    #print "mynt watch -f --base-url=http://12"

@task
def server():
  '''
    Run a simple server on port 8000, watching the scss and source
  '''

  '''
  SASScompile().start()
  MyntWatcher().start()
  PythonServer().start()
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

  while len(threads) > 0:
    try:
      threads = [t.join(1) for t in threads if t is not None and t.isAlive()]
    except KeyboardInterrupt:
      print "Ctrl-c received! killing threads..."
      for t in threads:
        t.kill_received = True
      serv.shutdown()
