import random

high_score = 0

def dice_game():
    global high_score
    while True:
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = (input("Enter your choice: "))
        print("\n")
        if choice == "1" or choice == "Roll Dice":
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            print(f"You roll a...", a)
            print(f"You roll a...", b)
            print("\n")
            new_score = a + b
            print(f"You have rolled a total of: ", new_score)
            if new_score > high_score:
                high_score = new_score
                print("New High Score!\n")
        if choice == "2" or choice == "Leave Game":
            print("Goodbye!")
            break

dice_game()
