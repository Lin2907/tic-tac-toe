
# Enter Username
def user_name():
    print("Hi there ! Ready to Play?")
    username = input("Enter your username: ")
    print(f"Welcome, {username}! Let's start !.\n")

user_name()

#Drawing a game board using array and index

def game():
    board =["-" , "-" ,"-",
        "-" , "-" , "-" ,
        "-", "-", "-"]
    print (board[0] + " | " + board[1] + " | "+ board[2])
    print ("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print ("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

game()















