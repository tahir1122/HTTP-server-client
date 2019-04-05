# Tahir Mahmood
# 801028975

# Used guidance from online tutorials. This was programmed in Ubuntu 18 using Python2.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  
import os
import sys  

class HandleRequests(BaseHTTPRequestHandler):  

  def do_GET(self):  
    rootdir = '.'
    try:  
      if self.path.endswith('.html'):  
        f = open(rootdir + '/' + self.path) 
  
        self.send_response(200)  
  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
   
        self.wfile.write(f.read())  
        f.close()  
        return  

    except IOError:  
      self.send_error(404, 'Not Found')

  def do_POST(self):       
    request_path = self.path
    
    print("\n----- Request Start ----->\n")
    print(request_path)
    
    request_headers = self.headers
    content_length = request_headers.getheaders('content-length')
    length = int(content_length[0]) if content_length else 0
    
    print(request_headers)
    print(self.rfile.read(length))
    print("<----- Request End -----\n")
    
    self.send_response(200)

  def do_PUT(self):
      self.do_POST()

def run():  
  print('http server is starting...')  
  
  address = sys.argv[1]
  port = int(sys.argv[2])
  server_address = (address, port)

  httpd = HTTPServer(server_address, HandleRequests)  
  print('Http Server is Running ...')  
  httpd.serve_forever()  

if __name__ == '__main__':  
  run()  