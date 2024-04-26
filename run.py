import os

def instructions():
    print("Game Instructions:")
    print("The game is played by 2 Players and on a 3x3 board.")
    print("Players take turns marking a field with their symbol ('X' or 'O').")
    print("The first player who matches three of their symbols in a row, column, or diagonal wins.")
    print("If all fields are filled and no player has won, the game ends in a tie.")

# Initial screen with options for player


def start_game():
    print("===============================\n")
    print("  Welcome to Tic Tac Toe Game  \n")
    print("===============================\n")
    print("Hello!\n")
    while True:
        print("Choose an option:\n")
        print("1. Instructions\n")
        print("2. Start the Game\n")
        print("3. Quit\n")
        option = input("Enter your option: \n")
        if option == "1":
            instructions()
        elif option == "2":
            main()
            play_again()    
        elif option == "3":
            print("Bye!\n")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.\n")

# Enters Username and displays a message if no valid username is entered


def valid_username(username):
    if len(username) < 2 or len(username) > 10:
        return False
    if not username.isalpha():
        return False
    return True

def user_names():
    print("Ready to Play?\n")
    while True:
        username1 = input("Enter username - Player 1 (X): \n")
        if valid_username(username1):
            break
        else:
            print("Invalid input. Username must be between 2 and 10 letters only.\n")

    while True:
        username2 = input("Enter username - Player 2 (O): \n")
        if valid_username(username2):
            break
        else:
            print("Invalid input. Username must be between 2 and 10 letters only.\n")

    return username1, username2


def game(board):
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("--------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("--------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])


# Function to check the winner
def check_winner(board, player):
    # Define the winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Vertical
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Horizontal
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check each winning condition
    for combination in win_combinations:
        if all(board[pos] == player for pos in combination):
            return True
    return False


# 'pos' is used to iterate over all the positions of the cells

def check_tie(board):
    return all(pos != "1" and pos != "2" and pos != "3" and
               pos != "4" and pos != "5" and pos != "6" and
               pos != "7" and pos != "8" and pos != "9" for pos in board)

# Function to check if player input is valid


def player_input(board, player_name, player_symbol):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        game(board)
        try:
            inp = int(input(f'{player_name}, enter a number from 1 to 9: \n'))
            if 1 <= inp <= 9 and board[inp - 1] not in ["X", "O"]:
                board[inp - 1] = player_symbol
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.\n")
        else:
            print("This place is already taken or number not in range.\n")


# Main game logic


def main():
    username1, username2 = user_names()
    current_player = "X"
    winner = None
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    game(board)  # Displays the initial board
    while True:
        player_input(board, username1 if current_player == "X" else
                     username2, current_player)
        if check_winner(board, current_player):
            winner = current_player
            break
        elif check_tie(board):
            break
        current_player = "O" if current_player == "X" else "X"

    game(board)  # Display the final board
    if winner:
        print(f"Congratulations,{username1 if winner == 'X'else username2}!\n")
        print("You win!\n")
    else:
        print("It's a tie!\n")


def play_again():
    while True:
        play_again = input("Do you want to play again? (y/n):\n").lower()
        if play_again == "y":
            main()
        elif play_again == "n":
            print("Thanks for playing!\n")
            exit()
        else:
            print("Please enter 'y' to play again or 'n' to quit.\n")

if __name__ == "__main__":
    start_game()




















