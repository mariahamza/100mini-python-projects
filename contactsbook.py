import json
print("-----Contacts Book-----")
contacts= []
def store_info():
  with open("contacts.txt","w") as f:
    return json.dump(contacts,f)

def add_contact(name,number,email):
  name=name.title()
  contacts.append({"Name":name,"Number":number,"Email":email})

def view_contacts():
  if len(contacts)==0:
    print("No Contacts.")
  else:
    for i,contact in enumerate(contacts,start=1):
      print(i,contact["Name"],contact["Number"],contact["Email"])

def search_contacts(search):
  found=False
  for contact in contacts:
    if search.lower() in contact["Name"].lower():
      print("Contact found!")
      print(contact["Name"],contact["Number"],contact["Email"])
      found=True
  if not found:
    print("Contact not found.")
  
def edit_contacts(num,number,email):
  if number!="":
    contacts[num-1]["Number"]=number
  if email!="":
    contacts[num-1]["Email"]=email
  

def delete_contact(num):
  if len(contacts)==0:
    print("Cannot delete. List is already empty.")
  else:
    contacts.pop(num-1)
    print("Contact deleted")

def load_contacts():
  try:
    with open("contacts.txt","r") as f:
      return json.load(f)
  except FileNotFoundError:
    return []

contacts=load_contacts()

while True:
  print("1- Add Contact\n2- View All Contacts\n3- Search Contact\n4- Edit Contact\n5- Delete Contact\n6- Quit\n")
  while True:
    try:
      choice=int(input("Choose Number: > "))
      if 1<=choice<=6:
        break
      print("Choice must be between 1-6.")
    except ValueError:
      print("Enter a number.")

  if choice==1:
    while True:
        name=input("Add Name: ")
        number=input("Add Number: ")
        email=input("Add Email: ")
        break
    add_contact(name,number,email)
    print("Contact Added!")
    store_info()

  elif choice==2:
    view_contacts()

  elif choice==3:
      search=input("Enter the name you're searching for:\n")
      search=search.lower()
      search_contacts(search)
  
  elif choice==4:
    if len(contacts)==0:
      print("Nothing to edit.")
    else:
      view_contacts()
      while True:
        try:
          num=int(input("Which contact do you want to edit? "))
          if 1<=num<=len(contacts):
            break
          print("Contact not found.")
        except ValueError:
          print("Enter a number.")
      number=input("New number (Enter to keep): ").strip()
      email=input("New email (Enter to keep): ").strip()
      edit_contacts(num,number,email)
      print("Contact Updated!")
      store_info()

  elif choice==5:
    if len(contacts)==0:
      print("Contact Book is already empty.")
    else:
      view_contacts()
      while True:
        try:
          num=int(input("Which contact do you wanna delete? "))
          if 1<=num<=len(contacts):
            break
          print("Contact not found.")
        except ValueError:
          print("Enter a number.")
      delete_contact(num)
      store_info()

  elif choice==6:
    break


      




    
