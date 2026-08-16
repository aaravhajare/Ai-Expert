import requests

def get_random_joke() :
    # Fetch a random joke from the server 

    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    if response.status_code == 200 :

        # print("Full json response : " , response.json)

        joke_data = response.json()

        return f"{joke_data["setup"]} - {joke_data["punchline"]}"

    else :
        return "FAiled to retrive data"


def main() :

    print("Welcome to random joke generator")


    while True :

        inp = input("type y to get a random joke and 1/exit to exit")

        if inp == "1" or inp == "exit" :
            print("Good Bye")
            break


        elif inp == "y":
            joke = get_random_joke()

            print("The joke is : \n" , joke)


if __name__ == "__main__" :
    main()