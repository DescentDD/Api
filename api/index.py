from http.server import BaseHTTPRequestHandler
import os
import re
import random

def find_png_files(directory):
    file_list = os.listdir(directory)
    png_files = [file_name for file_name in file_list if re.search(r'\.(png|jpg)$', file_name)]
    return png_files
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        imgs=find_png_files('img')
        img = random.choice(imgs)
        self.send_response(200)
        content_type = 'image/png' if img.lower().endswith('.png') else 'image/jpeg'
        self.send_header('Content-type', content_type)
        self.end_headers()
        file_path = os.path.join(os.getcwd(), 'img', img)
        with open(file_path, 'rb') as file:
            content = file.read()
            #print(content)
            print(type(content))
            self.wfile.write(content)
        return
    
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), handler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()