import requests
import random
import html


Education_category_id = 9 #GK

Api_url = f"https://opentdb.com/api.php?amount=10&category={Education_category_id}&type=multiple"


def get_questions() :

    response = requests.get(Api_url)

    if response.status_code == 200 :

        data = response.json()

        if data["response_code"] == 0 and data["results"] :

            return data["results"]

    return None


def run_quiz() :

    questions_list = get_questions()

    if not questions_list :

        print("Failed to fetch questions")

        return


    score = 0

    print("Welcome to the quiz")

    for i , q in enumerate(questions_list , 1) :

        question_text = html.unescape(q["question"])

        correct = html.unescape(q["correct_answer"])

        incorrects = [html.unescape(a) for a in q["incorrect_answers"]]


        options = incorrects + [correct]

        random.shuffle(options)



        print(f"Question {i} : {question_text}")

        for idx , option in enumerate(options , 1) :

            print(f" {idx} . {option}")



        while True :

            try :

                choice = int(input("Enter Your answer (1-4):"))

                if 1<= choice <= len(options) :

                    break

                else:

                    print("Invalid input. Please enter a number between 1 and 4.")

            except ValueError :

                print("Invalid input. Please enter a number.")


        if options[choice - 1] == correct :

            print("Correct! \n")

            score += 1

        else :

            print(f"Wrong. The correct answer is : {correct} \n")

    print(f"Final Score is : {score} / {len(questions_list)}")

    print(f"Percentage is : {score / len(questions_list)*100:.1f}%")

if __name__ == "__main__" :

    run_quiz()
