from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        #Se o caminho for esse, o diretorio main
        #Então passe a config de resposta
        #Mostra o conteudo
        #E finaliza os headers
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            #self.send_header("testando", "abc")
            self.end_headers()
            data = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>HTTP PYTHON</title>
                </head>
            <body>
            <button>Menu Principal</button>
            <p>Dir: {self.path}</p>
            </body>
            </html>
            """.encode()
            self.wfile.write(data)

        #Caso contrario outro conteudo noutro caminho
        elif self.path == '/eventos':
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            #self.send_header("testando", "abc")
            self.end_headers()
            data = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>HTTP PYTHON</title>
                </head>
            <body>
            <button>Eventos</button>
            <p>Dir: {self.path}</p>
            </body>
            </html>
            """.encode()
            self.wfile.write(data)


server = HTTPServer(('localhost', 8080), SimpleHandler)
server.serve_forever()