import datetime
import random
from os import write

Task_files = "MyTasks.txt"

Quotes = [
    "Keep going! You're doing great.",
    "One step at a time!",
    "Focus on progress, not perfection.",
    "Your future depends on what you do today.",
    "Small efforts add up to big results.",
    "Stay positive and keep pushing forward!"
]

def add_task(task):
    date = datetime.date.today().isoformat()
    with open(Task_files,"a") as file:
        file.write(f"{date}: {task}\n")
    print("Tasks added successfully!")
    print("Motivation:", random.choices(Quotes))


def view_tasks():
    try:
        with open(Task_files,"r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found, Wanna add something??")
            else:
                print("\n-----Your Tasks-----")
                for task in tasks:
                    print(task.strip())
                print("\nMotivation: ", random.choice(Quotes))
    except FileNotFoundError:
        print("No task file found. Start by adding a task.")

def main():
    while True:
        print("\n_____ Daily Task Logger ____")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter The Tasks Description: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye My Friend! Have a Great Day!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()



