#THIS ONE IS NO GOOD, DONT USE THIS ONE OMEGALUL
def func1():
    return 0

def func2():
    return 0

if __name__ == "__main__":
    print("==========FTP Command line utility==========")

    usr_command = input("Enter a command\n(CONNECT, LIST, RETRIEVE, STORE, QUIT): ")
    print(usr_command)

    while(usr_command != 'quit'):
        usr_command = input("\nEnter a command: ")
        print(usr_command)
