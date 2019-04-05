
  
import httplib  
import sys  
  
http_server = sys.argv[1]
port_number = int(sys.argv[2])
command = sys.argv[3]
filname = sys.argv[4]
conn = httplib.HTTPConnection(http_server, port_number)

if command == 'GET':
  conn.request(command, filname)  

  rsp = conn.getresponse()  

  print(rsp.status, rsp.reason)  
  data_received = rsp.read()  
  print(data_received)  

  conn.close()
elif command == 'PUT':
  f = open('./' + filname)
  contents = f.read()
  conn.request(command, contents)

  rsp = conn.getresponse()  

  print(rsp.status, rsp.reason)  
  data_received = rsp.read()  
  print(data_received)  

  conn.close()