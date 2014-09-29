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
player_one_bullet_count = 6
player_one_score = 0

player_two_x_location = len(playing_field[0]) - 5
player_two_y_location = 7
player_two_bullet_count = 6
player_two_score = 0

'''
try a bullet class:
'''
class player_one_bullet:
  x_location = 0
  y_location = 0
  direction = "Right-Up"
  active = False

class player_two_bullet:
  x_location = 0
  y_location = 0
  direction = "Left-Up"
  active = False

# player 1 bullets
bullet_1 = player_one_bullet

bullet_2 = player_one_bullet
bullet_3 = player_one_bullet
bullet_4 = player_one_bullet
bullet_5 = player_one_bullet
bullet_6 = player_one_bullet

# player 2 bullets
bullet_7 = player_two_bullet
bullet_8 = player_two_bullet
bullet_9 = player_two_bullet
bullet_10 = player_two_bullet
bullet_11 = player_two_bullet
bullet_12 = player_two_bullet 


bullet_loop_count = 0 # ?

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
  if bullet_direction == "Right-Up" and bullet_active == False and bullet_count > 0:
    bullet_active = True
    bullet_x_location = player_x_location + 1
    bullet_y_location = player_y_location - 1

  elif bullet_direction == "Left-Up" and bullet_active == False and bullet_count > 0:
    bullet_active = True
    bullet_x_location = player_x_location - 1
    bullet_y_location = player_y_location - 1
  
  elif bullet_active == True: pass    # should not happen, because the next bullet should be up
  return bullet_active, bullet_x_location, bullet_y_location

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

def check_for_hit():
  global player_one_score, player_two_score, bullet_1, bullet_7
  if player_one_x_location == bullet_7.x_location and player_one_y_location == bullet_7.y_location and bullet_7.active == True:
        player_two_score += 1
        bullet_7.active = False
        
  if player_two_x_location == bullet_1.x_location and player_two_y_location == bullet_1.y_location and bullet_1.active == True:
    player_one_score += 1
    bullet_1.active = False

def update_playing_field():
  playing_field[player_one_y_location][player_one_x_location] = '1'
  playing_field[player_two_y_location][player_two_x_location] = '2'
  playing_field[bullet_1.y_location][bullet_1.x_location] = 'o'
  playing_field[bullet_7.y_location][bullet_7.x_location] = 'o'
def print_playing_field():
  print "bullet 7 active: ", bullet_7.active, "bullet 1 active: ", bullet_1.active
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      print playing_field[x][y],
    print ""
  print "Player 1 bullets left:", player_one_bullet_count, "P1 score: ", player_one_score, "P2 score: ", player_two_score

def check_for_key_press():
  global player_one_x_location, player_one_y_location, player_two_x_location, player_two_y_location, bullet_active
  global bullet_x_location, bullet_y_location, player_one_bullet_count, bullet_direction, player_two_score, player_one_score
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
          bullet_1.active, bullet_1.x_location, bullet_1.y_location = shoot("Right-Up", bullet_1.active, player_one_bullet_count, player_one_x_location, player_one_y_location)
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
          bullet_7.active, bullet_7.x_location, bullet_7.y_location = shoot("Left-Up", bullet_7.active, player_two_bullet_count, player_two_x_location, player_two_y_location)
        else: print char
                
      except IOError: pass
      
      check_for_hit()

      bullet_1.direction, bullet_1.y_location, bullet_1.x_location, bullet_1.active = move_bullets(bullet_1.direction, bullet_1.x_location, bullet_1.y_location, bullet_1.active)
      bullet_7.direction, bullet_7.y_location, bullet_7.x_location, bullet_7.active = move_bullets(bullet_7.direction, bullet_7.x_location, bullet_7.y_location, bullet_7.active)

      update_playing_field()
      print_playing_field()
      time.sleep(0.05)
  finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

# Auto resize terminal window (doesn't work when window is fullscreen or half_screen)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=19, cols=66))
check_for_key_press()