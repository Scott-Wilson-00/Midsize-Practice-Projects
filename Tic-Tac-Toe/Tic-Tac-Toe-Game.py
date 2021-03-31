# Import the helper script
import helper as ttt

# The 2D array representing the board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

# Sets the player who's turn it is
player = 'X'

# Displays the tutorial
ttt.show_tut()

# Initializes player wins to be tracked
xWins = 0
oWins = 0

# Flag for program running
running = True

while running:
    # Clears the board and displays it
    board = ttt.reset_board()
    print('-' * 43)
    ttt.print_board(board)

    # Flag for game running
    playing = True
   
    while playing:
        # Gets a valid player choice --> calls update_board()
        # Displays newly updated board
        ttt.get_player_choice(board, player)
        print('-' * 43)
        ttt.print_board(board)
        

        # If a player wins, display the winner, add to their wins, end the game
        if ttt.check_for_win(board):
            print(f'\nPlayer {player} wins!')
            if player == 'X':
                xWins += 1
            else:
                oWins += 1
            playing = False

        # Swap whos turn it is
        player = ttt.switch_player(player)

    # Asks if the users would like to play again
    while True:
        ans = input("Play again? (yes/no): ").lower()

        # Ensures the answer is a valid input
        while ans != 'yes' and ans != 'no':
            print('\nPlease answer yes or no')
            ans = input("Play again? (yes/no): ").lower()

        # Continues/ends the program
        if ans == 'no':
            running = False
        break

# Displays win counts and thanks the players
if xWins == 1:
    grammar = 'time'
else:
    grammar = 'times'

print(f'\nPlayer X won {xWins} {grammar}.')

if oWins == 1:
    grammar = 'time'
else:
    grammar = 'times'

print(f'Player O won {oWins} {grammar}.')
print("Thanks for playing!")
