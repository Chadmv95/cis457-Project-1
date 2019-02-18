from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/Users/chadvredeveld/Documents/cis457/ftp-folder", perm="elradfmw")
authorizer.add_anonymous("/Users/chadvredeveld/Documents/cis457/ftp-folder", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

try:
    server = FTPServer(("127.0.0.1", 8021), handler)
    server.serve_forever()
except ftplib.all_errors:
    print("Error: ftp error \n")