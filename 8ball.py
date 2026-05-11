import random
import time

# Predefined list of possible 8-ball responses.
answers = ["It is certain", "It is decidely so", "Without a doubt", "Yes Definitely", "You may rely on it", "As I see it, yes", "Most Likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot Predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
# Print the ASCII art with short pauses to simulate a "loading" animation.
print("  .-'''-.")
time.sleep(.5)
print(" /   _   \\")
time.sleep(.5)
print(" |  (8)  |")
time.sleep(.5)
print(" \\   ^   /")
time.sleep(.5)
print("  '-...-'")

def ask_the_ball():
    # Collect the user's name and question, then format them for display.
    name = input("What is your name? ")
    cap_name = name.upper()
    question = input("What is your question? ")
    cap_question = question.upper()
    # Pick a random response from the answers list.
    answer = random.choice(answers)

    # Echo back the question, then reveal the answer after a brief "thinking" pause.
    print(f"{cap_name}, you asked '{cap_question}'.")
    print("Pondering the Orb")
    print("🔮 ✨ 🔮")
    time.sleep(random.randint(1, 5))
    print(f"{answer}")
    # Ask whether the user wants to continue and hand off to play_again.
    ask_again = input("Would you like to ask again? yes/no ")
    play_again(ask_again)

def play_again(user_answer):
    # Normalize the input so users can type yes/no in any case.
    more = user_answer.upper()
    if more == "YES":
        # Restart the question flow.
        ask_the_ball()
    elif more == "NO":
        # End the program politely.
        print("Thank you for playing.")
        exit()
    else:
        # If input is invalid, ask again and recurse.
        wrong = input("Please type 'yes' or 'no'. ")
        play_again(wrong)
        
# Start the game immediately when the script is run.
ask_the_ball()
