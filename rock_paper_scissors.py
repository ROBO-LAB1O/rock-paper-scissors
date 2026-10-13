##ROCK - PAPER - SIC##
import random
c=['rock','paper','sci']

count=0
while True:
    b=random.choice(c)
    a=input("Enter your choice: ").strip().lower()
    if a==b:
      print("it's a tie btw....")
    elif a=='rock' and b=='paper':
      print("Computer wins ! Try again")
      break
    elif a=='rock' and b=='sci':
      print("You won!")
      break
    elif a=='paper' and b=='sci':
      print("Computer win")
      break
    elif a=='paper' and b=='rock':
      print("you won")
      break
    elif a=='sci' and b=='rock':
      print("Computer won")
      break
    elif a=='sci' and b=='paper':
      print("you won")
      break
    else:
      print("Error!")
    count+=1
    
print(f"Computer chosed {b}")
print(count)


