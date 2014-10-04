









######################     Last commit: Convert all of the bullet objects to arrays, 
######################                  in order to iterate through multiple bullets later

######################     Next: Multiple bullets per player by iterating through them





















# check for hit
# multiple bullets
# obstacles
import termios, fcntl, sys, os, time, tty
### game variables ###
# Small
playing_field = [["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
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
                 ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]

game_over = False

player_one_x_location = 4
player_one_y_location = 7
p1_bullet_count = -1 # -1 because in shoot(), bullet_count adds one to itself (0+1 = 1, so to get to element 0, -1+1 = 0)
player_one_score = 0

player_two_x_location = len(playing_field[0]) - 5
player_two_y_location = 7
p2_bullet_count = -1 # -1 because in shoot(), bullet_count adds one to itself (0+1 = 1, so to get to element 0, -1+1 = 0)
player_two_score = 0

# bullet data for each player. Each element is the bullet # for each player (6 bullets per person)
p1_bullet_x_location = [0, 0, 0, 0, 0, 0]
p1_bullet_y_location = [0, 0, 0, 0, 0, 0]
p1_bullet_direction = ["Right-Up", "Right-Up", "Right-Up", "Right-Up", "Right-Up", "Right-Up"]
p1_bullet_active = [False, False, False, False, False, False]

p2_bullet_x_location = [0, 0, 0, 0, 0, 0]
p2_bullet_y_location = [0, 0, 0, 0, 0, 0]
p2_bullet_direction = ["Left-Up", "Left-Up", "Left-Up", "Left-Up", "Left-Up", "Left-Up"]
p2_bullet_active = [False, False, False, False, False, False]

def move_player(direction, player_x_location, player_y_location):
  if direction == "up":
    if player_y_location != 1:  
      playing_field[player_y_location][player_x_location] = " "
      player_y_location-=1

  elif direction == "down":
    if player_y_location != len(playing_field)-2:
      playing_field[player_y_location][player_x_location] = " "
      player_y_location+=1

  elif direction == "left":
    if player_x_location != 1:
      playing_field[player_y_location][player_x_location] = " "
      player_x_location-=1

  elif direction == "right":
    if player_x_location != len(playing_field[0])-2:
      playing_field[player_y_location][player_x_location] = " "
      player_x_location+=1
  return player_x_location, player_y_location

def shoot(bullet_direction, bullet_active, bullet_count, player_x_location, player_y_location):
  if bullet_count < 6:
    bullet_count+=1
    if bullet_direction == "Right-Up" and bullet_active == False:
      bullet_active = True
      bullet_x_location = player_x_location + 1
      bullet_y_location = player_y_location - 1

    elif bullet_direction == "Left-Up" and bullet_active == False:
      bullet_active = True
      bullet_x_location = player_x_location - 1
      bullet_y_location = player_y_location - 1
  
  else: pass
  return bullet_active, bullet_x_location, bullet_y_location, bullet_count

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

def check_for_hit(player_one_score, player_two_score, p1_bullet_x_location, p1_bullet_y_location, p2_bullet_x_location, p2_bullet_y_location, p1_bullet_active, p2_bullet_active):
  if player_two_x_location == p1_bullet_x_location and player_two_y_location == p1_bullet_y_location and p1_bullet_active == True:
    player_one_score += 1
    p1_bullet_active = False

  if player_one_x_location == p2_bullet_x_location and player_one_y_location == p2_bullet_y_location and p2_bullet_active == True:
        player_two_score += 1
        p2_bullet_active = False

  return player_one_score, player_two_score, p1_bullet_active, p2_bullet_active

def update_playing_field():
  playing_field[player_one_y_location][player_one_x_location] = '1'
  playing_field[player_two_y_location][player_two_x_location] = '2'
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


def print_playing_field():
  print "bullet 2 active: ", p2_bullet_active[p2_bullet_count], "bullet 1 active: ", p1_bullet_active[p1_bullet_count]
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      print playing_field[x][y],
    print ""
  print "Player 1 bullets left:", p1_bullet_count, "P1 score: ", player_one_score, "P2 score: ", player_two_score

def check_for_key_press():
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
    while 1:
      # check for keypress. If there isn't any, don't check for which key pressed and do a screen refresh.
      try:
        char = ord(sys.stdin.read(1))

        # player 1
        if char=='\x1b[A':
          print "up"
        elif char == 119:
          player_one_x_location, player_one_y_location = move_player("up", player_one_x_location, player_one_y_location)
          print 'w'     
        elif char == 115:
          player_one_x_location, player_one_y_location = move_player("down", player_one_x_location, player_one_y_location)
          print 's'
        elif char==97:
          player_one_x_location, player_one_y_location = move_player("left", player_one_x_location, player_one_y_location)
          print 'a'
        elif char == 100:
          player_one_x_location, player_one_y_location = move_player("right", player_one_x_location, player_one_y_location)
          print 'd'
        elif char == 102:                                                                       
          p1_bullet_active[p1_bullet_count], p1_bullet_x_location[p1_bullet_count], p1_bullet_y_location[p1_bullet_count], p1_bullet_count = shoot("Right-Up", p1_bullet_active[p1_bullet_count], p1_bullet_count, player_one_x_location, player_one_y_location)
          print 'f'

        # player 2
        elif char == 91:
          print 'up'
          player_two_x_location, player_two_y_location = move_player("up", player_two_x_location, player_two_y_location)
        elif char == 39:
          print 'down'
          player_two_x_location, player_two_y_location = move_player("down", player_two_x_location, player_two_y_location)
        elif char == 59:
          print 'left'
          player_two_x_location, player_two_y_location = move_player("left", player_two_x_location, player_two_y_location)
        elif char == 92:
          print 'right'
          player_two_x_location, player_two_y_location = move_player("right", player_two_x_location, player_two_y_location)
        elif char == 108:
          print 'fire'
          p2_bullet_active[p2_bullet_count], p2_bullet_x_location[p2_bullet_count], p2_bullet_y_location[p2_bullet_count], p2_bullet_count = shoot("Left-Up", p2_bullet_active[p2_bullet_count], p2_bullet_count, player_two_x_location, player_two_y_location)
        else: print char
                
      except IOError: pass
      #player_one_score, player_two_score, p1_bullet_active[x], p2_bullet_active[x] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[x], p1_bullet_y_location[x], p2_bullet_x_location[x], p2_bullet_y_location[x], p1_bullet_active[x], p2_bullet_active[x])
      player_one_score, player_two_score, p1_bullet_active[p1_bullet_count], p2_bullet_active[p2_bullet_count] = check_for_hit(player_one_score, player_two_score, p1_bullet_x_location[p1_bullet_count], p1_bullet_y_location[p1_bullet_count], p2_bullet_x_location[p2_bullet_count], p2_bullet_y_location[p2_bullet_count], p1_bullet_active[p1_bullet_count], p2_bullet_active[p2_bullet_count])                                                                                                    
      p1_bullet_direction[p2_bullet_count], p1_bullet_y_location[p1_bullet_count], p1_bullet_x_location[p1_bullet_count], p1_bullet_active[p1_bullet_count] = move_bullets(p1_bullet_direction[p1_bullet_count], p1_bullet_x_location[p1_bullet_count], p1_bullet_y_location[p1_bullet_count], p1_bullet_active[p1_bullet_count])
      p2_bullet_direction[p2_bullet_count], p2_bullet_y_location[p2_bullet_count], p2_bullet_x_location[p2_bullet_count], p2_bullet_active[p2_bullet_count] = move_bullets(p2_bullet_direction[p2_bullet_count], p2_bullet_x_location[p2_bullet_count], p2_bullet_y_location[p2_bullet_count], p2_bullet_active[p2_bullet_count])

      update_playing_field()
      print_playing_field()
      time.sleep(0.05)
  finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

# Auto resize terminal window (doesn't work when window is fullscreen or half_screen)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=19, cols=66))
check_for_key_press()