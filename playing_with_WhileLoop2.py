
user_command = ""

while True: 
    user_command = input("Enter a command !").lower()
    if user_command == "Start":
        print("Car Starting")
    elif user_command =="Stop":
        print("Car Stopped")
    elif user_command =="Help":
        print("""
Start - for starting a car
Stop  - for stopping the car
Quit  - for exiting the program
        """)
    elif user_command == "Quit":    
        break
    else:
        print("Sorry add one of the command")

     