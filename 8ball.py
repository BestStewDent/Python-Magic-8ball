import random
import time

answers = ["It is certain", "It is decidely so", "Without a doubt", "Yes Definitely", "You may rely on it", "As I see it, yes", "Most Likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot Predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
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
    name = input("What is your name? ")
    cap_name = name.upper()
    question = input("What is your question? ")
    cap_question = question.upper()
    get_the_i = random.randint(0, len(answers)-1)
    answer = answers[get_the_i]

    print(f"{cap_name}, you asked '{cap_question}'.")
    print("Pondering the Orb")
    print("🔮 ✨ 🔮")
    time.sleep(random.randint(1, 5))
    print(f"{answer}")
    ask_again = input("Would you like to ask again? yes/no ")
    play_again(ask_again)

def play_again(user_answer):
    more = user_answer.upper()
    if more == "YES":
        ask_the_ball()
    elif more == "NO":
        print("Thank you for playing.")
        exit()
    else:
        wrong = input("Please type 'yes' or 'no'. ")
        play_again(wrong)
        
ask_the_ball()
