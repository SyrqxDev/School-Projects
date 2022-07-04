import random
import replit
import time
from getpass import getpass
def wait(number):
  time.sleep(number)
rps = ["rock", "paper","scissors"]
PC_Point = 0
PlayerPoint = 0 


def Begin():
  pc_or_plr = int(input("Do you want to play with a player or without a player\n[1] Computer\n[2] Player\n[Choice]: " ))
  mode = pc_or_plr
  if mode == 1:
    computer()
  elif mode == 2:
    playerMode()

def computer():
  replit.clear()
  
  choice = random.choice(rps)
  global PC_Point, PlayerPoint
  userChoice = int(input("Enter a choice to play:\n[1]: Rock\n[2]: Paper\n[3]: Scissors:\n[Choice]: "))
  PC_Point = PC_Point
  PlayerPoint = PlayerPoint
  
  if userChoice == 1 and choice == "rock":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    print("Draw, Rock can't beat Rock! You both get a point")
    PC_Point += 1
    PlayerPoint += 1
    endScreen("Draw", PC_Point, PlayerPoint)
  elif userChoice == 2 and choice == "rock":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PlayerPoint += 1
    print("You won! Paper beats rock! You recieve a point")
    endScreen("User", PC_Point, PlayerPoint)
  elif userChoice == 3 and choice == "rock":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PC_Point += 1
    print("You Lost! Rock Beats Scissors! The computer recieved a point")
    endScreen("Computer", PC_Point, PlayerPoint)
  elif userChoice == 1 and choice == "paper":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PC_Point += 1
    print("You Lost! Paper beats Rock! The computer recieved a point")
    endScreen("Computer", PC_Point, PlayerPoint)
  elif userChoice == 2 and choice == "paper":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PC_Point += 1
    PlayerPoint += 1
    print("Draw! Paper can't beat Paper! You both recieve a point")
    endScreen("Computer", PC_Point, PlayerPoint)
  elif userChoice == 3 and choice == "paper":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PlayerPoint += 1
    print("You Win! Paper beats Rock! You recieve a point")
    endScreen("Computer", PC_Point, PlayerPoint)
  elif userChoice == 1 and choice == "scissors":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PC_Point += 1
    print("You Lose! Rock beats Scissors! The computer recieved a point")
    endScreen("Computer", PC_Point, PlayerPoint)
  elif userChoice == 2 and choice == "scissors":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PlayerPoint += 1
    print("You Win! Scissors beats Paper! You recieve a point")
    endScreen("Computer", PC_Point, PlayerPoint)
  elif userChoice == 3 and choice == "scissors":
    replit.clear()
    print("The computer chose", choice, "and you chose", userChoice)
    wait(1)
    PC_Point += 1
    PlayerPoint += 1
    print("Draw! Scissors can't beat Scissors! You both recieve a point")
    endScreen("Computer", PC_Point, PlayerPoint)

  
def playerMode():
  player1 = True
  player2 = False
  global username1
  global username2
  username1 = input("Enter the username of player1 ")
  username2 = input("Enter the username of player2 ")
  global p1Score, p2Score
  p1Score = 0
  p2Score = 0

  
  if player1== True:
    replit.clear()
    player2 = True
    player1 = False
    print(username1 + "'s Turn:")
      
    choice = int(getpass("Enter a choice to play:\n[1]: Rock\n[2]: Paper\n[3]: Scissors:\n[Choice]: "))
    replit.clear()
    wait(1)
    print(username2 + "'s Turn: ")
    choice2 = int(getpass("Enter a choice to play:\n[1]: Rock\n[2]: Paper\n[3]: Scissors:\n[Choice]: "))
      
    if choice == choice2:
      replit.clear()
      print(username1 + " and " + username2 + " Drew the game, both players recive a point") 
      p1Score += 1
      p2Score += 1
      multiEndScreen(p1Score, p2Score)
    if choice == 1 and choice2 == 2:
      print(username2 + " Won the game, Paper beats rock! " + username2 + " Recieves a point")

      p2Score += 1
      multiEndScreen(p1Score, p2Score)
    elif choice == 2 and choice2 == 3:
      print(username2 + " Won the game, Scissors beats paper! " + username2 + " Recieves a point")

      p2Score += 1
      multiEndScreen(p1Score, p2Score)
    elif choice == 3 and choice2 == 1:
      print(username2 + " Won the game, Rock beats scissors! " + username2 + " Recieves a point")

      p2Score += 1
      multiEndScreen(p1Score, p2Score)
    elif choice == 2 and choice2 == 1:
      print(username1 + " Won the game, Paper beats Rock! " + username1 + " Recieves a point")
    
      p1Score += 1
      multiEndScreen(p1Score, p2Score)
    elif choice == 3 and choice2 == 2:
      print(username1 + " Won the game, Scissors beats Paper! " + username1 + " Recieves a point")
    
      p1Score += 1
      multiEndScreen(p1Score, p2Score)
    elif choice == 1 and choice2 == 3:
      print(username1 + " Won the game, Rock beats Scissors! " + username1 + " Recieves a point")
    
      p1Score += 1
      multiEndScreen(p1Score, p2Score)
      
def multiEndScreen(p1Score, p2Score):
  wait(5)
  replit.clear()
  print("Score:\n\nComputer[", p1Score, "]\n\nPlayer[", p2Score, "]\n\n")
  again = int(input("Would you like to play again:\n[1] Yes\n[2] No\n[Choice]: "))
  if again == 1:
    replit.clear()
    playerMode()
  else:
    if p1Score == p2Score:
      print(username1 + " and " + username2 + " drew in the game, you are both equal on points")
    elif p1Score > p2Score:
      print(username1 + " won the game, " + username1 + " has the most points")
    elif p1Score < p2Score:
      print(username2 + " won the game, " + username2 + " has the most points")
    else:
      print("ERROR: CALCULATING GAME RESULTS")
def endScreen(Winner, PC_Point, PlayerPoint):
  wait(5)
  replit.clear()
  print("Score:\n\nComputer[", PC_Point, "]\n\nPlayer[", PlayerPoint, "]\n\n")
  again = int(input("Would you like to play again:\n[1] Yes\n[2] No\n[Choice]: "))
  if again == 1:
    replit.clear()
    computer()
  else:
    if PC_Point == PlayerPoint:
      print("You and the computer drew in the game, you are both equal on points")
    elif PC_Point > PlayerPoint:
      print("The computer won the game, the computer had more points than you")
    elif PC_Point < PlayerPoint:
      print("You won the game, you have the most points")
    else:
      print("ERROR: CALCULATING GAME RESULTS")
Begin()