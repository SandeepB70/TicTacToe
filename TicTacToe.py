game_board = [[1,2,3], [4,5,6], [7,8,9]]
#keeps track of moves already made so a player cannot repeat a move
moves_made = []
player1 = 'X'
player2 = 'O'
#Tells the game who is currently making their move, 1 is for player1 and 2 is for player2
crnt_player = 1
#Position on the board where the player wants to put their symbol
player_move = 0
#Checks if the input is valid or not.
invalid = True
#The number of turns that have passed so far
turn = 0
#indicates if a draw took place at the end of the game
draw = True

def print_board():
    '''
    Prints the gameboard
    '''
    border = '-------------------'
    for row in game_board:
        print("{}".format(border))
        print('|  ', end ='')
        for symbol in row:
            print(f"{symbol}", end = '  |  ')
        print('')
    print("{}".format(border))

def check3(player_num):
    '''
    Checks for three in a row for the current player.
    '''
    #Represents which symbol we are checking for three in a row(X or O)
    symbol = ''
    if player_num == 1:
        symbol = player1
    else:
        symbol = player2
    
    #Check each row
    for row in game_board:
        if row[0] == symbol and row[1] == symbol and row[2] == symbol:
            return True

    #check each column
    first_col = [row[0] for row in game_board]
    if first_col[0] == symbol and first_col[1] == symbol and first_col[2] == symbol:
        return True

    second_col = [row[1] for row in game_board]
    if second_col[0] == symbol and second_col[1] == symbol and second_col[2] == symbol:
        return True

    third_col = [row[2] for row in game_board]
    if third_col[0] == symbol and third_col[1] == symbol and third_col[2] == symbol:
        return True
    
    #Check diagonal from left to right
    if game_board[0][0] == symbol and game_board[1][1] == symbol and game_board[2][2] == symbol:
        return True
    
    #Check diagonal from right to left
    if game_board[0][2] == symbol and game_board[1][1] == symbol and game_board[2][0] == symbol:
        return True

    return False

def update_board(symbol, move):
    '''
    Updates the board to reflect the player's move. 'symbol' is the symbol ('X' or 'O') of the current player
    and 'move' represents where the player wants to place their symbol.
    '''
    for row in game_board:
        if player_move in row:
            indx = row.index(player_move)
            row[indx] = symbol
            moves_made.append(player_move)
            break

print("Welcome to Bakasoon's Tic Tac Toe.")
print("Yuh done know de rules but I guh explain.")
print("\nPlayer 1's symbol is an 'X' and Player 2's symbol is an 'O'.")
print("Players take turns placing their symbols on the board.")
print("First one to three in a row wins. If neither player")
print("gets three in a row by the end of the game, it is a draw.")
print("Here is what the board looks like.")
print_board()
print("Select the number of the space where you would like to place your symbol during your turn.")
crnt_player = int(input("Who would like to go first, Player 1 or Player 2? (Enter 1 or 2): "))

while invalid:
    if crnt_player < 1 or crnt_player > 2:
        crnt_player = int(input("Invalid response, please enter '1' or '2': "))
    else:
        invalid = False

#game will have a total of 9 moves
for x in range(0,9):
    turn += 1
    invalid = True
    player_move = int(input(f'Player {crnt_player}, enter your move: '))
    #Check if the player's move is valid
    while invalid:
        if player_move < 1 or player_move > 9:
            print('Invalid position!')
            player_move = int(input('Please select a valid position on the board: '))
            continue
        #check that the player is not trying to take a position on the board that has already been taken.
        if len(moves_made) != 0:
            if player_move in moves_made:
                player_move = int(input('Position has already been taken, please select another: '))
                continue
        if crnt_player == 1:
            update_board(player1, player_move)
        else:
            update_board(player2, player_move)
        print_board()
        invalid = False
    #Once the game has reached its fifth turn, need to start checking for three symbols in a row
    if turn >= 5:
        if check3(crnt_player) == True:
            print(f'Player {crnt_player} won!')
            draw = False
            break
    #If no one has won, alternate the current player.        
    if crnt_player == 1:
        crnt_player = 2
    else:
        crnt_player = 1
#Game has reached the end with no winner.
if draw:
    print('Game is a draw')