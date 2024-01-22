import os

def display_menu():
    """
    Display the menu options for the To-Do List Application.
    """
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_todo_list(todo_list):
    """
    Display the current To-Do list.
    """
    print("\nCurrent To-Do List:")
    if not todo_list:
        print("No tasks yet.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    """
    Add a new task to the To-Do list.
    """
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the To-Do list.")

def mark_completed(todo_list):
    """
    Mark a task as completed in the To-Do list.
    """
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        todo_list[index] += " (Completed)"
        print("Task marked as completed.")
    except IndexError:
        print("Invalid index. Task not found.")

def delete_task(todo_list):
    """
    Delete a task from the To-Do list.
    """
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        deleted_task = todo_list.pop(index)
        print(f"Task '{deleted_task}' deleted.")
    except IndexError:
        print("Invalid index. Task not found.")

def todo_list_app():
    # Initialize an empty To-Do list
    todo_list = []

    while True:
        # Display the menu
        display_menu()

        # Get user choice
        choice = input("Enter your choice (1-5): ")

        # Perform the chosen action
        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    # Run the To-Do List Application
    todo_list_app()
