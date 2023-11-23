to_do = []
# print("Enter \033[1madd \033[0mto add a task to the to-do list.")
# print("Enter \033[1mcomplete \033[0mto mark a task as complete.")
# print("Enter \033[1mview all \033[0mto view the current tasks in the to-do list.")
# print("Enter \033[1mview complete \033[0mto view the completed task in the to do list.")
# print("Enter \033[1mview incomplete \033[0m to view all the incomplete task in the to do list.")
# print("Enter \033[1mhelp \033[0mto display all the help messages.")
# print("Enter \033[1mexit \033[0mto exit the program.")


while True:
    
    command = input("Enter a command as mentioned above: ").lower()
    if command == 'add':
        task = input("Enter task: ")
        if task  not in [a['descreption'] for a in to_do]:
            to_do.append({'descreption': task, 'status':'Incomplete'})
            print(f"Task {task} added")
            
        else:
            print("Task already exist.")
            
            
    elif command == 'complete':
        for i, task in enumerate(to_do, start=1):
            print(f"{i}. {task['descreption']} - {task['status']}")

        q = int(input("Enter the task which is completed: "))
        if 1 <= q <= len(to_do):
            to_do[q - 1]['status'] = "Completed"
            print(f"Task {to_do[q - 1]['descreption']} marked as complete.") 
        else:
            print("Task not found.")
    elif command == 'view all':
        
        for i, task in enumerate(to_do, start=1):
            print(f"{i}. {task['descreption']} - {task['status']}")

    elif command == 'view complete':
        complete = [a for a in to_do if a['status'] == 'Completed']
        for i,a in enumerate(complete, start=1):
            print(f"{i}. {a['descreption']} - {a['status']}")
            
    elif command == 'view incomplete':
        complete = [a for a in to_do if a['status'] == 'Incomplete']
        for i,a in enumerate(complete, start=1):
            print(f"{i}. {a['descreption']} - {a['status']}")
    elif command == "help":
        print("Enter \033[1madd \033[0mto add a task to the to-do list.")
        print("Enter \033[1mcomplete \033[0mto mark a task as complete.")
        print("Enter \033[1mview all \033[0mto view the current tasks in the to-do list.")
        print("Enter \033[1mview complete \033[0mto view the completed task in the to do list.")
        print("Enter \033[1mview incomplete \033[0m to view all the incomplete task in the to do list.")
        print("Enter \033[1mhelp \033[0mto display all the help messages.")
        print("Enter \033[1mexit \033[0mto exit the program.")
        
    elif command == 'exit':
        print("Sure you want to exit this!")
        break
    else:
        print("The command you have entered is invalid. You can goto help.")
        
            

