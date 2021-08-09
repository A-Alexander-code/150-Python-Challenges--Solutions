import random

def additon():
    num01 = random.randint(5,20)
    num02 = random.randint(5,20)
    print(num01," + ",num02," = ")
    user_amswer = int(input("Your answer is: "))
    system_answer = num01 + num02
    answers = (user_amswer,system_answer)
    return answers

def subtraction():
    num03 = random.randint(25,50)
    num04 = random.randint(1,25)
    print(num03," - ",num04," = ")
    user_answer =  int(input("Your answer is: "))
    system_answer = num03 - num04
    answers = (user_answer,system_answer)
    return answers


def check_answer(user_answer,system_answer):
    if user_answer == system_answer:
        print("¡Correct!")
    else:
        print("Incorrect, the actual answer is",system_answer)
    
    
def main():
    print("1) Addition")
    print("2) Subtraction")
    selection = int(input("Enter 1 or 2: "))
    if selection == 1:
        user_answer, system_answer = additon()
        check_answer(user_answer,system_answer)
    elif selection == 2:
        user_answer, system_answer = subtraction()
        check_answer(user_answer,system_answer)
    else:
        print("Incorrect selection")

main()