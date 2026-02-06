# TermEscape - A simple terminal escape game
# Run with: python termescape.py

def intro():
    print("=" * 40)
    print("🖥️  WELCOME TO TERMESCAPE")
    print("=" * 40)
    print("You are trapped in a mysterious terminal.")
    print("Find the correct commands and escape!\n")


def room_one():
    print("\n📍 Room 1: Locked Terminal")
    print("A screen shows: 'Type the correct command to continue'")
    print("Hint: command to list files")

    while True:
        cmd = input(">>> ").strip().lower()
        if cmd == "ls":
            print("✔ Files found: key.txt")
            print("You picked up the key.\n")
            return True
        else:
            print("❌ Wrong command. Try again.")


def room_two():
    print("\n📍 Room 2: Password Gate")
    print("A file says: 'What is 7 * 6 ?'")

    while True:
        answer = input("Enter password: ").strip()
        if answer == "42":
            print("✔ Password accepted.\n")
            return True
        else:
            print("❌ Incorrect password.")


def room_three():
    print("\n📍 Room 3: Final Exit")
    print("Type the command to exit the terminal.")
    print("Hint: used to leave programs")

    while True:
        cmd = input(">>> ").strip().lower()
        if cmd in ["exit", "quit"]:
            print("\n🎉 CONGRATULATIONS!")
            print("You escaped the terminal successfully 🚀")
            return
        else:
            print("❌ That didn’t work.")


def main():
    intro()
    if room_one():
        if room_two():
            room_three()


if __name__ == "__main__":
    main()
