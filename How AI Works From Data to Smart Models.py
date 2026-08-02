import colorama
from colorama import Fore , Style 
from textblob import TextBlob

colorma.init()

print(f"{Fore.cyan} Welcome to sentiment spy {Style.reset_all}")

user_name = input("Enter user name")

if not user_name :
    user_name = "Mystery agent"

conversation_history = []

print(f"Hello Agent {user_name}")

while True :
    user_inp = input()

    if not user_inp :
        print("Please enter a valid command")
        continue

    if user_inp == "exit" :
        print("Agent exiting ")
        break

    elif user_inp == "history" :

        if not conversation_history :
            print("NO conversation history yet")

        else :
            print("Convversation HIstory :")

            for idx , (text , polarity , sentiment_type) in enumerate ( conversation_history , start=1) :

                if sentiment_type == "POsitive" :
                    print("positive")

                elif sentiment_type == "NEutral" :
                    print("nutral")

                else : 
                    print("Negetive")
    
    polarity = TextBlob(user_inp).sentiment.polarity

    if polarity > 0.25:

        sentiment_type = "Positive"

        color = Fore.GREEN

        emoji = "????"

    elif polarity < -0.25:

        sentiment_type = "Negative"

        color = Fore.RED

        emoji = "????"

    else:
        sentiment_type = "Neutral"

        color = Fore.YELLOW

        emoji = "????"