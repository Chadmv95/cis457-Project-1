from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/Users/JD/Desktop/CIS457/ftp", perm="elradfmw")
authorizer.add_anonymous("/Users/JD/Desktop/CIS457/ftp", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer


server = FTPServer(("127.0.0.1", 8021), handler)
server.serve_forever()
