def add_task(tasks):
    title= input("Enter the task to add: ")
    tasks = {
        "title": title,
        "completed": True
    }

    tasks.append(tasks)
    print(f"Task '{title}' added successfully!")

    def python_fuction(select_menu):
        print("running python function")
        print(select_menu)