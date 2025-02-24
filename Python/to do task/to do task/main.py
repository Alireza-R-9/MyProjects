import os

FILE_NAME = 'todo_list.txt'


def load_tasks():

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    else:
        tasks = []
    return tasks


def save_tasks(tasks):

    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def add_task(tasks):

    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added.')


def remove_task(tasks):

    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task number.")


def edit_task(tasks):

    task_index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_index < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_index] = new_task
        save_tasks(tasks)
        print(f'Task {task_index + 1} updated to "{new_task}".')
    else:
        print("Invalid task number.")


def display_tasks(tasks):

    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Edit task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
