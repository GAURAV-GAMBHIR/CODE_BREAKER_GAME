import random
# GET GUESS
def get_guess():
    return list(input("What is your guess?"))
# GENERATE COMPUTER CODE
def generate_code():
    digits=[str(num) for num in range(10)]
    # SHUFFLE THE DIGITS
    random.shuffle(digits)
    #THEN GRAB THE FIRST THREE
    return digits[:3]
#GENERATE THE CLUES
def generate_clues(code,user_guess) :
    if user_guess==code :
        return "CODE CRACKED"
    clues=[]
    for ind,num in enumerate(user_guess) :
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues==[]:
        return ["NOPE"]
    else:
        return clues
#RUN GAME LOGIC
print("WELCOME TO CODE BREAKER GAME!")
secret_code = generate_code()
clue_report=[]
while clue_report != "CODE CRACKED":
    guess=get_guess()
    clue_report=generate_clues(guess,secret_code)
    print(" HERE IS THE RESULT OF YOUR GUESS:")
    for clue in clue_report:
        print(clue)
