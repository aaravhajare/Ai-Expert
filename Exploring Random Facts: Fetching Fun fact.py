import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"


def get_random_fact() :

    response = requests.get(url) 

    if response.status_code == 200 :

        fact_df = response.json()
        print(f"did you know {fact_df['text']} \n")

    else :
        print("Failed to fetch Api")


while True :

    inp = input("press enter to get a random fact about tech : ")

    if inp == "exit" or "quit" :
        break

    get_random_fact()