import random
from colorama import init, Style, Fore

init(autoreset=True)


def display_board(board):
    print()

    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL

        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL

        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(" " + colored(board[0]) + " | " + colored(board[1]) + " | " + colored(board[2]))
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(" " + colored(board[3]) + " | " + colored(board[4]) + " | " + colored(board[5]))
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(" " + colored(board[6]) + " | " + colored(board[7]) + " | " + colored(board[8]))
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print()


def player_choice():
    symbol = " "

    while symbol not in ["X", "O"]:
        symbol = input(
            Fore.GREEN +
            "Do you want to be X or O: " +
            Style.RESET_ALL
        ).upper()

    if symbol == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def player_move(board, symbol):
    move = -1

    while move not in range(1, 10) or not board[move - 1].isdigit():

        try:
            move = int(input(
                Fore.GREEN +
                "Enter your move from 1-9: " +
                Style.RESET_ALL
            ))

            if move not in range(1, 10):
                print(Fore.RED + "Invalid move! Please enter 1-9.")

            elif not board[move - 1].isdigit():
                print(Fore.RED + "That position is already taken!")

        except ValueError:
            print(
                Fore.RED +
                "Please enter a number between 1-9."
            )

    board[move - 1] = symbol


def ai_move(board, ai_symbol, player_symbol):

    # 1. Try to win
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol

            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return

    # 2. Block the player
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol

            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return

    # 3. Take the center
    if board[4].isdigit():
        board[4] = ai_symbol
        return

    # 4. Take a random available position
    possible_moves = [i for i in range(9) if board[i].isdigit()]

    if possible_moves:
        move = random.choice(possible_moves)
        board[move] = ai_symbol


def check_win(board, symbol):

    win_conditions = [
        (0, 1, 2),  # Horizontal
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),  # Vertical
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),  # Diagonal
        (2, 4, 6)
    ]

    for condition in win_conditions:
        if (
            board[condition[0]]
            == board[condition[1]]
            == board[condition[2]]
            == symbol
        ):
            return True

    return False


def check_full_board(board):
    return all(not spot.isdigit() for spot in board)


def game():

    print(Fore.CYAN + Style.BRIGHT + "\n===== TIC TAC TOE =====\n")

    player_symbol, ai_symbol = player_choice()

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    print(
        Fore.YELLOW +
        f"\nYou are {player_symbol} and the computer is {ai_symbol}."
    )

    print("\nBoard positions:")
    display_board(board)

    # X always goes first
    current_symbol = "X"

    while True:

        # Player's turn
        if current_symbol == player_symbol:

            print(Fore.GREEN + "\nYour turn!")
            display_board(board)
            player_move(board, player_symbol)

            if check_win(board, player_symbol):
                display_board(board)
                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n🎉 Congratulations! You won!"
                )
                break

        # AI's turn
        else:

            print(Fore.MAGENTA + "\nComputer's turn...")
            ai_move(board, ai_symbol, player_symbol)

            if check_win(board, ai_symbol):
                display_board(board)
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\n💻 Computer wins! Better luck next time!"
                )
                break

        # Check for draw
        if check_full_board(board):
            display_board(board)
            print(
                Fore.YELLOW +
                Style.BRIGHT +
                "\n🤝 It's a draw!"
            )
            break

        # Switch turns
        if current_symbol == "X":
            current_symbol = "O"
        else:
            current_symbol = "X"


# Main program
while True:

    game()

    again = input(
        Fore.CYAN +
        "\nDo you want to play again? (y/n): " +
        Style.RESET_ALL
    ).lower()

    if again != "y":
        print(
            Fore.YELLOW +
            "\nThanks for playing Tic Tac Toe! 👋"
        )
        break