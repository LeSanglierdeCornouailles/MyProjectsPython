
user_command = ""

while user_command != "quit": 
    user_command = input("Enter a command ! : ").lower()
    if user_command == "start":
        print("Car Starting")
    elif user_command == "stop":
        print("Car Stopped")
    elif user_command == "help":
        print("""
Start - for starting a car
Stop  - for stopping the car
Quit  - for exiting the program
        """)
    elif user_command == "quit":    
        break
    else:
        print("Sorry add one of the command")

     