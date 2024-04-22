import os

print ( "===============================")
print ( "  Welcome to Tic Tac Toe Game  ")
print ( "===============================")

# Enter Username and displays a message if no valid username is entered
def user_names():
    print("Hello! Ready to Play?")
    while True:
        username1 = input("Enter username - Player 1 (X): ")
        if username1:
            break
        else:
            print("Enter a valid username for Player 1.")

    while True:
        username2 = input("Enter username - Player 2 (O): ")
        if username2:
            break
        else:
            print("Enter a valid username for Player 2.")

    print(f"Welcome, {username1} and {username2}! Let's start!\n")
    return username1, username2

def game(board):
    print (board[0] + "  |  " + board[1] + "  |  " + board[2])
    print ("--------------")
    print (board[3] + "  |  " + board[4] + "  |  " + board[5])
    print ("--------------")
    print (board[6] + "  |  " + board[7] + "  |  " + board[8])


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


# 'pos' is used to iterate over all the positions of the cells on the game board to check if any cell is still empty

def check_tie(board):
    return all(pos != "1" and pos != "2" and pos != "3" and pos != "4" and pos != "5" and pos != "6" and pos != "7" and pos != "8" and pos != "9" for pos in board)

# Function to check if player input is valid
def player_input(board, player_name, player_symbol):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        game(board)
        move_x = input(f'{player_name}, enter a number from 1 to 9: ')
        if move_x.isdigit():
            move_x = int(move_x)
            if move_x >= 1 and move_x <= 9 and board[move_x-1] != "X" and board[move_x-1] != "O":
                board[move_x-1] = player_symbol
                break
            else:
                print("This place is already taken or the input is invalid")
        else:
            print("Invalid input. Please enter a number.")
    

# Main game logic
def main():
    username1, username2 = user_names()
    current_player = "X"
    winner = None
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    
    game(board)  # Display the initial board
    while True:
        player_input(board, username1 if current_player == "X" else username2, current_player)
        if check_winner(board, current_player):
            winner = current_player
            break
        elif check_tie(board):
            break
        current_player = "O" if current_player == "X" else "X"

    game(board)  # Display the final board
    if winner:
        print(f"Congratulations, {username1 if winner == 'X' else username2}! You win!")
    else:
        print("It's a tie!")
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")

 # Checks if the script is being run directly, it calls the main() function, which is the main logic of the game
if __name__ == "__main__":
    main()



















