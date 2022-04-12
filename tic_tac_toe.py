from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print(("+" + "-"*7)*3 + "+\n" +
             ("|" + " "*7)*4 + "\n" +
             ("|" + " "*3 + board[0][0] + " "*3 + "|")+
             (" "*3 +       board[0][1] + " "*3 + "|")+
             (" "*3 +       board[0][2] + " "*3 + "|\n")+
             ("|" + " "*7)*4 + "\n" +
             ("+" + "-"*7)*3 + "+\n" +
             ("|" + " "*7)*4 + "\n" +
             ("|" + " "*3 + board[1][0] + " "*3 + "|")+
             (" "*3 +       board[1][1] + " "*3 + "|")+
             (" "*3 +       board[1][2] + " "*3 + "|\n")+
             ("|" + " "*7)*4 + "\n" +
             ("+" + "-"*7)*3 + "+\n" +
             ("|" + " "*7)*4 + "\n" +
             ("|" + " "*3 + board[2][0] + " "*3 + "|")+
             (" "*3 +       board[2][1] + " "*3 + "|")+
             (" "*3 +       board[2][2] + " "*3 + "|\n")+
             ("|" + " "*7)*4 + "\n"+
             ("+" + "-"*7)*3 + "+\n"
        )
 
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    numeroCasilla = input('select a number: ')

    for i in range(0,3):
        found = False
        for j in range(0,3):
            if numeroCasilla == board[i][j]:
                board[i][j] = 'O'
                found = True
                break    # is this break necessary?
        if found == True:
            break

    if found == True:
        display_board(board)
    else:
        print('invalid movement')
        return False

def make_list_of_free_fields(board):

    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    control_board =[['1','2','3'],
                    ['4','5','6'],
                    ['7','8','9']]
    global a  #is this necessary?
    #free_fields = []

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == control_board[i][j]:
                x = control_board[i][j]
                free_fields.append(x)

    # print(free_fields) uncomment this to see the list in the terminal

    if free_fields == []:
        a = True
    else:
        a = False
    
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    # ///////////////////////HORIZONTAL/////////////////////

    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True
            
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True
            
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True
        # ///////////////////////VERTICAL/////////////////////
            
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True

    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True

    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True
        # ///////////////////////DIAGONAL/////////////////////
            
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True

    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        if sign == 'X':
            print('The machine won!')
        else:
            print('You won!')
        return  True

    elif a == True:
        print('Tie')
        return True 

    else:
        print('Continue!')
        return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    global b
    pcMove = str(randrange(1,10))
    # print(pcMove) uncomment this to see the pc's moves in terminal

    for i in range(0,3):
        found = False
        for j in range(0,3):
            if pcMove == board[i][j]:
                board[i][j] = 'X'
                found = True
                break    # is this break necessary?
        if found == True:
            break

    if found == True:
        b = True
        display_board(board) 
    else:
       b = False

#////////////  main program ///////////////

board =[['1','2','3'],
        ['4','X','6'],
        ['7','8','9']]

free_fields = []      
make_list_of_free_fields(board)
display_board(board)

while free_fields != []:

    while enter_move(board) == False:
        enter_move(board)

    free_fields = []
    make_list_of_free_fields(board)
    if victory_for(board, sign = 'O') == True: 
        break
    
    draw_move(board)
    while  b == False:
        draw_move(board)

    free_fields = []
    make_list_of_free_fields(board) 
    if victory_for(board, sign = 'X') == True: 
        break