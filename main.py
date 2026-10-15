from http.server import BaseHTTPRequestHandler as GhostHandler , HTTPServer
from urllib.parse import urlparse , parse_qs 
class H(GhostHandler):
    def do_POST(self):
        POST_ok = False
        non_ok = False
        home_ok = False
        shab_ok = False
        ip_counts = {}
        sap = self.client_address[0]
        print (sap)
        print (self.path)
        response_stu = 200
        messae = ""
        log_analyzer = f"{self.command} {self.path} | ip: {sap}"
        print (log_analyzer)
        with open ("ghost.log","a") as file:
         file.write(log_analyzer + "\n")
        if ip in ip_counts:
         ip_counts[ip] += 1
        else:
         ip_counts[ip] = 1
        with open("ghost.log" , "r") as file:
         for line in file:
          print (line)
         for ip , count in ip_counts.items():
          print (ip , count)
        if self.command == "POST":
         POST_ok = True
         if self.path == "/submit":
          nonn_ok = True 
         else:
          nonn_ok = False
          response_stu = 400
          messea = "path bad" 
          if self.path == "/ghost":
           shab_ok = False
           response_stu = 405
           messae = "Method Not Allowed"
          else: 
           shab_ok = False
           response_stu = 405
           messae = "Method Not Allowed"
           if self.path == "/unknown":
            home_ok = False
            response_stu = 404
            messae = "not found"
           else:
            home_ok = False
            response_stu = 404
            messae = "not found"
        else:
         POST_ok = False
         response_stu = 405
         messae = "Method Not Allowed"
        if POST_ok and home_ok and shab_ok and nonn_ok:
         self.send_response(response_stu)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write("request accept".encode())
         print ("request accept")
        else:
         self.send_response(response_stu)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write(messae.encode())
    def do_GET (self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        method_ok = False
        path_ok = False
        id_ok = False
        auth_ok = False
        params_ok = False
        ip_counts = {}
        print (self.path)
        response_status = 200
        message = ""
        ip = self.client_address[0]
        print (ip)
        log_analyzer = f"{self.command} {self.path} | ip: {ip}"
        print (log_analyzer)
        with open("ghost.log" , "a") as file:
         file.write(log_analyzer + "\n")
        if ip in ip_counts:
         ip_counts[ip] += 1
        else:
         ip_counts[ip] = 1
        with open("ghost.log" ,"r") as file:
         for line in file:
          print (line)
        for ip , count in ip_counts.items():
         print (ip , count)
        if "id" in params:
         base = params.get("id" , [""])[0]
         lase = params.get("role" , [""])[0]
         if base == "5":
          auth_ok = True
         else:
          response_status = 401
          message = " user id Incorrect"
          auth_ok = False
         if lase == "user":
          auth_ok = True
         else:
          response_statue = 401
          message = "auth Incorrect"
          auth_ok = False
         if self.command == "GET":
          print ("method ok")
          method_ok = True
         else:
          response_status = 405
          message = "method Incorrect"
          method_ok = False
         if parsed.path == "/ghost":
          print ("path ok")
          path_ok = True
         else:
          response_status = 404
          message = "path Incorrect"
          path_ok = False
         if lase:
          params_ok = True
         else:
          params_ok = False
          response_status = 400
          message = "Request without role"
         if base:
          params_ok = True 
         else:
          params_ok = False
          response_status = 400
          message = "Request without id"
        else: 
         id_ok = False
         response_status = 400
         message = "id not found"
        print ("id :" , params.get("id" , [""])[0])
        print ("role :" , params.get("role", [""])[0])
        if path_ok and method_ok and auth_ok:
         self.send_response (response_status)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write("request accept".encode())
         print ("request accept")
        else:
         self.send_response (response_status)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write(message.encode())
         print ("request wrong")
server = HTTPServer(("127.0.0.1",8082),H)
server.serve_forever()
