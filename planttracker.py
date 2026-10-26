from datetime import date
import json

def loadplants():
    try:
        with open("plants.txt", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def storeplants():
    with open("plants.txt", "w") as f:
        json.dump(plants, f)

def ask_number(question, low, high):
    while True:
        try:
            n = int(input(question))
            if low <= n <= high:
                return n
            print(f"Enter a number from {low} to {high}.")
        except ValueError:
            print("Enter a number.")

def addplant(name, every):
    today_str = str(date.today())
    plants.append({
        "Name": name,
        "Every": every,
        "DatePlanted": today_str,  # Recorded when added
        "LastWatered": today_str
    })
    print("Plant Added Successfully!")

def viewplants():
    if len(plants) == 0:
        print("No Plants Yet.")
    else:
        for i, plant in enumerate(plants, start=1):
            
            planted_on = plant.get("DatePlanted", "Unknown")
            print(f"{i}. {plant['Name']} | Planted: {planted_on} | Water every {plant['Every']} days")

def waterplant(num):
    plants[num - 1]["LastWatered"] = str(date.today())
    print(f"'{plants[num - 1]['Name']}' has been watered!")

def days_since(plant):
    last = date.fromisoformat(plant["LastWatered"])
    return (date.today() - last).days

def needswater(plant_name):
    found = False
    for plant in plants:
        if plant["Name"].lower() == plant_name.lower():
            found = True
            days = days_since(plant)
            print(f"Last watered {days} day(s) ago.")
            if days >= plant["Every"]:
                print("Needs Watering!")
            else:
                print("Hydrated! Doesn't need water yet.")
            break
    if not found:
        print("Plant Not Found!")

def deleteplant(num):
    if len(plants) == 0:
        print("Nothing to Delete.")
    else:
        removed = plants.pop(num - 1)
        print(f"Deleted '{removed['Name']}'.")

plants = loadplants()

print("----Plant Tracker----")
while True:
    print("\n1- Add Plant\n2- View Plants\n3- Water A Plant\n4- What Needs Water?\n5- Delete Plant\n6- Quit")
    choice = ask_number("Your Choice > ", 1, 6)

    if choice == 1:
        name = input("Plant Name:\n").strip().title()
        if name == "":
            print("Name can't be empty.")
        else:
            every = ask_number("Water it every how many days? ", 1, 365)
            addplant(name, every)
            storeplants()

    elif choice == 2:
        viewplants()

    elif choice == 3:
        if len(plants) == 0:
            print("No plants to water.")
        else:
            viewplants()
            num = ask_number("Enter the number of the plant you watered: ", 1, len(plants))
            waterplant(num)
            storeplants()

    elif choice == 4:
        if len(plants) != 0:
            name = input("Enter plant name to check:\n").strip()
            needswater(name)
        else:
            print("No plants added yet.")

    elif choice == 5:
        if len(plants) == 0:
            print("Nothing to Delete.")
        else:
            viewplants()
            num = ask_number("Enter the number of the plant to delete: ", 1, len(plants))
            deleteplant(num)
            storeplants()

    elif choice == 6:
        print("Goodbye!")
        break
