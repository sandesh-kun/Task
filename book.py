# #Task 1

# num =  int(input("Enter a number up to which for Even number: "))

# for n in range(2, num + 1, 2):
#     print(n)
    
#Task 2
import random
guess_number = random.randint(1,100)
att = 3

for att in range (1, att+1, 1):
     guess = int(input("Attempt {}:Enter guess number: ".format(att)))
     
     if guess == guess_number:
         print("Correct Guess.")
         break
     else:
         if guess < guess_number:
             print("Higher than this number.")
         else:
             print("Lower than this number.")
else:
    print("The correct guess number was {}".format(guess_number))
            