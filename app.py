# libraries
from datetime import datetime

# define the task object
class Task:
    def __init__(self, task_id, title, description, due_date, priority_level, status, created_at):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority_level = priority_level
        self.status = status
        self.created_at = created_at

    def __str__(self):
        return f"ID: {self.task_id} \nTitle: {self.title} \nDescription: {self.description} \nDue Date: {self.due_date} \nPriority: {self.priority_level} \nStatus: {self.status} \nCreated at: {self.created_at} \n"

# define the task manager
class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.priority_list = ['low', 'medium', 'high']
        self.status_list = ['pending', 'in progress', 'completed']

    # add individual tasks
    def add_task(self, title, description, due_date, priority_level, status):
        # input validation
        if not isinstance(title, str):
            raise TypeError("Title must be a string element.")
        if not isinstance(description, str):
            raise TypeError("Description must be a string element.")
        if not isinstance(due_date, str):
            raise TypeError("Due date must be a string element.")
        if priority_level.lower() not in self.priority_list:
            raise ValueError("Priority level must be a valid value.")
        if status.lower() not in self.status_list:
            raise ValueError("Status must be a valid value.")

        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description, due_date, priority_level, status, created_at=datetime.now())
        self.tasks[task_id] = new_task
        print(f"Task {title} was added successfully!")

    # displaying all tasks
    def display_tasks(self, filter_column=None, filter_value=None):
        tasks_to_display = self.tasks.values() 

        if filter_column and filter_value:
            
            tasks_to_display = [
                task for task in tasks_to_display 
                if str(getattr(task, filter_column, "")).lower() == str(filter_value).lower()
            ]

        if not tasks_to_display:
            print("No tasks found.")

        for task in tasks_to_display:
            print(task)

    def update(self, task_id, column, value):
        if task_id not in self.tasks:
            raise ValueError("The task id provided was not found.")

        task_to_update = self.tasks[task_id]
        
        if hasattr(task_to_update, column):
            setattr(task_to_update, column, value)
            print(f"Updated {column} of task id {task_id} to {value}.")
        else:
            print(f"Column {column} does not exist.")

    def mark_as_completed(self, task_id):
        self.update(task_id, column='status', value='completed')

    def delete_task(self, task_id):
        if task_id not in self.tasks:
            raise ValueError("The task id provided was not found.")
        
        del self.tasks[task_id]
        print(f"Task {task_id} successfully removed!")

if __name__ == '__main__':
    task_manager = TaskManager()
    
    while True:
        print("""What would you like to do? (Enter the number)
        1. Add a task
        2. Display all tasks
        3. Update a task
        4. Mark a task as completed
        5. Delete a task
        6. Exit""")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")
            due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            priority_level = input("Enter the priority level of the task (low, medium, high): ")
            status = input("Enter the status of the task (pending, in progress, completed): ")

            task_manager.add_task(title, description, due_date, priority_level, status)
        
        elif choice == '2':
            print("1. Show all tasks")
            print("2. Filter tasks")

            sub_choice = input("Select an option: ")

            if sub_choice == '2':
                column = input("Enter the column to filter by: ").strip().lower()
                value = input(f"Enter the value for {column}: ").strip().lower()
                task_manager.display_tasks(filter_column=column, filter_value=value)
            else:
                task_manager.display_tasks()

        elif choice == '3':
            task_id = int(input("Enter the task id of the row to be modified: "))
            column = input("Enter the column to be modified: ")
            value = input("Enter the new value: ")

            task_manager.update(task_id, column, value)

        elif choice == '4':
            task_id = int(input("Enter the task id to be marked as completed: "))

            task_manager.mark_as_completed(task_id)

        elif choice == '5':
            task_id = int(input("Enter the task id to be deleted: "))

            task_manager.delete_task(task_id)

        elif choice == '6':
            print("Closing out of the program")
            break
        
        else:
            print("Please enter a number from 1 - 6.")