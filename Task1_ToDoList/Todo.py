
tasks = []

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")

        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            print("Deleted:", deleted["task"])
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
import json

# Load saved tasks
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save tasks
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()

# Main application
while True:

    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":

        task = input("Enter your task: ").strip()

        if task:
            tasks.append({
                "task": task,
                "completed": False
            })

            save_tasks()
            print("Task added successfully!")

        else:
            print("Task cannot be empty.")

    # View Tasks
    elif choice == "2":

        print("\nYour Tasks:")

        if not tasks:
            print("No tasks available.")

        for i, task in enumerate(tasks, start=1):

            status = "Completed" if task["completed"] else "Pending"

            print(f"{i}. {task['task']} - {status}")

    # Mark Completed
    elif choice == "3":

        try:
            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):

                tasks[number - 1]["completed"] = True

                save_tasks()
                print("Task completed successfully!")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":

        try:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):

                deleted = tasks.pop(number - 1)

                save_tasks()
                print("Deleted:", deleted["task"])

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    # Exit
    elif choice == "5":

        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")