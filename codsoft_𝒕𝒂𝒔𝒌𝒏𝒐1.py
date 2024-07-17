import os
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: {task}')
    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task["completed"] else 'Not Done'
            print(f'{idx}. {task["task"]} - {status}')
    def mark_task_as_completed(self, index):
        if index < 1 or index > len(self.tasks):
            print('Invalid task number.')
            return
        self.tasks[index - 1]["completed"] = True
        print(f'Task {index} marked as completed.')
    def delete_task(self, index):
        if index < 1 or index > len(self.tasks):
            print('Invalid task number.')
            return
        removed_task = self.tasks.pop(index - 1)
        print(f'Deleted task: {removed_task["task"]}')
    def clear_tasks(self):
        self.tasks.clear()
        print('All tasks cleared.')
def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Clear all tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_as_completed(index)
        elif choice == '4':
            index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
main()
