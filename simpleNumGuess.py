import random

number=random.randint(1,10)

guess=int(input("Please Guess a number between 1 and 10: "))

if(guess==number):
	print("Correct, you win")
elif(guess<number):
	print("Too Low")
elif(guess>number):
	print("Too High")
else:
	print("That's not a number")

print("The right answer was: "+ str(number))
