import requests
import os
import time
from replit import db

def loadJoke(jokeId):
    joke_url = f"https://icanhazdadjoke.com/j/{jokeId}"
    result = requests.get(joke_url, headers={"Accept": "application/json"})
    if result.status_code == 200:
        loaded_joke_data = result.json()
        loaded_joke = loaded_joke_data["joke"]
        print()
        print(loaded_joke)
        print()
    else:
        print("Sorry, an error occurred")

while True:
    print("RANDOM DAD JOKES 😄")
    print()
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    jokeData = result.json()
    joke = jokeData["joke"]
    jokeId = jokeData["id"]

    answer = input("Would you like to:\n1 See a dad joke\n2 Load a saved dad joke\n> ")

    if answer == "1":
        print()
        print(joke)
        print()
        save = input("Would you like to save the joke?\n> ")
        print()
        if save.lower() == "yes":
            db[joke] = jokeId  # Save the joke text as the key and the jokeId as the value
            time.sleep(2)
            os.system("clear")
        else:
            continue
    elif answer == "2":
        saved_jokes = db.prefix("")
        if saved_jokes:
            print("Loading saved jokes...")
            for key in saved_jokes:
                joke_text = key
                joke_id = db[key]
                loadJoke(joke_id)  # Pass the correct joke_id to the loadJoke function
        
        else:
            print("No saved jokes found.")
        time.sleep(4)
        os.system("clear")
