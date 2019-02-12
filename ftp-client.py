# CIS457 Project 1
# Description: ftp-client will connect to an ftp server. Valid commands are exit, retrieve, store, and list

#!/usr/bin/python3
import ftplib


# Function to get FTP connection information from user
# return IP of server and port number
def welcome():
    print("Welcome to FTP client app\n")
    serverName=input("Please enter the server name:\n")
    portNumber=input("please enter the port number:\n")
    return serverName, portNumber


# Create client connection to server
# Param - IP and port of server
# return ftp connection
# To Do: Add try/catch for connection
def create_client(ip, port):
    ftp = ftplib.FTP('')
    ftp.connect(ip, int(port))
    ftp.login()
    return ftp


# List directories on server
# param - ftp connection
def list_files(ftp):
    print("List files in directory: ")
    print(ftp.retrlines('List'))


# Retrieve a file from the server
# param - ftp connection
def retrieve(ftp):
    directory= input("Enter directory to retrieve file from\n")
    filename= input("Enter filename of file to retrieve\n")
    ftp.cwd(directory)
    # create file to store retrieved data in
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR '+filename, localfile.write, 1024)
    localfile.close()


# Store file in server
# param - ftp connection
def store(ftp):
    filename=input("Enter filename to store \n")
    ftp.storbinary('STOR '+filename, 'rb')


# End client connection to server
# param - ftp connection
def quit_connection(ftp):
    print("quit")
    ftp.quit()


def main():
    server_name, port_number=welcome()
    ftp_connection = create_client(server_name, port_number)
    command = None
    while command != "quit":
        command = input("Enter Command: LIST, RETRIEVE, STORE, QUIT")
        if command.lower() == "list":
            list_files(ftp_connection)
        elif command.lower() == "retrieve":
            retrieve(ftp_connection)
        elif command.lower() == "store":
            store(ftp_connection)
        elif command.lower() == "quit":
            quit_connection(ftp_connection)
            command = "quit"
        else:
            print("Invalid command, please try again\n\n")


if __name__ == "__main__":
    main()

