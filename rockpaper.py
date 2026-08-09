import random
from colorama import init, Style, Fore

init(autoreset=True)


def display_choices():
    print(Fore.CYAN + "\n===== ROCK PAPER SCISSORS =====")
    print(Fore.YELLOW + "1. Rock")
    print(Fore.YELLOW + "2. Paper")
    print(Fore.YELLOW + "3. Scissors")


def player_choice():
    while True:
        display_choices()

        try:
            choice = int(input(
                Fore.GREEN +
                "\nEnter your choice (1-3): " +
                Style.RESET_ALL
            ))

            if choice in range(1, 4):
                return choice

            else:
                print(
                    Fore.RED +
                    "Invalid choice! Please enter 1, 2, or 3."
                )

        except ValueError:
            print(
                Fore.RED +
                "Please enter a number between 1-3."
            )


def get_choice_name(choice):
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }

    return choices[choice]


def ai_choice():
    return random.randint(1, 3)


def check_winner(player, ai):

    if player == ai:
        return "draw"

    elif (
        (player == 1 and ai == 3) or
        (player == 2 and ai == 1) or
        (player == 3 and ai == 2)
    ):
        return "player"

    else:
        return "ai"


def display_result(player, ai, result):

    print(
        Fore.GREEN +
        "\nYou chose: " +
        Style.BRIGHT +
        get_choice_name(player)
    )

    print(
        Fore.MAGENTA +
        "Computer chose: " +
        Style.BRIGHT +
        get_choice_name(ai)
    )

    if result == "player":

        print(
            Fore.GREEN +
            Style.BRIGHT +
            "\n🎉 You win!"
        )

    elif result == "ai":

        print(
            Fore.RED +
            Style.BRIGHT +
            "\n💻 Computer wins!"
        )

    else:

        print(
            Fore.YELLOW +
            Style.BRIGHT +
            "\n🤝 It's a draw!"
        )


def game():

    player_score = 0
    ai_score = 0
    draws = 0

    print(
        Fore.CYAN +
        Style.BRIGHT +
        "\n===== ROCK PAPER SCISSORS ====="
    )

    while True:

        player = player_choice()
        ai = ai_choice()

        result = check_winner(player, ai)

        display_result(player, ai, result)

        # Update score
        if result == "player":
            player_score += 1

        elif result == "ai":
            ai_score += 1

        else:
            draws += 1

        # Display score
        print(
            Fore.CYAN +
            "\n===== SCORE ====="
        )

        print(
            Fore.GREEN +
            f"You: {player_score}"
        )

        print(
            Fore.RED +
            f"Computer: {ai_score}"
        )

        print(
            Fore.YELLOW +
            f"Draws: {draws}"
        )

        # Ask if player wants another round
        again = input(
            Fore.CYAN +
            "\nPlay another round? (y/n): " +
            Style.RESET_ALL
        ).lower()

        if again != "y":
            break

    print(
        Fore.CYAN +
        Style.BRIGHT +
        "\n===== FINAL SCORE ====="
    )

    print(Fore.GREEN + f"You: {player_score}")
    print(Fore.RED + f"Computer: {ai_score}")
    print(Fore.YELLOW + f"Draws: {draws}")

    if player_score > ai_score:

        print(
            Fore.GREEN +
            Style.BRIGHT +
            "\n🏆 You won the game!"
        )

    elif ai_score > player_score:

        print(
            Fore.RED +
            Style.BRIGHT +
            "\n💻 Computer won the game!"
        )

    else:

        print(
            Fore.YELLOW +
            Style.BRIGHT +
            "\n🤝 The game ended in a draw!"
        )


# Main program

while True:

    game()

    again = input(
        Fore.CYAN +
        "\nDo you want to start a new game? (y/n): " +
        Style.RESET_ALL
    ).lower()

    if again != "y":

        print(
            Fore.YELLOW +
            "\nThanks for playing! 👋"
        )

        break