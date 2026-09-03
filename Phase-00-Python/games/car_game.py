Started = False
# Stopped = False
# command = ''
print("Welcome to the car Please Enter the command to start or stop")
while True:
    command = input("-> ").lower()
    if command == "start":
        if Started:
            print("Sorry you already started the car")
        else:
            Started = True
            print('Welcome your car is strat now')
    elif command == "stop":
        if not Started:
            print("Sorry you already stopped the car")
        else:
            Started = False
            print ('Your car has stopped')
    elif command == "quit" or command == "exit":
        break
    elif command == "help" or command == "--help" or command == "--h":
        print("""
start - To start the car
stop - To stop the car
quit/exit - To exit the car
        """)
    else:
        print("""
Sorry I don't understand 
that command 
please take a help 
enter 
--help
--h
""")
print("Thanks You Please Share Your Experience With Us.!")