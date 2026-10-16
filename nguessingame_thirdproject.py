import random
secret=random.randint(1,100)
count=0

while True:
  while True:
    try:
      inp=int(input('Enter a number (1-100)\n'))
      if 1<=inp<=100:
        break
      print('Number not in range.')
    except ValueError:
      print('Enter a number. Not a char')
  
  count+=1

  if inp<secret:
    print('Too low.')
  elif inp>secret:
    print('Too high.')
  elif inp==secret:
    print(f'You got it! it took you {count} times to get it right.')
    break

  if count==7:
    print(f'You lose! it was {secret}.')
    break

    
