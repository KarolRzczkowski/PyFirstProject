import random
import time

def game_start():
    board_size = 3
    board = [['_' for _ in range(board_size)] for _ in range(board_size)]

    frog = "𓆏"
    frog_x, frog_y = 0, 0

    board[frog_x][frog_y] = frog

    # Generate a random location for the wrong element
    wrong_x, wrong_y = random.randint(0, board_size - 1), random.randint(0, board_size - 1)
    board[wrong_x][wrong_y] = 'X'  # Representing the wrong element with 'X'

    print('Welcome to the Frog Game!')
    print('You control the frog (𓆏). Avoid landing on the wrong element (X).\n')

    for row in board:
        print(" ".join(row))

    moves_left = 3  
    moves_forward = 3  
    moves_right = 3
    moves_back = 3  

    forward = 'forward'
    left  = 'left'
    right = 'right' 
    back  = 'back'
     
    while moves_forward > 0 and moves_left > 0 and moves_right > 0 and moves_back > 0:
        move = input(f"Enter your move: ({forward}, {left}, {right}, {back}): ").lower()
        
        if move == "left":
            if frog_y > 0:
                board[frog_x][frog_y], frog_y = '_', frog_y - 1
                board[frog_x][frog_y] = frog
                moves_left -= 1
            else:
                print("You can't move left any further.")
        elif move == "forward":
            if frog_x < board_size - 1:
                board[frog_x][frog_y], frog_x = '_', frog_x + 1
                board[frog_x][frog_y] = frog
                moves_forward -= 1
            else:
                print("You can't move forward any further.")
        elif move == "right":
            if frog_y < board_size - 1:
                board[frog_x][frog_y], frog_y = '_', frog_y + 1
                board[frog_x][frog_y] = frog
                moves_right -= 1
        elif move == 'back':
            if frog_y > 0:
                board[frog_x][frog_y], frog_x = '_', frog_x - 1
                board[frog_x][frog_y] = frog
                moves_back -= 1
            else:
                print("You can't move back any further.")
        else:
            print("Invalid move. Please enter 'left', 'forward', 'right', or 'back'.")

        # Check if the frog landed on the wrong element
        if board[frog_x][frog_y] == 'X':
            print('Frog landed on the wrong element!')
            print('You lose!')
            return

        # Update the board after each move
        for row in board:
            print(" ".join(row))

    print('Congratulations! You successfully completed the game.')

if __name__ == "__main__":
    inputforstart = input('Do you want to start the game? (Yes/No): ').lower()
    if inputforstart == 'yes':
        game_start()
    else:
        print('So I"m logging you out ')
        time.sleep(1)
        print('Ok, goodbye!')
