import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        quit()

    if user_input not in options :
        print("Please try again. ")
        continue
    
    random_number = random.randint (0,2)

    # 0:rock, 1:paper and 2:scissors

    computer_hand = options[random_number]
    print("Computer picked", computer_hand + ".")

    if user_input == "rock" and computer_hand == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_hand == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_hand == "paper":
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You lost!")
        computer_wins += 1

        
print("You won", user_score , "times!")
print("The computer one", computer_score, "times")
print("Goodbye")



