from http.server import BaseHTTPRequestHandler as GhostHandler , HTTPServer
class N(GhostHandler):
    def do_GET(self):
        ip_counts = {}
        with open("ghost.log" , "r") as file:
         for line in file:
          ghost_line = line.split("|")[1]
          ip = ghost_line.split(":")[1].strip()
          if ip in ip_counts:
           ip_counts[ip] += 1
          else:
           ip_counts[ip] = 1 
         for ip,count in ip_counts.items():
          print (f"{ip} {count} request")
    def do_POST(self):
        ip_counts = {}
        with open("ghost.log" , "r") as file:
         for line in file:
          ghost_line = line.split("|")[1]
          ip = ghost_line.split(":")[1].strip()
          if ip in ip_counts:
           ip_counts[ip] += 1
          else:
           ip_counts[ip] = 1
         for ip,count in ip_counts.items():
          print (f"{ip} {count} request")
server = HTTPServer(("127.0.0.1",8083),N)
server.serve_forever()
