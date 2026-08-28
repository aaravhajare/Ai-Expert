import requests
import random
import html
import time
import msvcrt


# -------------------------------
# QUIZ SETTINGS
# -------------------------------

CATEGORIES = {
    "1": (9, "General Knowledge"),
    "2": (17, "Science & Nature"),
    "3": (21, "Sports")
}

QUESTIONS_PER_QUIZ = 10
TIME_PER_QUESTION = 10


# -------------------------------
# GET QUESTIONS FROM API
# -------------------------------

def get_questions(category_id):

    api_url = (
        f"https://opentdb.com/api.php?"
        f"amount={QUESTIONS_PER_QUIZ}"
        f"&category={category_id}"
        f"&type=multiple"
    )

    try:
        response = requests.get(api_url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            if data["response_code"] == 0 and data["results"]:
                return data["results"]

    except requests.RequestException:
        pass

    return None


# -------------------------------
# TIMER INPUT
# -------------------------------

def timed_input(prompt, time_limit):

    print(prompt, end="", flush=True)

    start_time = time.time()
    user_input = ""

    while True:

        elapsed = time.time() - start_time

        # Time is over
        if elapsed >= time_limit:
            print("\n\n⏰ Time's up!")
            return None

        # Check if user pressed a key
        if msvcrt.kbhit():

            char = msvcrt.getwch()

            # Enter key
            if char == "\r":

                print()
                return user_input

            # Backspace
            elif char == "\b":

                if user_input:
                    user_input = user_input[:-1]
                    print("\b \b", end="", flush=True)

            # Normal key
            else:

                user_input += char
                print(char, end="", flush=True)

        # Show remaining time
        remaining = int(time_limit - elapsed)

        print(
            f"\r{prompt}{user_input}   "
            f"[Time: {remaining}s]",
            end="",
            flush=True
        )

        time.sleep(0.05)


# -------------------------------
# CATEGORY SELECTION
# -------------------------------

def choose_category():

    print("\n==============================")
    print("       CHOOSE CATEGORY")
    print("==============================")

    print("1. General Knowledge")
    print("2. Science & Nature")
    print("3. Sports")

    while True:

        choice = input("\nEnter your choice (1-3): ")

        if choice in CATEGORIES:
            return CATEGORIES[choice]

        print("❌ Invalid input! Please enter 1, 2, or 3.")


# -------------------------------
# RUN QUIZ
# -------------------------------

def run_quiz():

    print("\n================================")
    print("       🧠 TRIVIA QUIZ")
    print("================================")

    print(f"You have {TIME_PER_QUESTION} seconds for each question.")

    category_id, category_name = choose_category()

    print(f"\nFetching {category_name} questions...")

    questions_list = get_questions(category_id)

    if not questions_list:

        print("\n❌ Failed to fetch questions.")
        print("Please check your internet connection.")
        return

    score = 0

    print("\n================================")
    print("         QUIZ STARTS!")
    print("================================")

    for i, q in enumerate(questions_list, 1):

        question_text = html.unescape(q["question"])

        correct = html.unescape(q["correct_answer"])

        incorrects = [
            html.unescape(answer)
            for answer in q["incorrect_answers"]
        ]

        options = incorrects + [correct]

        random.shuffle(options)

        print("\n--------------------------------")
        print(f"Question {i} / {len(questions_list)}")
        print(f"Category: {category_name}")
        print("--------------------------------")

        print(question_text)

        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        # -------------------------------
        # GET ANSWER WITH TIMER
        # -------------------------------

        while True:

            choice = timed_input(
                "\nEnter your answer (1-4): ",
                TIME_PER_QUESTION
            )

            # Time ran out
            if choice is None:

                print(f"The correct answer was: {correct}")
                break

            # Check whether input is a number
            try:
                choice = int(choice)

            except ValueError:

                print(
                    "❌ Invalid input! "
                    "Please enter a number between 1 and 4."
                )

                continue

            # Check range
            if choice < 1 or choice > 4:

                print(
                    "❌ Invalid input! "
                    "Please enter a number between 1 and 4."
                )

                continue

            # Valid answer
            if options[choice - 1] == correct:

                print("✅ Correct!")
                score += 1

            else:

                print("❌ Wrong!")
                print(f"The correct answer was: {correct}")

            break

    # -------------------------------
    # FINAL SCORE
    # -------------------------------

    percentage = (score / len(questions_list)) * 100

    print("\n================================")
    print("          QUIZ COMPLETE!")
    print("================================")

    print(f"Category : {category_name}")
    print(f"Score    : {score} / {len(questions_list)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("🏆 Perfect Score!")

    elif percentage >= 80:
        print("🔥 Excellent!")

    elif percentage >= 60:
        print("👍 Good Job!")

    elif percentage >= 40:
        print("🙂 Keep Practicing!")

    else:
        print("📚 Keep Learning!")

    print("================================")


# -------------------------------
# START PROGRAM
# -------------------------------

if __name__ == "__main__":
    run_quiz()