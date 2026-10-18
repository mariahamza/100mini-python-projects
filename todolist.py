print("***Maria's To-Do List:***")
import json

def save_tasks():
  with open("tasks.json","w") as f:
    json.dump(tasks,f)
    
def add_task(title):
  tasks.append({"Title":title,"Done":False})

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, start=1):
        if task["Done"]:
            print(i, "[x]", task["Title"])
        else:
            print(i, "[ ]", task["Title"])

def complete_task(num):
  if 1 <= num <= len(tasks):
    tasks[num-1]["Done"]=True

def delete_task(dnum):
  if 1 <= dnum <= len(tasks):
    tasks.pop(dnum-1)
    
def load_tasks():
  try:
    with open("tasks.json", "r") as f:
      return json.load(f)
  except FileNotFoundError:
    return []
    
tasks = load_tasks()
    
while True:
  print("1- Add Task\n2- View Tasks\n3- Complete Task\n4- Delete task\n5- Quit")
  while True:
    try:
      choice=int(input("Your Choice: > "))
      if 1<=choice<=5:
        break
      print("Choose a number (1-5):")
    except ValueError:
      print("Enter a number.")
    
  if choice==1:
    title=input("What's the task you wanna add?\n")
    add_task(title)
    save_tasks()
  
  
  elif choice==2:
    view_tasks()
    
  
  elif choice==3:
    if len(tasks)==0:
      print("No tasks to complete. List is empty.")
    else:
      while True:
        try:
          num=int(input("What task did you complete?"))
          break
        except ValueError:
          print("Enter a valid number.")
      complete_task(num)
      save_tasks()
      
  elif choice==4:
    if len(tasks)==0:
      print("No tasks to delete.")
    else:
      while True:
        try:
          dnum=int(input("What task do you wanna delete?"))
          break
        except ValueError:
          print("Enter a valid number.")
      delete_task(dnum)
      save_tasks()

  elif choice==5:
    break







