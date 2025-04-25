#-----------------------------------------------------------------------------
# Name:        Connect 4
# Purpose:     Plays a game of Connect 4
#
# Author:      812673, 760087
# Created:     25-Mar-2024
# Updated:     04-Apr-2024
#----------------------------------------------------------------------
#Value grid (6 x 7) indicating empty and player pieces.
coordinate_grid = [
                   [0, 0, 0, 0, 0, 0, 0], #1
                   [0, 0, 0, 0, 0, 0, 0], #2
                   [0, 0, 0, 0, 0, 0, 0], #3
                   [0, 0, 0, 0, 0, 0, 0], #4
                   [0, 0, 0, 0, 0, 0, 0], #5
                   [0, 0, 0, 0, 0, 0, 0]  #6
]               #   1  2  3  4  5  6  7 

#Used to convert the grid into player pieces and empty spaces.
coordinate_dict = { 0 : " ", 1 : "\033[1;31;40mo", 2 : "\033[1;34;40mo"}
display_board = []

#Creates and prints the board.
def make_board():
  #For each set of lists.
  for row in coordinate_grid:
    #Takes the value corresponding with each number in the grid and applies to dictionary to store in a row.
    display_row = [coordinate_dict.get(value) for value in row]
    #Adds each row to the board.
    display_board.append(display_row)
    #Prints the list as a string with spacing.
  for row in display_board:
    aligned_row = ' '.join(row)
    print("\033[1;37;40m| " + aligned_row + "\033[1;37;40m |")
  print("  1 2 3 4 5 6 7  \n")
  #Clears the board for next time.
  display_board.clear()

#Checks for where the piece will be placed by player 1 or player 2.
def player_move(player, column):
  value = 6
  #Descends down the column.
  for iteration in range(6):
    value -= 1
    if coordinate_grid[value][column - 1] == 0:
      if player == 1:
        coordinate_grid[value][column - 1] = 1
        print("")
        make_board()
        break
      if player == 2:
        coordinate_grid[value][column - 1] = 2
        print("")
        make_board()
        break

#Intro.
print("Welcome to connect 4.")
print("The goal of the game is to try to get 4 pieces in a row before your opponent. \nThis can be done horizontally, vertically, or diagonally.")
print("Type 1 - 7 to place a piece on the board.")
print("Good luck to both players! \n\n")

#Alternates the game until someone wins or there is a tie.
make_board()
game = True
#Game begins.
player_turn = 1
while game == True:
  move = input(f'''Player {player_turn}'s turn. ''')
  #Ensures only digits to not crash the terminal.
  while move.isdigit() == False:
    move = input(f"Invalid move, please try again\nPlayer {player_turn}'s turn. ")
  else:
    move = int(move)
    #Ensures the move is within the boundaries.
    while move <= 0 or move >= 8:
      move = input(f"Invalid row, please try again\nPlayer {player_turn}'s turn. ")
      while move.isdigit() == False:
        move = input(f"Invalid move, please try again\nPlayer {player_turn}'s turn. ")
      else:
        move = int(move)
    #Makes sure the column is not full.
    while coordinate_grid[0][move - 1] == 1 or coordinate_grid[0][move - 1] == 2:
      move = input(f"Column {move} is full, please try again\nPlayer {player_turn} 's turn. ")
      while move.isdigit() == False:
        move = input(f"Invalid move, please try again\nPlayer {player_turn}'s turn. ")
      else:
        move = int(move)
      while move <= 0 or move >= 8:
        move = input(f"Invalid row, please try again\nPlayer {player_turn}'s turn. ")
        while move.isdigit() == False:
          move = input(f"Invalid move, please try again\nPlayer {player_turn}'s turn. ")
        else:
          move = int(move)
  #Runs the player move.
  player_move(player_turn, move)
  
  #Checks if game is over.
  #Horizontal condition.
  connected_horizontal = 0
  #Iterates through each row checking for consecutive pieces.
  for row in coordinate_grid:
    row_value = 0
    for row_iteration in range(7):
      if row[row_value] == player_turn:
        connected_horizontal += 1
        if connected_horizontal == 4:
          game = False
        if row_iteration == 6:
          connected_horizontal = 0
      else:
        connected_horizontal = 0
      row_value += 1

  #Vertical condition.
  connected_vertical = 0
  #Iterates through the column in which the player placed a piece looking for 4 in a row.
  for vertical_iteration in range(6):
    if coordinate_grid[vertical_iteration][move - 1] == player_turn:
      connected_vertical += 1
      if connected_vertical == 4:
        game = False
    else: 
      connected_vertical = 0

  #Diagonal condition.
  row_num = 0
  #Scans the top 3 rows for player pieces and checks the diagonals of each piece.
  for row in coordinate_grid[:3]:
    connected_diagonal_l = 0
    connected_diagonal_r = 0
    for iterate in range(7):
      #Left diagonal for columns 4,5,6, and 7 (top right to bottom left diagonal).
      if iterate >= 3:
        if row[iterate] == player_turn:
          connected_diagonal_l += 1
          #Assign coordinates of scanned piece (must match to player).
          row_num_l = row_num
          column_l = iterate
          #Checks the left diagonal.
          for n_l in range(3):
            if coordinate_grid[row_num_l + 1][column_l - 1] == player_turn:
              connected_diagonal_l += 1
              if n_l != 2:
                row_num_l += 1
                column_l -= 1   
              #Win condition.
              if connected_diagonal_l == 4:
                game = False
            #Goes to next row.
            else:
              connected_diagonal_l = 0
              if iterate == 6:
                row_num += 1
              break    
        #Goes to next row.
        else:
          connected_diagonal_l = 0
          if iterate == 6:
            row_num += 1
      else:
        connected_diagonal_l = 0
        
      #Right diagonal for columns 1,2,3, and 4 (top left to bottom right diagonal).
      if iterate <= 3:
        connected_diagonal_r = 0
        if row[iterate] == player_turn:
          connected_diagonal_r += 1
          #Assign coordinates of scanned piece (must match to player).
          row_num_r = row_num
          column_r = iterate
          #Checks the right diagonal.
          for n_r in range(3):
            if coordinate_grid[row_num_r + 1][column_r + 1] == player_turn:
              connected_diagonal_r += 1
              if n_r != 2:
                row_num_r += 1
                column_r += 1
              #Win condition.
              if connected_diagonal_r == 4:
                game = False
            #Goes to next row.
            else:
              connected_diagonal_r = 0
              if iterate == 6:
                row_num += 1
              break 
        #Goes to next row.
        else:
          connected_diagonal_r = 0
          if iterate == 6:
            row_num += 1
      else:
        connected_diagonal_r = 0
        
  #Alternates between players.
  if player_turn == 1:
    player_turn += 1
  else:
    player_turn -= 1

  #Tie condition.
  tie = False
  tie_count = 0
  #Checks for any empty spaces after checking for wins.
  if game == True:
    for row in coordinate_grid:
      if row.count(0) == 0:
        tie_count += 1
        if tie_count == 6:
          print("GAME OVER: it's a tie!")
          tie = True
          game = False
        
#Declares winner.
if tie != True:
  if player_turn == 2:
    print("GAME OVER: Player 1 Won!")
  else:
    print("GAME OVER: Player 2 Won!")