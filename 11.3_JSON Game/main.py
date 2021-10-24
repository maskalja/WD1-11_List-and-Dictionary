import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
wg = []


with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    highsc_list = sorted(score_list, key=lambda d: d["attempts"]) #sorts the dictionaries in the list according to the "attempts" key
    for score_dict in highsc_list[:3]:
        print("Player: " + score_dict["name"], "| Attempts: " + str(score_dict["attempts"]), "| Secret number: "+ str(score_dict["secret"]), "| Date: " + score_dict["date"], "| Wrong guesses: " + str(score_dict["wrong_guesses"]))

name = input("Enter player's name? ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()), "secret": secret, "wrong_guesses": wg})
        with open("score_list.json", "w") as score_file:
            score_list = score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        wg.append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        wg.append(guess)
        print("Your guess is not correct... try something bigger")