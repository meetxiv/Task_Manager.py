
tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({
        "title": title,
        "description": description,
        "completed": False
    })
    print(f"Task '{title}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, 1):
        status = "completed" if task["completed"] else "pending"
        print(f"{index}. [{status}] {task['title']} - {task['description']}")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print(f"Task '{tasks[task_num]['title']}' marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task['title']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    while True:
        print("\n=== Simple Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nWhat would you like to do? (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
