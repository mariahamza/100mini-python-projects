print("Welcome To Maria's Pizza Shop")
pizza=['Margherita','Pepperoni','Four Cheese','BBQ Chicken','Hawaiian']
phonebook={'Maria':'095389477','Lara':'09313972','Basma':'0933034732','Mudar':'095958745','Sarah':'0988373289'}
Prices={'Margherita':9,'Pepperoni':12,'Four Cheese':10,'BBQ Chicken':14,'Hawaiian':15}
sizes=("Small","Medium","Large")
customer=set()

print('Choose your pizza:')

while True:
  try:
    cchoice=int(input('1-Margherita Pizza\n2-Pepperoni Pizza\n3-Four Cheese Pizza\n4-BBQ Chicken Pizza\n5-Hawaiian Pizza\n'))
    if 1<=cchoice<=5 :
      break
    print('Please enter a valid number')
  except ValueError:
    print("Enter a number, not a text.")

name=pizza[cchoice-1]
price=Prices[name]
print(name+": "+"$"+str(price))

print("Choose Your Pizza Size:")
while True:
  try:
    schoice=int(input("1-Small\n2-Medium\n3-Large\n"))
    if 1<=schoice<=3:
      break
    print("Enter a valid number:")
  except ValueError:
    print("Enter a number, not a text")
text=sizes[schoice-1]

if schoice==3:
  price+=3
print(text+": Price: $"+str(price))

print("what's your name?")
customer_name=input('-> ').strip().capitalize()
customer.add(customer_name)

if customer_name in phonebook:
  print(f"Welcome back {customer_name}!\nYour number: {phonebook[customer_name]}")
else:
  print(f"Hello there {customer_name}!")





