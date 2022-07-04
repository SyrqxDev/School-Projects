import replit
import time
def clear():
  replit.clear()


def start():
  clear()
  print("[1] Write to the file")
  print("[2] Read from the file")
  print("[3] Clear the file")

  option = int(input("---> "))
  clear()
  
  if option == 1:
    data = input("What do you want to write to the file? \n --> ")
    with open("text.txt", "+a") as file:
      file.write(data+"\n")
      print("ADDED: " + data + " To the file")
      file.close()
      input("\nPress enter to return to menu\n")
      start()
  if option == 2:
    with open("text.txt", "r") as file:
      print(file.read())
      input("\nPress enter to return to menu\n")
      start()
  if option == 3:
    warning = input("ARE YOU SURE YOU WANT TO WIPE YOUR FILE: [YES] [NO]\n---> ")
    if warning == "YES":
      with open("text.txt", "w") as file:
        file.write("")
        print("FILE CLEARED")
        input("\nPress enter to return to menu\n")
        start()
    elif warning == "NO":
      print("so why clear the file noob")
      time.sleep(3)
      start()
    else:
      start()
  
start()