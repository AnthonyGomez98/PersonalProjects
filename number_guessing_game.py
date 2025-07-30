import random

def select_difficulty():
    print("\n🎮 Select Difficulty:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–500)")
    print("4. Hardcore Mode (1–100, one guess only)")
    
    while True:
        choice = input("Enter 1, 2, 3, or 4: ").strip()
        if choice == "1":
            return 1, 50, False
        elif choice == "2":
            return 1, 100, False
        elif choice == "3":
            return 1, 500, False
        elif choice == "4":
            return 1, 100, True
        else:
            print("❌ Invalid selection. Please try again.")

def give_hint(secret_number):
    if secret_number % 2 == 0:
        return "Hint: It's an even number."
    elif secret_number % 5 == 0:
        return "Hint: It's divisible by 5."
    elif secret_number in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        return "Hint: It's a prime number."
    else:
        return f"Hint: It's greater than {secret_number - random.randint(3, 10)}."

def play_again():
    return input("\nPlay again? (y/n): ").lower().startswith("y")

def number_guessing_game():
    """Plays a number guessing game with difficulty, hints, and hardcore mode—fully self-contained."""
    
    print("🎯 Welcome to the Number Guessing Game!")
    session_high_score = None

    while True:
        low, high, is_hardcore = select_difficulty()
        secret_number = random.randint(low, high)
        attempts = 0

        print(f"\nI'm thinking of a number between {low} and {high}.")
        if is_hardcore:
            print("💀 Hardcore Mode Activated: Only ONE guess allowed!")

        while True:
            try:
                guess = int(input("Take a guess: "))
                attempts += 1
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
                continue

            if guess == secret_number:
                print(f"✅ You got it in {attempts} attempt(s)!")
                if not is_hardcore:
                    if session_high_score is None or attempts < session_high_score:
                        session_high_score = attempts
                        print("🏆 New Session High Score!")
                    else:
                        print(f"🎯 Current Session High Score: {session_high_score} attempt(s)")
                break
            else:
                if is_hardcore:
                    print(f"💥 Wrong guess! The number was {secret_number}. Game Over.")
                    break
                if guess < secret_number:
                    print("📉 Too low!")
                else:
                    print("📈 Too high!")
                if attempts % 5 == 0:
                    print(give_hint(secret_number))

        if not play_again():
            print("\n👋 Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    number_guessing_game()

