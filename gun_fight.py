









######################  Done: 
              

######################  Next:
###################### Later: 





















# check for hit
# multiple bullets
# obstacles
import termios, fcntl, sys, os, time, tty
from termios import tcflush, TCIOFLUSH
### game variables ###
# Small
playing_field = [["/","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","\\"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
                 ["\\","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","/"]]


game_over = False
game_time_left = 30
second_interval = 0
refresh_rate = 0.05

player_one_x_location = 4
player_one_y_location = 7
p1_bullet_count = 5 # -1 because in shoot(), bullet_count adds one to itself (0+1 = 1, so to get to element 0, -1+1 = 0)
player_one_score = 0

player_two_x_location = len(playing_field[0]) - 5
player_two_y_location = 7
p2_bullet_count = 5 # -1 because in shoot(), bullet_count adds one to itself (0+1 = 1, so to get to element 0, -1+1 = 0)
player_two_score = 0

# bullet data for each player. Each element is the bullet # for each player (6 bullets per person)
p1_bullet_x_location = [0, 0, 0, 0, 0, 0]
p1_bullet_y_location = [0, 0, 0, 0, 0, 0]
p1_bullet_direction = ["none", "none", "none", "none", "none", "none"]
p1_bullet_active = [False, False, False, False, False, False]

p2_bullet_x_location = [0, 0, 0, 0, 0, 0]
p2_bullet_y_location = [0, 0, 0, 0, 0, 0]
p2_bullet_direction = ["none", "none", "none", "none", "none", "none"]
p2_bullet_active = [False, False, False, False, False, False]

def move_player(player, direction, player_x_location, player_y_location):
  playing_field[player_y_location-2][player_x_location] = ' '
  playing_field[player_y_location-2][player_x_location+1] = ' '

  playing_field[player_y_location-1][player_x_location] = ' '
  playing_field[player_y_location-1][player_x_location+1] = ' '

  playing_field[player_y_location][player_x_location-1] = ' '
  playing_field[player_y_location][player_x_location] = ' '
  playing_field[player_y_location][player_x_location+1] = ' '
  playing_field[player_y_location][player_x_location+2] = ' '
  playing_field[player_y_location][player_x_location+3] = ' '

  playing_field[player_y_location+1][player_x_location] = ' '
  playing_field[player_y_location+1][player_x_location+1] = ' '

  playing_field[player_y_location+2][player_x_location-1] = ' '
  playing_field[player_y_location+2][player_x_location+2] = ' '
  if direction == "up":
    if player_y_location != 1:  
      #playing_field[player_y_location][player_x_location] = " "
      player_y_location-=1

  elif direction == "down":
    if player_y_location != len(playing_field)-2:
      #playing_field[player_y_location][player_x_location] = " "
      player_y_location+=1

  elif direction == "left":
    if player == 2 and player_x_location > (len(playing_field[0])/2)+6: 
      if player_x_location != 1:
        #playing_field[player_y_location][player_x_location] = " "
        player_x_location-=1
    elif player == 1:
      if player_x_location != 1:
        #playing_field[player_y_location][player_x_location] = " "
        player_x_location-=1

  elif direction == "right":
    if player == 1 and player_x_location < (len(playing_field[0])/2)-7:
      if player_x_location != len(playing_field[0])-2:
        #playing_field[player_y_location][player_x_location] = " "
        player_x_location+=1
    elif player == 2:
      if player_x_location != len(playing_field[0])-2:
        #playing_field[player_y_location][player_x_location] = " "
        player_x_location+=1

  return player_x_location, player_y_location

def shoot(bullet_direction, bullet_active, bullet_count, player_x_location, player_y_location):
  if bullet_count >= 0:
    bullet_count-=1
    if bullet_direction == "Right-Up" and bullet_active == False:
      bullet_active = True
      bullet_x_location = player_x_location + 1
      bullet_y_location = player_y_location - 1

    elif bullet_direction == "Right-Down" and bullet_active == False:
      bullet_active = True
      bullet_x_location = player_x_location + 1
      bullet_y_location = player_y_location + 1

    elif bullet_direction == "Left-Up" and bullet_active == False:
      bullet_active = True
      bullet_x_location = player_x_location - 1
      bullet_y_location = player_y_location - 1

    elif bullet_direction == "Left-Down" and bullet_active == False:
      bullet_active = True
      bullet_x_location = player_x_location - 1
      bullet_y_location = player_y_location + 1
  return bullet_active, bullet_x_location, bullet_y_location, bullet_count, bullet_direction

def move_bullets(bullet_direction, bullet_x_location, bullet_y_location, bullet_active): 
  if bullet_active == True: 
    # clear previous bullet 
    playing_field[bullet_y_location][bullet_x_location] = " "
      
    ### Hitting a boundary: ###
    # endzone boundary (left and right walls)
    if bullet_x_location > len(playing_field[0])-2:
      # deactivate bullet
      bullet_active = False
      bullet_direction = "none"
      
    elif bullet_x_location < 1:
      # deactivate bullet
      bullet_active = False
      bullet_direction = "none"   
      
    # side boundary (top and bottom walls)
    if bullet_y_location > len(playing_field)-3 and bullet_direction == "Right-Down":
      bullet_direction = "Right-Up"
    elif bullet_y_location < 2 and bullet_direction == "Right-Up": 
      bullet_direction = "Right-Down"
    elif bullet_y_location > len(playing_field)-3 and bullet_direction == "Left-Down":
      bullet_direction = "Left-Up"
    elif bullet_y_location < 2 and bullet_direction == "Left-Up": 
      bullet_direction = "Left-Down"

    ### Moving the bullet ###
    if bullet_direction == "Right-Up":
      bullet_x_location += 1
      bullet_y_location -= 1
    elif bullet_direction == "Right-Down":
      bullet_x_location += 1
      bullet_y_location += 1
    elif bullet_direction == "Left-Up":
      bullet_x_location -= 1
      bullet_y_location -= 1
    elif bullet_direction == "Left-Down":
      bullet_x_location -= 1
      bullet_y_location += 1

  return bullet_direction, bullet_y_location, bullet_x_location, bullet_active

def refresh_playing_field_variables():
  global player_one_x_location, player_one_y_location, p1_bullet_count, player_two_x_location, player_two_y_location, p2_bullet_count, p1_bullet_x_location, p1_bullet_y_location, p1_bullet_direction, p1_bullet_active, p2_bullet_x_location, p2_bullet_y_location, p2_bullet_direction, p2_bullet_active 

  player_one_x_location = 4
  player_one_y_location = 7
  p1_bullet_count = 5 # -1 because in shoot(), bullet_count adds one to itself (0+1 = 1, so to get to element 0, -1+1 = 0)

  player_two_x_location = len(playing_field[0]) - 5
  player_two_y_location = 7
  p2_bullet_count = 5 # -1 because in shoot(), bullet_count adds one to itself (0+1 = 1, so to get to element 0, -1+1 = 0)

  # bullet data for each player. Each element is the bullet # for each player (6 bullets per person)
  p1_bullet_x_location = [0, 0, 0, 0, 0, 0]
  p1_bullet_y_location = [0, 0, 0, 0, 0, 0]
  p1_bullet_direction = ["Right-Up", "Right-Up", "Right-Up", "Right-Up", "Right-Up", "Right-Up"]
  p1_bullet_active = [False, False, False, False, False, False]

  p2_bullet_x_location = [0, 0, 0, 0, 0, 0]
  p2_bullet_y_location = [0, 0, 0, 0, 0, 0]
  p2_bullet_direction = ["Left-Up", "Left-Up", "Left-Up", "Left-Up", "Left-Up", "Left-Up"]
  p2_bullet_active = [False, False, False, False, False, False]

def refresh_playing_field():
  refresh_playing_field_variables()
  update_playing_field()
  print_playing_field()

def check_for_hit(player_one_score, player_two_score, p1_bullet_x_location, p1_bullet_y_location, p2_bullet_x_location, p2_bullet_y_location, p1_bullet_active, p2_bullet_active):
  if player_two_x_location == p1_bullet_x_location and player_two_y_location == p1_bullet_y_location and p1_bullet_active == True:
    player_one_score += 1
    p1_bullet_active = False

  if player_one_x_location == p2_bullet_x_location and player_one_y_location == p2_bullet_y_location and p2_bullet_active == True:
        player_two_score += 1
        p2_bullet_active = False

  return player_one_score, player_two_score, p1_bullet_active, p2_bullet_active

def update_playing_field():
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      if playing_field[x][y] == "1" or playing_field[x][y] == "2" or playing_field[x][y] == "o": 
        playing_field[x][y] = " "
    print ""
  '''
    __
    () 
   /||\_
    ||
   /  \




  '''
  # print both players

    # print player one character
  playing_field[player_one_y_location-2][player_one_x_location] = '_'
  playing_field[player_one_y_location-2][player_one_x_location+1] = '_'

  playing_field[player_one_y_location-1][player_one_x_location] = '('
  playing_field[player_one_y_location-1][player_one_x_location+1] = ')'

  playing_field[player_one_y_location][player_one_x_location-1] = '/'
  playing_field[player_one_y_location][player_one_x_location] = '|'
  playing_field[player_one_y_location][player_one_x_location+1] = '|'
  playing_field[player_one_y_location][player_one_x_location+2] = '\\'
  playing_field[player_one_y_location][player_one_x_location+3] = '_'

  playing_field[player_one_y_location+1][player_one_x_location] = '|'
  playing_field[player_one_y_location+1][player_one_x_location+1] = '|'

  playing_field[player_one_y_location+2][player_one_x_location-1] = '/'
  playing_field[player_one_y_location+2][player_one_x_location+2] = '\\'


  playing_field[player_two_y_location][player_two_x_location] = '2'

  # print 6 bullets per person * 2
  playing_field[p1_bullet_y_location[0]][p1_bullet_x_location[0]] = 'o'
  playing_field[p2_bullet_y_location[0]][p2_bullet_x_location[0]] = 'o'
  
  playing_field[p1_bullet_y_location[1]][p1_bullet_x_location[1]] = 'o'
  playing_field[p2_bullet_y_location[1]][p2_bullet_x_location[1]] = 'o'

  playing_field[p1_bullet_y_location[2]][p1_bullet_x_location[2]] = 'o'
  playing_field[p2_bullet_y_location[2]][p2_bullet_x_location[2]] = 'o'

  playing_field[p1_bullet_y_location[3]][p1_bullet_x_location[3]] = 'o'
  playing_field[p2_bullet_y_location[3]][p2_bullet_x_location[3]] = 'o'

  playing_field[p1_bullet_y_location[4]][p1_bullet_x_location[4]] = 'o'
  playing_field[p2_bullet_y_location[4]][p2_bullet_x_location[4]] = 'o'

  playing_field[p1_bullet_y_location[5]][p1_bullet_x_location[5]] = 'o'
  playing_field[p2_bullet_y_location[5]][p2_bullet_x_location[5]] = 'o'

def start_menu():
  p1_bullet_string = ""
  for bullet in range(p1_bullet_count+1):
    p1_bullet_string += "|"

  p2_bullet_string = ""
  for bullet in range(p2_bullet_count+1):
    p2_bullet_string += "|"

  print "        Score:", player_one_score, "                            Score: ", player_two_score
  for x in range(len(playing_field)):
    if x == 2:
      print "|       Player One                           Player Two       |"
    elif x == 3:
      print "|       ----------                           ----------       |"
    elif x == 4:
      print "|         W - Up                               [ = Up         |"
    elif x == 6:
      print "|   A - Left   D - Right               ; = Left   \ = Right   |"
    elif x == 8:
      print "|         S - Down                            '' = Down       |"
    elif x == 12:
      print "|                   Press enter to begin...                   |"
    else:
      for y in range(len(playing_field[0])):
        print playing_field[x][y],
      print ""
  print "        ", p1_bullet_string, "                             ", p2_bullet_string

  # wait for enter to be pressed
  enter_key_pressed = raw_input()   

def print_playing_field():
  p1_bullet_string = ""
  for bullet in range(p1_bullet_count+1):
    p1_bullet_string += "|"
  # keep the length of p1_bullet_string equal to 6, so p2_bullet_string doesn't change position in the print line below
  while len(p1_bullet_string) < 6:
    p1_bullet_string += " "

  p2_bullet_string = ""
  for bullet in range(p2_bullet_count+1):
    p2_bullet_string += "|"
  # keep the length of p1_bullet_string equal to 6, so p2_bullet_string doesn't change position in the print line below
  while len(p1_bullet_string) < 6:
    p1_bullet_string += " "

  print "        Score:", player_one_score, "            ", game_time_left, "              Score: ", player_two_score
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      print playing_field[x][y],
    print ""
  print "        ", p1_bullet_string, "                             ", p2_bullet_string

def print_after_score(winner_for_round):
  if winner_for_round == 1 or winner_for_round == 2:
    game_message = "|                       Player " + str(winner_for_round) + " Scores!                      |"
  elif winner_for_round == 0:
    game_message = "|                        No more bullets!                     |"
  elif winner_for_round == 3:
    winner_for_game = 0
    if player_one_score > player_two_score: 
      winner_for_game = 1
    elif player_two_score > player_one_score: 
      winner_for_game = 2
    game_message = "|                  Game Over! Player " + str(winner_for_game) + " Wins!               |"
    
  print "        Score:", player_one_score, "            ", game_time_left, "              Score: ", player_two_score
  for x in range(len(playing_field)):
    if x == 2:
      print game_message
    else:
      for y in range(len(playing_field[0])):
        print playing_field[x][y],
      print ""
  print ""

  # 2 second break
  time.sleep(2)

  # ignore all keystrokes in this period
  tcflush(sys.stdin, TCIOFLUSH)
  refresh_playing_field()

def print_post_game():
  if player_one_score > player_two_score: 
    game_message = "|                  Game Over! Player 1 Wins!                  |"
  elif player_two_score > player_one_score: 
    game_message = "|                  Game Over! Player 2 Wins!                  |"
  else:
    game_message = "|                      Game Over! Draw!                       |"
  print "        Score:", player_one_score, "            ", game_time_left, "              Score: ", player_two_score
  for x in range(len(playing_field)):
    if x == 2:
      print game_message
    else:
      for y in range(len(playing_field[0])):
        print playing_field[x][y],
      print ""
  print ""

  # ignore all keystrokes in this period
  tcflush(sys.stdin, TCIOFLUSH)

def game_loop():
  global player_one_x_location, player_one_y_location, player_two_x_location, player_two_y_location, bullet_active
  global bullet_x_location, bullet_y_location, p1_bullet_count, p2_bullet_count, bullet_direction, player_two_score, player_one_score
  
  global p1_bullet_x_location, p1_bullet_y_location, p1_bullet_direction, p1_bullet_active
  global p2_bullet_x_location, p2_bullet_y_location, p2_bullet_direction, p2_bullet_active 


  fd = sys.stdin.fileno()

  oldterm = termios.tcgetattr(fd)
  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)

  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

  try:
    while game_over == False:
      # check for keypress. If there isn't any, don't check for which key pressed and do a screen refresh.
      try:
        char = ord(sys.stdin.read(1))

        # player 1
        if char=='\x1b[A':
          print "up"
        elif char == 119:
          player_one_x_location, player_one_y_location = move_player(1, "up", player_one_x_location, player_one_y_location)
          print 'w'     
        elif char == 115:
          player_one_x_location, player_one_y_location = move_player(1, "down", player_one_x_location, player_one_y_location)
          print 's'
        elif char == 97:
          player_one_x_location, player_one_y_location = move_player(1, "left", player_one_x_location, player_one_y_location)
          print 'a'
        elif char == 100:
          player_one_x_location, player_one_y_location = move_player(1, "right", player_one_x_location, player_one_y_location)
          print 'd'
        elif char == 114:   
          if p1_bullet_count > -1:                                                                    
            p1_bullet_active[p1_bullet_count], p1_bullet_x_location[p1_bullet_count], p1_bullet_y_location[p1_bullet_count], p1_bullet_count, p1_bullet_direction[p1_bullet_count+1] = shoot("Right-Up", p1_bullet_active[p1_bullet_count], p1_bullet_count, player_one_x_location, player_one_y_location)
          print 'r'
        elif char == 102:   
          if p1_bullet_count > -1:                                                                    
            p1_bullet_active[p1_bullet_count], p1_bullet_x_location[p1_bullet_count], p1_bullet_y_location[p1_bullet_count], p1_bullet_count, p1_bullet_direction[p1_bullet_count+1] = shoot("Right-Down", p1_bullet_active[p1_bullet_count], p1_bullet_count, player_one_x_location, player_one_y_location)
          print 'f'

      
        # player 2
        if char == 27:
          char = ord(sys.stdin.read(1))
          if char == 91:
            char = ord(sys.stdin.read(1))

        if char == 65:
          print 'up'
          player_two_x_location, player_two_y_location = move_player(2, "up", player_two_x_location, player_two_y_location)
        elif char == 66:
          print 'down'
          player_two_x_location, player_two_y_location = move_player(2, "down", player_two_x_location, player_two_y_location)
        elif char == 68:
          print 'left'
          player_two_x_location, player_two_y_location = move_player(2, "left", player_two_x_location, player_two_y_location)
        elif char == 67:
          print 'right'
          player_two_x_location, player_two_y_location = move_player(2, "right", player_two_x_location, player_two_y_location)
        elif char == 10:
          print 'fire'
          if p2_bullet_count > -1:   
            p2_bullet_active[p2_bullet_count], p2_bullet_x_location[p2_bullet_count], p2_bullet_y_location[p2_bullet_count], p2_bullet_count, p2_bullet_direction[p2_bullet_count+1] = shoot("Left-Up", p2_bullet_active[p2_bullet_count], p2_bullet_count, player_two_x_location, player_two_y_location)
        elif char == 47:
          print 'fire'
          if p2_bullet_count > -1:   
            p2_bullet_active[p2_bullet_count], p2_bullet_x_location[p2_bullet_count], p2_bullet_y_location[p2_bullet_count], p2_bullet_count, p2_bullet_direction[p2_bullet_count+1] = shoot("Left-Down", p2_bullet_active[p2_bullet_count], p2_bullet_count, player_two_x_location, player_two_y_location)
        
        else: print char
                
      
      except IOError: pass

      # return one object/dictionary instead of these long lines here:

      # check if score changed, if so, take a break
      current_p1_score = player_one_score
      current_p2_score = player_two_score

      #player_one_score, player_two_score, p1_bullet_active[x], p2_bullet_active[x] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[x], p1_bullet_y_location[x], p2_bullet_x_location[x], p2_bullet_y_location[x], p1_bullet_active[x], p2_bullet_active[x])
      player_one_score, player_two_score, p1_bullet_active[0], p2_bullet_active[0] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[0], p1_bullet_y_location[0], p2_bullet_x_location[0], p2_bullet_y_location[0], p1_bullet_active[0], p2_bullet_active[0])                                                                                                    
      player_one_score, player_two_score, p1_bullet_active[1], p2_bullet_active[1] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[1], p1_bullet_y_location[1], p2_bullet_x_location[1], p2_bullet_y_location[1], p1_bullet_active[1], p2_bullet_active[1])   
      player_one_score, player_two_score, p1_bullet_active[2], p2_bullet_active[2] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[2], p1_bullet_y_location[2], p2_bullet_x_location[2], p2_bullet_y_location[2], p1_bullet_active[2], p2_bullet_active[2])   
      player_one_score, player_two_score, p1_bullet_active[3], p2_bullet_active[3] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[3], p1_bullet_y_location[3], p2_bullet_x_location[3], p2_bullet_y_location[3], p1_bullet_active[3], p2_bullet_active[3])   
      player_one_score, player_two_score, p1_bullet_active[4], p2_bullet_active[4] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[4], p1_bullet_y_location[4], p2_bullet_x_location[4], p2_bullet_y_location[4], p1_bullet_active[4], p2_bullet_active[4])   
      player_one_score, player_two_score, p1_bullet_active[5], p2_bullet_active[5] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[5], p1_bullet_y_location[5], p2_bullet_x_location[5], p2_bullet_y_location[5], p1_bullet_active[5], p2_bullet_active[5])   

      no_bullets_active = True
      for x in p1_bullet_active:
        if x == True:
          no_bullets_active = False
      for x in p2_bullet_active:
        if x == True:
          no_bullets_active = False

      # check if bullets are out, if so, take a break 
      if p1_bullet_count < 0 and p2_bullet_count < 0 and no_bullets_active == True:
        print_after_score(0)

      # check if score changed, if so, take a break
      if player_one_score > current_p1_score and no_bullets_active == True:
        print_after_score(1)
      elif player_two_score > current_p2_score and no_bullets_active == True:
        print_after_score(2)

      p1_bullet_direction[0], p1_bullet_y_location[0], p1_bullet_x_location[0], p1_bullet_active[0] = move_bullets(p1_bullet_direction[0], p1_bullet_x_location[0], p1_bullet_y_location[0], p1_bullet_active[0])
      p1_bullet_direction[1], p1_bullet_y_location[1], p1_bullet_x_location[1], p1_bullet_active[1] = move_bullets(p1_bullet_direction[1], p1_bullet_x_location[1], p1_bullet_y_location[1], p1_bullet_active[1])
      p1_bullet_direction[2], p1_bullet_y_location[2], p1_bullet_x_location[2], p1_bullet_active[2] = move_bullets(p1_bullet_direction[2], p1_bullet_x_location[2], p1_bullet_y_location[2], p1_bullet_active[2])
      p1_bullet_direction[3], p1_bullet_y_location[3], p1_bullet_x_location[3], p1_bullet_active[3] = move_bullets(p1_bullet_direction[3], p1_bullet_x_location[3], p1_bullet_y_location[3], p1_bullet_active[3])
      p1_bullet_direction[4], p1_bullet_y_location[4], p1_bullet_x_location[4], p1_bullet_active[4] = move_bullets(p1_bullet_direction[4], p1_bullet_x_location[4], p1_bullet_y_location[4], p1_bullet_active[4])
      p1_bullet_direction[5], p1_bullet_y_location[5], p1_bullet_x_location[5], p1_bullet_active[5] = move_bullets(p1_bullet_direction[5], p1_bullet_x_location[5], p1_bullet_y_location[5], p1_bullet_active[5])
      
      p2_bullet_direction[0], p2_bullet_y_location[0], p2_bullet_x_location[0], p2_bullet_active[0] = move_bullets(p2_bullet_direction[0], p2_bullet_x_location[0], p2_bullet_y_location[0], p2_bullet_active[0])
      p2_bullet_direction[1], p2_bullet_y_location[1], p2_bullet_x_location[1], p2_bullet_active[1] = move_bullets(p2_bullet_direction[1], p2_bullet_x_location[1], p2_bullet_y_location[1], p2_bullet_active[1])
      p2_bullet_direction[2], p2_bullet_y_location[2], p2_bullet_x_location[2], p2_bullet_active[2] = move_bullets(p2_bullet_direction[2], p2_bullet_x_location[2], p2_bullet_y_location[2], p2_bullet_active[2])
      p2_bullet_direction[3], p2_bullet_y_location[3], p2_bullet_x_location[3], p2_bullet_active[3] = move_bullets(p2_bullet_direction[3], p2_bullet_x_location[3], p2_bullet_y_location[3], p2_bullet_active[3])
      p2_bullet_direction[4], p2_bullet_y_location[4], p2_bullet_x_location[4], p2_bullet_active[4] = move_bullets(p2_bullet_direction[4], p2_bullet_x_location[4], p2_bullet_y_location[4], p2_bullet_active[4])
      p2_bullet_direction[5], p2_bullet_y_location[5], p2_bullet_x_location[5], p2_bullet_active[5] = move_bullets(p2_bullet_direction[5], p2_bullet_x_location[5], p2_bullet_y_location[5], p2_bullet_active[5])

      update_playing_field()
      print_playing_field()

      time.sleep(refresh_rate)
      
      global second_interval, game_time_left, game_over
      second_interval += refresh_rate

      # '1.18' - just trying to keep timing precise, need to find a
      # new way to keep time synced with refresh rate
      if second_interval > 1.18:
        game_time_left -= 1
        second_interval = 0

      # check if time ran out
      if game_time_left < 1:
        game_over = True
  finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

# Auto resize terminal window (doesn't work when window is fullscreen or half_screen)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=19, cols=66))
start_menu()
game_loop()
print_post_game()
time.sleep(2)