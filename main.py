import re , random 
from colorama import Fore , init

init(autoreset=True)

destinations = {
    "beach": ["GOa" , "Dapoli" , "Diveagar" ],
    "mountain" : ["Mount Everest" , "Mount Apls" ],
    "cities" : ["Pune" ,  "Mumbai" , "Delhi"]
}

jokes = [
"Why don't programmers like nature? Too many bugs!",
"Why did the computer go to the doctor? Because it had a virus",
"Why do travelers always feel warm? Because of all their hot spots!"]

def normalize(inp) :
    return re.sub(r"\s+" , " " , inp.strip().lower())

def recommend() :

    preference = input("You :")
    preference = normalize(preference)

    if preference in destinations :
        suggestion = random.choice(destinations[preference])
        print(f"travel Bot : How about {suggestion}")

        print("Do You like it yes/no")

        answer = input().lower

        if answer == "Yes" :
            print("Travel bot : Nice enjoy" , suggestion)

        elif answer == "No" :
            print("Travel bot : Let's try another")
            recommend()
        else :
            print("Travel bot : I will suggest")
            recommend()
    else : 
        print("Travel bot : I don't have the destivnation")
        recommend()

def packingtips() :
    print("Travel bot : Where To")
    location = normalize(input("You: "))

    print("Travel bot : How many days")
    days = input("you : ")

    print("PAcking tips for " , days "are")
