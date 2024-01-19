import os, time

myList = []

def printList():
  print()
  for row in myList:
    for item in row:
      print(f"{item:^10}", end =" | ")
    print()    
      

while True:
  print("\033[1mTO DO LIST 🙋‍♀️📜 \033[0m")
  print()
  print("Do you want to:")
  action = input("1. VIEW\n2. ADD\n3. EDIT\n4. REMOVE ITEM\n5. ERASE LIST\n:") 
  print()
  if action == "1":
    option = input("Would you like to view all tasks or view a certain priority?: ")
    if option == "all":
      printList()
    else:
      whichPriority = input("Which priority would you like to view?: ")
      for row in myList:
        if whichPriority in row:
          for item in row:
            print(item, end=" | ")
      
  elif action == "2":
    item = input("What would you like to add to your list?: ")
    when = input("When is it due by?: ")
    priority = input("What's the priority?: ")
    row = [item, when, priority]
    myList.append(row)
    print()
  elif action == "4":
    item = input("What task have you finished and want to remove? :")
    for row in myList:      
      if item in row:
          myList.remove(row)      
      else:
        print(f"{item} was not in the list")
  elif action == "3":
    printList()
    item = input("Which task would you like to replace? : ")
    newItem = input("What would you like to replace it with? : ")
    item = input("What would you like to add to your list?: ")
    when = input("When is it due by?: ")
    priority = input("What's the priority?: ")
    row = [item, when, priority]
    myList.append(row)
    print()
  elif action == "5":
    myList = []
    
  time.sleep(2)
  os.system("clear")
  print()
  