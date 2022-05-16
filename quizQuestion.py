#Quiz Question

points = 3
#Q1
answer = input("What is the capital of France?")
answer = answer.title()
while answer != "Paris":
    answer = input("Incorrect, try again: ")
    points = points - 1
    answer = answer.title()
print("Correct! Well done.")
if points < 0:
    points = 0
print("You have",points,"points")

#Q2
answer = input("Where is the Brandenburg Gate?")
answer = answer.title()
while answer != "Berlin":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
print("Correct! Well done.")
points = points + 1
print("You have",points,"points")

#Q3
answer = input("Where is the Colliseum?")
answer = answer.title()
while answer != "Rome":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
print("Correct! Well done.")
points = points + 1
print("You have",points,"points")
