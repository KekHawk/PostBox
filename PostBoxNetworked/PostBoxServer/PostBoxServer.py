import http.server
import socketserver

from datetime import datetime

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        if "?input=" in self.path:
            with open("PostBox.txt","a+") as f:
                f.write(str("[" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "]  " + self.path[self.path.index("?input=") + len("?input="):].replace("_", " ") + "\n"))


PORT = 8000

httpd = socketserver.TCPServer(("", PORT), ServerHandler)

print("Serving at port", PORT)
httpd.serve_forever()
