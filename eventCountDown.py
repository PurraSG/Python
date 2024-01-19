import datetime

today = datetime.date.today()

print("EVENT COUNTDOWN TIMER")
print()
thing = input("Input the event: ").strip().capitalize()
print()
year = int(input("Input the year: "))
month = int(input("Input the month: "))
day = int(input("Input the day: "))
print()

event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference == 0:
  print(thing,"is today 🥳 🥳 🥳 ")
elif difference > 0:
  print(thing, "is coming in", difference, "days")
else:
  print(thing, "happened", difference, "days ago 😭 😭 😭")