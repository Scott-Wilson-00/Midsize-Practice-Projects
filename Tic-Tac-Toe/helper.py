# Helper script for Tic-Tac-Toe game

# Recieves player input
def get_player_choice(b, player):
    while True:
        try:
            # Gets player choice (1-9), ensures it's an int
            choice = int(input(f'\nPlayer {player}, choose your position (1-9): '))

            # Ensures 1 <= choice <= 9
            if choice < 1 or choice > 9:
                raise ValueError
            # Sets the 2D array position based on choice
            elif choice == 1:
                pos = 0,0
            elif choice == 2:
                pos = 0,1
            elif choice == 3:
                pos = 0,2
            elif choice == 4:
                pos = 1,0
            elif choice == 5:
                pos = 1,1
            elif choice == 6:
                pos = 1,2
            elif choice == 7:
                pos = 2,0
            elif choice == 8:
                pos = 2,1
            elif choice == 9:
                pos = 2,2

            # Checks if position is already taken
            if not update_board(b, pos, player):
                raise ValueError
            break

        # Message to print if input is not valid
        except ValueError:
            print('\nInvalid input! Ensure it is an integer from 1-9 and the position is not taken.')


# Add the most recent play to the board   
def update_board(b, pos, player):
    # Check if space on board is already filled
    if b[pos[0]][pos[1]] != ' ':
        return False
    # If not, add the players move to the board
    else:
        b[pos[0]][pos[1]] = player
        return True


# Check if either player has won
def check_for_win(b):

    # Checks rows
    for row in b:
        # If the first position of the row is filled 
        if (row[0] == 'X' or row[0] == 'O'):
            # If the other placements in the row are the same
            if (row[0] == row[1] and row[0] == row[2]):
                return True

    # Checks columns
    for c in range(3):
        # If the first position of the column is filled 
        if b[0][c] == 'X' or b[0][c] == 'O':
            # If the other placements in the column are the same
            if b[0][c] == b[1][c] and b[0][c] == b[2][c]:
                return True

    # Checks diagonals
    # If middle position is filled
    if b[1][1] == 'X' or b[1][1] == 'O':
        # If top left and bottom right are the same
        if b[1][1] == b[0][0] and b[1][1] == b[2][2]:
            return True
        # If top right and bottom left are the same
        elif b[1][1] == b[0][2] and b[1][1] == b[2][0]:
            return True

    # Returns False if 3 in a row is not found
    return False
     

# Prints out the board for the players to see
def print_board(b):
    print()
    # Loops through rows
    for r in range(len(b)):
        if r == 1 or r == 2:
            print('- - - - - - ')
        # Loops through columns
        for c in range(len(b[r])):
            if c == 1 or c == 2:
                print('| ', end=' ')
            if c != 2:
                print(b[r][c], end=' ')
            else:
                print(b[r][c])

# Displays the tutorial for the game
def show_tut():
    print('''Welcome to Tic-Tac-Toe!
In this game you will play against a friend to score 3 in a row.
The layout for the board is as shown:
            
1 |  2 |  3
- - - - - - 
4 |  5 |  6
- - - - - - 
7 |  8 |  9
(The number is the input for that position)
Lets play!''')

# Resets the game board
def reset_board():
    return [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    ]


# Switches the current player
def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'
