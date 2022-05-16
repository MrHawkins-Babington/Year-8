#Quiz Question

#Q1
answer = input("What is the capital of France?")
answer = answer.title()
while answer != "Paris":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
print("Correct! Well done.")


#Q2
answer = input("Where is the Brandenburg Gate?")
answer = answer.title()
while answer != "Berlin":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
print("Correct! Well done.")

#Q3
answer = input("Where is the Colliseum?")
answer = answer.title()
while answer != "Rome":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
print("Correct! Well done.")
