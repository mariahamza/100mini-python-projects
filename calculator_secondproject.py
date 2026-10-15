print("****Maria's Calculator****")
def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
 try:
  b!=0
  return a/b
 except:
   print('Cannot divide by 0')

operations={"+":add,"-":subtract,"*":multiply,"/":divide}
while True:
  choice=input("Another Calculation?\n").capitalize()
  if choice=="No":
    break
  elif choice=="Yes":
    
    while True:
      try:
        a=float(input('Enter first number:\n'))
        break
      except ValueError:
        print('Please enter a valid number, not a char.')

    while True:
      try:
        b=float(input('Enter Second number:\n'))
        break
      except ValueError:
        print('Please enter a valid number.')
  
    while True:
        oinput=input('Enter operation:\n')
        if oinput in operations:
          break
        print('Enter + - * /:')

    result=operations[oinput](a,b)
    print(result)

  else:
    print('Enter Yes or No?')
    


