import random

user_score = 0 
computer_score = 0

options = ["rock", "paper", "scissor"]

while True:
  user_choice = input("Choose Rock/Paper/scissor (or) press Q to quit: ").lower()

  if user_choice == "q":
    print("Come back later>>>")
    break
  
  if user_choice not in options:
    print("Please choose a valid choice")
    continue

  random_number = random.randint(0, 2)
  # 0-rock, 1-paper, 2-scissor
  computer_choice = options[random_number]
  print(f"Computer picked {computer_choice}.")

  if user_choice == computer_choice:
    print("It's a tie. Go again")
    continue

  elif user_choice == "rock" and computer_choice == "scissor":
    print("You won..!!")
    user_score += 1
    continue

  elif user_choice == "paper" and computer_choice == "rock":
    print("You won..!!")
    user_score += 1
    continue

  elif user_choice == "scissor" and computer_choice == "paper":
    print("You won..!!")
    user_score += 1
    continue

  else:
    print("You Lose...")
    computer_score += 1

print("--------------------------------------")
print(f"You won {user_score} times")
print(f"Computer won {computer_score} times")  
print("--------------------------------------")