car_state = "stop"

while True:
    command = input("Enter a command (start, stop, exit): ").lower()

    if command == "start":
        if car_state == "start":
            print("Car is already in start state.")
        else:
            print("Ready to race!")
            car_state = "start"
    elif command == "stop":
        if car_state == "stop":
            print("Car is already in stop state.")
        else:
            print("Car stopped.")
            car_state = "stop"
    elif command == "exit":
        confirm_exit = input("Are you sure you want to exit? (yes/no): ").lower()
        if confirm_exit == "yes":
            print("Exited")
            break
        else:
            print("Resuming.")
    else:
        print("Invalid command.")
