# GLobal Variables

#Is the game on ?
game_is_on = True

#Who won?
Winner = None

#current player
current_player = "X"

#Number of turns
number_of_turns = 1


board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"] 

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    
#play_game

def play_game():
    #global variables
    global number_of_turns
    global game_is_on
    display_board() #initialize board
    #While game is going
    while game_is_on:
        
        handle_turn(current_player)
        
        check_if_game_over()
        
        flip_player()
        
        
    #The game ended    
    if Winner == "X" or Winner  == "O":
        print(Winner + ' WON')
    elif Winner == None:
        print("TIE")          
    
#Handle turn for players
def handle_turn(player):
    print ("It's player " + player + "'s turn")
    
    position = input("Choose your position from 1-9  : ")
    
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose your position from 1-9  : ")
    
    position = int(position) - 1
    
    if board[position] != "-":
        print("Not a valid position")
    
    
    board[position] = player
    
    display_board()            
    
    
    
  
#Check if the game is over 
def check_if_game_over():
    #check if there was a winner
    check_if_win()
    #check if there was a tie
    check_if_tie()
    
#Check if there is a winner   
def check_if_win():
    #set up global winner
    global Winner 
    
    #check_rows()
    row_winner = check_rows()
    
    #check_diag()
    diagonal_winner = check_diag()
    
    #check_col()
    column_winner = check_col()
    
    if row_winner:
        #There was a win
        Winner = row_winner
        
   
    elif column_winner:
        #there was a win
        Winner = column_winner
        
        
    elif diagonal_winner:
        #There was a win
        Winner = diagonal_winner
        
         
    else:
        Winner = None   
   

    return
 
#check the rows in board
def check_rows():
    #set up global variables
    global game_is_on
    
    row_1 = board[0] == board[1] ==board[2] != "-"
    row_2 = board[3] == board[4] ==board[5] != "-"
    row_3 = board[6] == board[7] ==board[8] != "-"
    #if there is a win, set game_is_on to false
    if row_1 or row_2 or row_3:
        game_is_on = False
    #Check who is the winner X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


#Check the columns in board
def check_col():
    #set up global variables
    global game_is_on
    
    #check which column has won
    column_1 = board[0] == board[3] ==board[6] != "-"
    column_2 = board[1] == board[4] ==board[7] != "-"
    column_3 = board[2] == board[5] ==board[8] != "-"
    
    #if there is a win, set game_is_on to false
    if column_1 or column_2 or column_3:
        game_is_on = False
    #Check who is the winner X or O
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return
    

#check the diagonal in board
def check_diag():
    #set up global variables
    global game_is_on
    
    #Check win is through which diagonal
    diagonal_1 = board[0] == board[4] ==board[8] != "-"
    diagonal_2 = board[2] == board[4] ==board[6] != "-"
    
    #if there is a win, set game_is_on to false
    if diagonal_1 or diagonal_2:
        game_is_on = False
    #Check who is the winner X or O
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

#Check if there is a tie    
def check_if_tie():
    #global variables
    global game_is_on
    
    if "-" not in board:
        game_is_on = False
            
    return

#FLip the players turn
def flip_player():
    #global variable
    global current_player
    
    #flip the players
    if current_player == "X":
        current_player = "O"
        
    #if player is O
    elif current_player == "O":
        current_player = "X"
       
        
    return

play_game() 