import random, time, os

f=open("my.ideas", "a+")

while True:
  print("IDEA STORAGE SYSTEM 📜")
  print()
  choice = input("Would you like to add ('a') an idea or load ('r') a random idea? ")
  print()
  
  if choice == "a":
    f=open("my.ideas", "a")
    aIdea = input("Add your idea here: > ")
    f.write(f"{aIdea}\n")
    print("Your idea has been stored")
  
  elif choice == "r":
    f.seek(0)
    rIdea = f.readlines()
    if rIdea:
      random_idea = random.choice(rIdea)
      print(f"Random idea: {random_idea}")
      time.sleep(4)
      os.system("clear")
    
f.close()