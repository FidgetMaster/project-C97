import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess A Number Between 1 And 9:")
while chances < 5:
    guess = int(input("Enter Your Guess: "))
    if(guess == number):
        print("You Win!")
        break
    elif(guess < number):
        print("Too Low, Guess A Number Higher Than: ", guess)
    else:
        print("Too High, Guess A Number Lower Than: ", guess)
    chances = chances + 1
if not chances < 5:
    print("You Loose. The Number Is: ", number)
    
