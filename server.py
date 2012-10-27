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
    httpd = SocketServer.TCPServer(("", 8000), handler)
    httpd.serve_forever()

class MyntWatcher (threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    call(["mynt", "watch", "-f", "--base-url=127.0.0.1:8000", "source", "generated"])

@task
def server():
  '''
    Run a simple server on port 8000, watching the scss and source
  '''

  SASScompile().start()
  MyntWatcher().start()
  PythonServer().start()