"""
Automaton routines for controlling Google Chrome.
"""

import json, time
import urllib2
import subprocess
from websocket import create_connection

class MethodBuilder:
    def __init__(self, comm, name):
        self.comm = comm
        self.name = name
    def __getattr__(self, attr):
        return MethodBuilder(self.comm, self.name + '.' + attr)
    def __call__(self, **kwargs):
        return self.comm.send(self.name, **kwargs)

class Intercom:
    def __init__(self, ws_url, id=1):
        self.id = id
        self.conn = create_connection(ws_url, timeout=1)
    def setup(self):
        self.Page.enable()
        self.wait()
    def visit(self, url):
        self.Page.navigate(url=url)
        self.wait()
    def send(self, method, **kwargs):
        props = dict(id=self.id, method=method)
        if len(kwargs) > 0:
            props.update(dict(params=kwargs))
        self.conn.send(json.dumps(props))
    def recv(self):
        try:
            return json.loads(self.conn.recv())
        except:
            return None
    def wait(self):
        for msg in self:
            pass
    def html(self):
        self.wait()
        self.DOM.getDocument()
        doc = self.recv()
        self.DOM.getOuterHTML(nodeId=doc['result']['root']['nodeId'])
        node = self.recv()
        return node['result']['outerHTML']
    def __getattr__(self, attr):
        return MethodBuilder(self, attr)
    def __iter__(self):
        while True:
            msg = self.recv()
            if msg is None: break
            yield msg

def start_chrome():
    chrome = subprocess.Popen(
        ['C:/Users/Grant/AppData/Local/Google/Chrome/Application/chrome.exe',
         '--user-data-dir=c:/tmp/automaton', '--remote-debugging-port=9222'])

def connect():
    start_chrome()
    data = urllib2.urlopen('http://localhost:9222/json').read()
    ws_url = json.loads(data)[0]['webSocketDebuggerUrl']
    comm = Intercom(ws_url)
    return comm
