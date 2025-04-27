#Create a function that show the menu 
def display_menu():
  print("\n==================== Developed by Imranshuraj ====================")
  print("\n\n====================To-Do-List Menu====================")
  print("1. View Tasks")
  print("2. Add Task")
  print("3. Remove Task")
  print("4. Mark Task as Processing")
  print("5. Mark task as completed")
  print("6. Exit")
  
#Function that show the tasks
def display_tasks(tasks):
  if not tasks:
    print("There are no tasks here.")
  else:
    print("Here are your tasks: \n")
    for i, task in enumerate(tasks, start=1):
      print(f"Task {i}. {task}")

#Function to add a task      
def add_task(tasks):
  task = input("Enter the task you want to add:")
  tasks.append(task)
  print(f"Task '{tasks}' has been added to the list.")

#Function to remove a task  
def remove_task(tasks):
  display_tasks(tasks)
  if tasks:
    try:
      task_num = int(input("\nEnter the number of the task to remove: "))
      if 1 <= task_num <=len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' has been removed.")
      else:
        print("Invalid task number.")
    except ValueError:
      print("Please enter a valid number.")
      
#Function to add task as processing
def mark_task_as_processing(tasks):
  display_tasks(tasks)
  if tasks:
    try:
      task_num = int(input("\nEnter the number of the task to mark task as processing:"))
      if 1 <= task_num <= len(tasks):
        tasks[task_num -1] += " [Task is under processing]"
        print(f"Task {task_num} has been marked as processing.")
      else:
        print("Invalid task number.")
    except ValueError:
      print("Please enter a valid number.")
     
#Function to add task is completed
def mark_task_as_completed(tasks):
  display_tasks(tasks)
  if tasks:
    try:
      task_num = int(input("\nEnter the number of task to mark task  as completed"))
      if 1 <= task_num <= len(tasks):
         tasks[task_num - 1] += "[Task is completed]"
         print(f"Task {task_num} has been marked as completed.")
      else:
        print("Invalid task number.")
    except ValueError:
      print("Please enter a valid number.")
      
#Main function to run the program
def main():
  tasks = []
  display_menu()
  while True:
    choice = input("\nPlease select  an option (1-5): ")
    print("=========================================================\n")
    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      add_task(tasks)
    elif choice == "3":
      remove_task(tasks)
    elif choice == "4":
      mark_task_as_processing(tasks)
    elif choice == "5":
      mark_task_as_completed(tasks)
    elif choice == "6":
      print("Now you have exited the program. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")
        
if __name__ == "__main__":
  main()