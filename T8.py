to_do = []
bin_list = []
file_name = "todo.txt"

def save_list():
    with open(file_name, 'w') as f:
        for task in to_do:
            f.write(f"{task['description']} - {task['status']}\n")
            
def load_list():
    try:
        with open(file_name, 'r') as file:
            for line in file:
                description, status = line.strip().rsplit(' - ', 1)
                to_do.append({'description': description, 'status': status})
    except FileNotFoundError:
        open(file_name, 'w').close()
    

while True:
    
    command = input("Enter a command as mentioned above: ").lower()
    if command == 'add':
        task = input("Enter task: ")
        if task not in [a['description'] for a in to_do]:
            to_do.append({'description': task, 'status': 'Incomplete'})
            print(f"Task {task} added.")
            save_list()
        else:
            print("Task already exists.")
            
    elif command == 'complete':
        for i, task in enumerate(to_do, start=1):
            print(f"{i}. {task['description']} - {task['status']}")

        q = int(input("Enter the task which is completed: "))
        if 1 <= q <= len(to_do):
            to_do[q - 1]['status'] = "Completed"
            print(f"Task {to_do[q - 1]['description']} marked as complete.") 
        else:
            print("Task not found.")
            
    elif command == 'view all':
        load_list() 
        for i, task in enumerate(to_do, start=1):
            print(f"{i}. {task['description']} - {task['status']}")
            
    elif command == 'view complete':
        load_list() 
        complete = [a for a in to_do if a['status'] == 'Completed']
        for i, a in enumerate(complete, start=1):
            print(f"{i}. {a['description']} - {a['status']}")
            
    elif command == 'view incomplete':
        load_list()
        incomplete = [a for a in to_do if a['status'] == 'Incomplete']
        for i, a in enumerate(incomplete, start=1):
            print(f"{i}. {a['description']} - {a['status']}")
            
    elif command == 'delete':
            bin_list.extend(to_do)
            to_do.clear()
            print("To-do list deleted and moved to bin.")
            save_list()
    elif command == 'view bin':
        load_list()
        for i, task in enumerate(bin_list, start=1):
            print(f"{i}. {task['description']} - {task['status']} in bin")

            
    elif command == 'restore':
        load_list()
        if bin_list:
            for i, task in enumerate(bin_list, start=1):
                print(f"{i}. {task['description']} - {task['status']} in bin")

            q = int(input("Enter the task to restore: "))
            if 1 <= q <= len(bin_list):
                to_do.append(bin_list.pop(q - 1))
                print(f"Task {q} restored.")
                save_list()
            else:
                print("Task not found in bin.")
        else:
            print("Bin is empty. No tasks to restore.")
    elif command == 'clear bin':
        load_list()
        bin_list.clear()
        print("Bin cleared.")
        save_list()
        
    elif command == "help":
        print("Enter \033[1madd \033[0mto add a task to the to-do list.")
        print("Enter \033[1mcomplete \033[0mto mark a task as complete.")
        print("Enter \033[1mview all \033[0mto view the current tasks in the to-do list.")
        print("Enter \033[1mview complete \033[0mto view the completed task in the to do list.")
        print("Enter \033[1mdelete \033[0mto delete the to-do list and take it to the bin.")
        print("Enter \033[1mview bin \033[0mto view all the tasks in the bin.")
        print("Enter \033[1mrestore \033[0mto restore a task from the bin.")
        print("Enter \033[1mclear bin \033[0mto clear all tasks from the bin.")
        print("Enter \033[1mhelp \033[0mto display all the help messages.")
        print("Enter \033[1mexit \033[0mto exit the program.")
                
    elif command == 'exit':
        print("Are you sure you want to exit?")
        save_list()
        break
    else:
        print("The command you have entered is invalid. You can go to help.")
