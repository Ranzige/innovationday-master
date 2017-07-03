from threading import Thread
import time
import webbrowser
import SocketServer
import json
import os
from BaseHTTPServer import HTTPServer

port_number = 8000

server = None


def startServer(port):
    originDir = os.getcwd()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    Handler = HTTPServer.SimpleHTTPRequestHandler
    global server
    server = SocketServer.TCPServer(("", port), Handler)

    print("serving at port", port)
    server.serve_forever()
    os.chdir(originDir)


def start(port):
    thread = Thread(target=startServer, args=[port])
    thread.start()
    time.sleep(2)  # Wait to start the server first


def test():
    if not server:
        print("Failed to start server")

    url = "http://localhost:" + str(port_number) + '/' + 'index.html'
    url += "?number="
    url += "1"

    jsonObj = {
        "person": {
            "name": "Jack",
            "age": 20
        }
    }

    jsonStr = json.dumps(jsonObj)
    url += "&person="
    url += jsonStr
    webbrowser.open(url)
    print(url + " is opened in browser")


def stop():
    if server:
        server.shutdown()


if __name__ == "__main__":
    start(port_number)
    test()