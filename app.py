from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server = ThreadingHTTPServer(('0.0.0.0', port), Handler)
    print(f'Serving on http://0.0.0.0:{port}')
    server.serve_forever()
