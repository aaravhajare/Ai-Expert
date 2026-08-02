import re
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ----------------------------
# Data
# ----------------------------
destinations = {
    "beach": ["Goa", "Dapoli", "Diveagar"],
    "mountain": ["Mount Everest", "Mount Alps"],
    "cities": ["Pune", "Mumbai", "Delhi"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# ----------------------------
# Helper Function
# ----------------------------
def normalize(inp):
    return re.sub(r"\s+", " ", inp.strip().lower())

# ----------------------------
# Recommendation Function
# ----------------------------
def recommend():
    print(Fore.CYAN + "\nTravel Bot: Choose a destination type:")
    print(Fore.GREEN + "• beach")
    print(Fore.GREEN + "• mountain")
    print(Fore.GREEN + "• cities")

    preference = input(Fore.YELLOW + "You: ")
    preference = normalize(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])

        print(Fore.CYAN + f"Travel Bot: How about {suggestion}?")

        print(Fore.CYAN + "Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"Travel Bot: Awesome! Enjoy your trip to {suggestion}!")

        elif answer == "no":
            print(Fore.MAGENTA + "Travel Bot: No problem! Let's try another destination.")
            recommend()

        else:
            print(Fore.RED + "Travel Bot: Please answer with yes or no.")
            recommend()

    else:
        print(Fore.RED + "Travel Bot: Sorry, I don't have that destination category.")
        recommend()

# ----------------------------
# Packing Tips
# ----------------------------
def packingtips():
    print(Fore.CYAN + "\nTravel Bot: Where are you going?")
    location = normalize(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "Travel Bot: How many days will you stay?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"\nPacking Tips for {location.title()} ({days} days)")
    print(Fore.GREEN + "✔ Pack versatile clothes.")
    print(Fore.GREEN + "✔ Bring chargers and adapters.")
    print(Fore.GREEN + "✔ Check the weather forecast.")
    print(Fore.GREEN + "✔ Carry medicines if needed.")
    print(Fore.GREEN + "✔ Keep your ID and tickets safely.")

# ----------------------------
# Joke
# ----------------------------
def tell_joke():
    print(Fore.MAGENTA + "\nTravel Bot: " + random.choice(jokes))

# ----------------------------
# Help Menu
# ----------------------------
def show_help():
    print(Fore.CYAN + "\n========== HELP ==========")
    print(Fore.GREEN + "recommend / suggest  -> Get a travel recommendation")
    print(Fore.GREEN + "pack / packing       -> Packing tips")
    print(Fore.GREEN + "joke / funny         -> Hear a travel joke")
    print(Fore.GREEN + "help                 -> Show commands")
    print(Fore.GREEN + "exit / bye           -> Exit the chatbot")
    print(Fore.CYAN + "==========================")

# ----------------------------
# Main Chat
# ----------------------------
def chat():
    print(Fore.CYAN + Style.BRIGHT + "🌍 Welcome to TravelBot!")

    name = input(Fore.YELLOW + "Your name: ")

    print(Fore.GREEN + f"\nNice to meet you, {name}!")
    print(Fore.CYAN + "Type 'help' to see available commands.\n")

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()

        elif "pack" in user_input or "packing" in user_input:
            packingtips()

        elif "joke" in user_input or "funny" in user_input:
            tell_joke()

        elif "help" in user_input:
            show_help()

        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "\nTravel Bot: Safe travels! Goodbye! 👋")
            break

        else:
            print(Fore.RED + "Travel Bot: I didn't understand that.")
            print(Fore.YELLOW + "Type 'help' to see available commands.")

# ----------------------------
# Run Program
# ----------------------------
chat()