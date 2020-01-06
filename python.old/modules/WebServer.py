import http.server
import socketserver


class WebServer:
    def startWebServer(self):
        PORT = 8080
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()
