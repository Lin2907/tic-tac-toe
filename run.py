
# Enter Username
def user_name():
    print("Hi there ! Ready to Play?")
    username = input("Enter your username: ")
    print(f"Welcome, {username}! Let's start !.\n")

user_name()

# Define current player

current_player = "X"
game_play = True


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


def player_input(board):
    move_x = int(input('Enter a number from 1 to 9 : '))
    if move_x >= 1 and move_x <= 9 and board[move_x-1] != "X" and board[move_x-1] != "O":  
        board[move_x-1] = current_player
    # inp-1 is due to index is starting from 0 -8
    else:
        print("This place is already taken or the input is invalid")

print (player_input(board))

# Main game loop

while game_play:
    game(board)
    player_input(board)


# Handle Horizontal Cases


















