while True:
    print("Please Enter the valid Command for help type 'Help' ")
    command = input("> ").lower()
    if command == "start":
        print('Welcome your car is strat now')
    elif command == "stop":
        print ('Your car has stopped')
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To exit the car
        """)
    else:
        print("Sorry I don't understand that command")