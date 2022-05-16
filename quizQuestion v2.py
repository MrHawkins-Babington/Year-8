#Quiz Question

goes = 1
points = 3
totalPoints = 0

#Q1
answer = input("What is the capital of France?")
answer = answer.title()
while answer != "Paris":
    answer = input("Incorrect, try again: ")
    points = points - 1
    goes = goes + 1
    if points < 0:
        points = 0
    else:
        points = points
    answer = answer.title()
totalPoints = totalPoints + points
print("Correct! Well done.")
print("\nYou got",points,"points for this question.")
print("It took you",goes,"goes to get this question correct.")
 



#Q2
goes = 1
points = 3

answer = input("\nWhat is Spanish for hat?")
answer = answer.title()
while answer != "Sombrero":
    answer = input("Incorrect, try again: ")
    points = points - 1
    goes = goes + 1
    if points < 0:
        points = 0
    else:
        points = points
    answer = answer.title()
totalPoints = totalPoints + points
print("Correct! Well done.")
print("\nYou got",points,"points for this question.")
print("It took you",goes,"goes to get this question correct.")

#Q3
goes = 1
points = 3

print("\nHow far is it from John O'groats to Lands end?")
print("Is it 674, 874 or 1074 miles?")
answer = input()
answer = answer.title()
while answer != "874":
    answer = input("Incorrect, try again: ")
    points = points - 1
    goes = goes + 1
    if points < 0:
        points = 0
    else:
        points = points
    answer = answer.title()
totalPoints = totalPoints + points
print("Correct! Well done.")
print("You got",points,"points for this question.")
print("\nIt took you",goes,"goes to get this question correct.")
print("Your total score is",totalPoints)
