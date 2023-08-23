import random
from data import question_data

#creating true/false in a simple way
count, score = 1, 0
choice_list = []
while count <= 10:
    choice = random.randint(0,11)
    if choice in choice_list:
        continue
    choice_list.append(choice)
    answer = input(f"Q.{count}: {question_data[choice]['text']}. (True/False): ").lower()
    if answer == question_data[choice]['answer'].lower():
        score += 1
        print(f"You got it right!\nThe correct answer was: {question_data[choice]['answer']}.")
        print(f"Your current score is {score}/{count}\n\n")
    else:
        print(f"That's wrong!\nThe correct answer was: {question_data[choice]['answer']}.")
        print(f"Your current score is {score}/{count}\n\n")
    count += 1
print(f"You've completed the quiz\nYour final score was: {score}/{count-1}")