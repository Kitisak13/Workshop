def view_task(tasks):
    for task in tasks:
        print(f"Task: {task['title']}, Completed: {task['completed']}")