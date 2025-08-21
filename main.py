import random
import time
import sys

# Ask for name
name = input("What is your name? ")

# Welcome them
print("Welcome", name, "to Stephen's Casino!")
time.sleep(1)

# Give them money
money = 500
print("Enjoy 500 euro on the house.")
time.sleep(1)

# Pretend they received it
print("[You received 500 euro]")
time.sleep(1)

# Pretend they walked to the wheel
print("[You walk to the roulette wheel]")
time.sleep(1)

# Main Game Loop - they can keep playing as long as they have money
while money > 0:

    # Present options/status
    print("---------------------------------------")
    print(f"What will you do with your €{money}?")
    time.sleep(1)
    print("1 : Place a bet")
    print("2 : Cash out and go home")

    # Ask what they want to do INFINITE LOOP
    while True:
        try:
            choice = int(input("choice: "))
            if choice == 1 or choice == 2:
                break  # Break on valid input
        except:
            pass
        print("Invalid choice, try again")

    # If they choose to bet
    if choice == 1:
        # Get the amount to bet INFINITE LOOP
        while True:
            print("How much do you want to bet?")
            bet = int(input("€€€? "))
            if bet > money:
                print("You do not have enough to bet that!")
                time.sleep(1)
            else:
                print("OK")
                time.sleep(1)
                break
        # Roll the wheel
        while True:
            try:
                colour = input("Please select a colour, red or black? ").lower()
                if colour == "red" or colour == "r" or colour == "1" or colour == "b" or colour == "black" or colour == "2":
                    print("Spinning the wheel....")
                    time.sleep(3)
                    if random.randint(1, 37) <= 18:
                        print("YOU WON")
                        money += bet
                        break
                    else:
                        print("YOU LOSE")
                        money -= bet
                        break
            except:
                print("Invalid choice")
                time.sleep(1)

    # If they choose to go home
    if choice == 2:
        print(f"You go home with €{money}")
        time.sleep(1)
        break

# Exit
sys.exit()