from random import randint
from art import logo
EASY_LIVES = 10
HARD_LIVES = 5

#difficulty function 
def game_level(level, random_num):
  if level =="easy":
    return EASY_LIVES
  else:
    return HARD_LIVES
    
def game():
  print(logo)
  print("Welcome to the number guessing game!")
  print("Im thinking of a number between 1 and 100")
  
  #Compare guess function
  def compare_guess(user_guess, random_num, turns):
    if user_guess == random_num:
      print(f"You got it! the answer was {random_num}")
    elif user_guess <  random_num:
      print("Try again too low")
      return turns - 1
    else:
      print("Try again too high")
      return turns - 1
  
  
  #Random number between 1 and 100
  random_num = randint(1,100)
  #print(f"Psst the number is {random_num}")
  level = input("Choose a difficulty. 'easy' or 'hard': ")
  game_level(level, random_num)
  
  #Let the user guess a number
  turns = game_level(level, random_num)
  
  
  user_guess = 0
  while user_guess != random_num:
    print(f"You have {turns} turns to make a guess")
    user_guess = int(input("Guess a number:"))
  
    turns = compare_guess(user_guess, random_num, turns)
    if turns == 0:
      print("You've run out of guesses. Sorry")
      return

game()
  
  
  
  
