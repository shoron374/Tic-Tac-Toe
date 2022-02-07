board_data = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

active_player = "O"


def board_print(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")


def quit_check(player_input):
    if player_input.lower() == "q":
        print("Thanks for playing!")
        quit()


def valid_player_input(player_input):
    valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if player_input not in valid_numbers:
        print("invalid input. Try again.")
        return False
    else:
        switch_player()
        return True


def board_update(board, player_input):
    if board[int(player_input)-1] == "-":
        board[int(player_input)-1] = active_player
    else:
        print("Oops, This slot is already taken!")
        switch_player()


def switch_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"


def check_horizontal(board):
    global active_player
    if board[0] == board[1] == board[2] == active_player: return True
    if board[3] == board[4] == board[5] == active_player: return True
    if board[6] == board[7] == board[8] == active_player: return True
    else: return False


def check_vertical(board):
    global active_player
    if board[0] == board[3] == board[6] == active_player: return True
    if board[1] == board[4] == board[7] == active_player: return True
    if board[2] == board[5] == board[8] == active_player: return True
    else: return False


def check_diagonal(board):
    global active_player
    if board[0] == board[4] == board[8] == active_player: return True
    if board[2] == board[4] == board[6] == active_player: return True
    else: return False


def game_winning(board):
    global active_player
    if check_vertical(board) or check_horizontal(board) or check_diagonal(board):
        return True
    else:
        return False


def game_draw(board):
    if "-" not in board:
        return True
    else:
        return False


def game_outcome(board):
    global active_player
    if game_winning(board):
        print(f"Congratulations! \"{active_player}\" won the game!")
        return True
    elif game_draw(board):
        print("Sorry its a draw!")
        return True
    else:
        return False


def game_outcome_condition(board):
    global active_player
    if game_winning(board):
        return True
    elif game_draw(board):
        return True
    else:
        return False


def refresh_board(board):
    index = 0
    while 0 <= index < 9:
        board[index] = "-"
        index += 1


def final_input():
    end_input = input("Do want to play again? (y/n): ")
    if end_input.lower() == "y":
        refresh_board(board_data)
        main()
    elif end_input.lower() == "n":
        quit()
    else:
        print("Invalid input!")
        final_input()


def main():
    while True:
        print("*" * 30)
        board_print(board_data)
        player_input_data = input("Type 1-9 and \"q\" to quit: ")
        quit_check(player_input_data)
        if not valid_player_input(player_input_data):
            continue
        board_update(board_data, player_input_data)
        game_outcome(board_data)
        if game_outcome_condition(board_data):
            board_print(board_data)
            final_input()


main()
