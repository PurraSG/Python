print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()

dictionary = {}

def prettyPrint():
  print()
  print(f"{'NAME':^12}{'TYPE':^15}{'HP':^4}{'MP':^6}")
  for key, value in dictionary.items():
    print(f"""{key:^12}|{value["type"]:^12}|{value["HP"]:^6}|{value["MP"]:^6}""")
    print()
      

while True:
  name = input("Input your beast's name: ").strip().title()
  type = input("Input your beast's type: ").strip().title()
  move = input("Input your beast's special move: ").strip().title()
  HP = input("Input your beast's staring HP: ").strip()
  MP = input("Input your beast's staring MP: ").strip()
  print("_______________")
  print()
  
  dictionary[name] = {"type": type, "move": move, "HP": HP, "MP":MP}
  
  prettyPrint()
  print()
  
  
  more = input("Would you like to add another?  ")
  if more == "yes":
    print()
    continue
  else:
    print("Bye!")
    break

