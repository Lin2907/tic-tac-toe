import os

# Enter Username
def user_names():
    print("Hi there! Ready to Play?")
    username1 = input("Enter username for Player 1 (X): ")
    username2 = input("Enter username for Player 2 (O): ")
    print(f"Welcome, {username1} and {username2}! Let's start!\n")
    return username1, username2

user_names()

# Define current player

current_player = "X"
game_play = True
winner = None


#Drawing a game board using array and index
board =["1" , "2" ,"3",
        "4" , "5" , "6" ,
        "7", "8", "9"]

# Function to check if player input is valid



def game(board):
    print (board[0] + " | " + board[1] + " | "+ board[2])
    print ("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print ("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

game(board)


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




















