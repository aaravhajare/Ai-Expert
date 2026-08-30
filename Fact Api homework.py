import requests

url = "https://useless.dotenv.dev/api/random?category={category}"

def get_random_fact() :

    response = requests.get(url) 

    if response.status_code == 200 :

        fact_df = response.json() 

        print(f"The fact is : {fact_df['text']}" )

    else : print("failed to fetch API")

categories = [
    "animal",
    "human",
    "space",
    "geography",
    "food",
    "sports",
    "language",
    "media",
    "things"
]

while True :

    global category = input("Enter the category from below : " , categories)
    
    inp = input("Press any key to get a random fact ")

    if inp == "exit" or inp == "quit" :
        break

    get_random_fact()