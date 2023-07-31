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
        imgs=find_png_files('api/img')
        img = random.choice(imgs)
        self.send_response(200)
        content_type = 'image/png' if img.lower().endswith('.png') else 'image/jpeg'
        self.send_header('Content-type', content_type)
        self.end_headers()
        with open('api/img/'+img, 'rb') as file:
            content = file.read()
            #print(content)
            print(type(content))
            self.wfile.write(content)
        return
    
