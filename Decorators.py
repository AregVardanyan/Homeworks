import json
import time

with open('Game1.json', 'w') as g1:
    json.dump({'John': '123', "Mike": '1234', "Jim": '12345'}, g1, indent=1)

with open('Game2.json', 'w') as g1:
    json.dump({'John': '123', "Mike": '1234', "Jim": '12345'}, g1, indent=1)


def login(func: callable, platform) -> callable:

    def check():
        print(f"Opening {platform}...")
        time.sleep(1)

        with open(f"{platform}.json") as g:
            data = json.load(g)
            username = input("Username :")

            for i in range(3):
                print("Checking...")
                time.sleep(1)

                if username in data:
                    break
                username = input("Can't find user. Write again :")

            else:
                print("Authentication failed")
                return

            password = input(f"Password for user {username}:")

            for i in range(3):
                print("Checking...")
                time.sleep(1)

                if password == data[username]:
                    break
                password = input(f"Wrong password for user {username}:")

            else:
                print("Authentication failed")
                return

            print("Authentication success")
            time.sleep(0.5)

            print(f"Running {func.__name__}...")
            func()

    return check


def enter():
    print("Welcome to the game")


enter = login(enter, "Game1")

enter()
