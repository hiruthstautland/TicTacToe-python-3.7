#Python 3 - Tic tac toe - Sentdex tutorial 
import itertools


def win(current_game):       

  def same_code(l):
    if l.count(l[0]) == len(l) and l[0] !=0:
      return True 
    else:
      return False
#Should pull in/shorten the "Player...is the winner" line!

              #horizontall winner
  for row in game: 
    print(row)
    if same_code(row):
      print(f"Player {row[0]} is the winner horizontally!")
      return True

  diags = []                      #diagonal winner
  for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])
  if same_code(diags):
    print(f"Player {diags[0]} is the winner diagonally (/)!")
    return True

  diags = []
  for ix in range(len(game)):
    diags.append(game[ix][ix])
  if same_code(diags):
    print(f"Player {diags[0]} is the winner diagonally (\\)!")
    return True

  for col in range(len(game)):             #vertically
    check = []
    for row in game:
      check.append(row[col])
    if same_code(check):
      print(f"Player {check[0]} is the winner vertically! ")
      return True

      return False

def game_board(game_map,player=0, row=0, column=0, just_display=False):
  try:
    if game_map[row][column] !=0:
        print("This position in taken! Choose a free one")
        return game_map, False
    print("   a  b  c ") 
    if not just_display:
       game_map[row][column] = player
    for count, row in enumerate(game_map):
        print (count, row)
    return game_map, True
    #handeling errors
  except IndexError as e:   
    print('Error: Please input the values 0, 1 or 2!', e) 
    return game_map, False
  except Exception as e:
    print("OPS! Something went wrong!", e)
    return game_map, False

play = True
players = [1, 2]
while play:
  game_size = int(input("What size would you like to play of Tic Tac Toe?" ))
  game = [[0 for i in range(game_size)] for i in range(game_size)]
  game_won = False
  game, _ = game_board(game, just_display=True)
  player_choice = itertools.cycle([1,2])
  while not game_won:
    current_player = next(player_choice)
    print(f"Current Player: {current_player}")
    played = False

    while not played:
      column_choice = int(input("Play column 0, 1, 2:  "))
      row_choice = int(input("Play row 0, 1, 2:  "))
      game, played = game_board(game, current_player, row_choice, column_choice)
    
    if win(game):
         game_won = True
         again = input("Rematch? Press y | Exit? Press n")
         if again.lower() == "y":
           print("Restarting!")
         elif again.lower() == "n":
           print("Goodbye!")
           play = False
         else: 
           print("Not a valid answer. Please press y or n, on your keybord!")
           
           play = False
