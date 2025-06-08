
def getselected_menu():
    print("------------To Do List App-------------")
    print("Menu:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Mark a task as completed")
    print("5. Load tasks from file")
    print("6. Save tasks to file")
    print("7. Exit")

    select_menu = input("Select an option number: ")
    select_menu =int(select_menu)
    print("You selected option: ",select_menu)
    print(type(select_menu))
    return select_menu

while True:
    select_menu = getselected_menu()

    tasks = []

    if select_menu == 1:
        task = input("Enter the task to add: ")
        print(f"Task '{task}' added successfully!")
    elif select_menu == 2:
        print("Here are all your tasks:")
        # This would normally list tasks, but we don't have any tasks yet.
    elif select_menu == 3:
        task_id = input("Enter the task ID to delete: ")
        print(f"Task with ID {task_id} deleted successfully!")
    elif select_menu == 4:
        task_id = input("Enter the task ID to mark as completed: ")
        print(f"Task with ID {task_id} marked as completed!")
    else:
        print("Invalid option selected. Please try again.")