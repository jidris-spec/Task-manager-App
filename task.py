# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")  # Prompt the user to input the task name
    tasks.append({"name": task_name, "completed": False})  # Append a dictionary representing the task to the tasks list
    print("Task added successfully.")  # Print a success message

# Function to view all tasks
def view_tasks(tasks):
    print("Tasks:")  # Print a header for the list of tasks
    for index, task in enumerate(tasks, start=1):  # Iterate over the tasks list, starting the index from 1
        status = "Completed" if task["completed"] else "Incomplete"  # Determine the status of the task based on the "completed" key in the dictionary
        print(f"{index}. {task['name']} - {status}")  # Print the task name and its status

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)  # Call the view_tasks function to display all tasks
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1  # Prompt the user to input the index of the task to mark as completed
    if 0 <= task_index < len(tasks):  # Check if the entered index is valid
        tasks[task_index]["completed"] = True  # Mark the selected task as completed by setting its "completed" key to True
        print("Task marked as completed.")  # Print a success message
    else:
        print("Invalid task index.")  # Print an error message if the entered index is invalid

# Main program
def main():
    tasks = []  # Initialize an empty list to store tasks
    while True:  # Start an infinite loop
        print("\nTask Manager")  # Print the title of the task manager
        print("1. Add Task")  # Print the option to add a task
        print("2. View Tasks")  # Print the option to view tasks
        print("3. Mark Task as Completed")  # Print the option to mark a task as completed
        print("4. Exit")  # Print the option to exit the program

        choice = input("Enter your choice: ")  # Prompt the user to input their choice

        if choice == "1":  # If the user chooses to add a task
            add_task(tasks)  # Call the add_task function
        elif choice == "2":  # If the user chooses to view tasks
            view_tasks(tasks)  # Call the view_tasks function
        elif choice == "3":  # If the user chooses to mark a task as completed
            mark_completed(tasks)  # Call the mark_completed function
        elif choice == "4":  # If the user chooses to exit the program
            print("Exiting the Task Manager.")  # Print a message indicating program exit
            break  # Exit the while loop and end the program
        else:  # If the user enters an invalid choice
            print("Invalid choice. Please try again.")  # Print an error message

if __name__ == "__main__":
    main()  # Call the main function to start the program
