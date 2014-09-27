#todo: shoot() and move_bullets for player 2 (no more global variables, use objects instead)

import termios, fcntl, sys, os, time, tty
# game variables
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

player_two_x_location = len(playing_field[0]) - 5
player_two_y_location = 7
player_two_bullet_count = 6

'''
try a bullet class:
'''
class Bullet:
  x_location = 0
  y_location = 0
  direction = ""
  active = False

bullet_x_location = 0
bullet_y_location = 0
bullet_direction = "Right-Up"
bullet_active = False

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

def shoot(player): 
  global bullet_active, bullet_x_location, bullet_y_location
  if player == 1 and bullet_active == False and player_one_bullet_count > 0:
    bullet_active = True
    bullet_x_location = player_one_x_location + 1
    bullet_y_location = player_one_y_location - 1
  elif player == 2: pass 

def move_bullets(player): 
  global bullet_loop_count
  global bullet_direction
  if bullet_loop_count > 0:
    bullet_loop_count = 0
    if player == 1 and bullet_active == True: 
      global bullet_y_location, bullet_x_location, bullet_active
      # clear previous bullet 
      playing_field[bullet_y_location][bullet_x_location] = " "
      
      # endzone boundary (left and right walls)
      if bullet_x_location > len(playing_field[0])-2:
        # deactivate bullet
        bullet_active = False
        bullet_direction = "done"
      
      elif bullet_x_location < 2:
        # deactivate bullet
        bullet_active = False
        bullet_direction = "done"   
      
      # side boundary (top and bottom walls)
      if bullet_y_location > len(playing_field)-3:
        bullet_direction = "Right-Up"
      elif bullet_y_location < 2: 
        bullet_direction = "Right-Down"

      if bullet_direction == "Right-Up":
        bullet_x_location += 1
        bullet_y_location -= 1
      elif bullet_direction == "Right-Down":
        bullet_x_location += 1
        bullet_y_location += 1

    elif player == 2: pass
  else: bullet_loop_count += 1
def update_playing_field():
  playing_field[player_one_y_location][player_one_x_location] = '1'
  playing_field[player_two_y_location][player_two_x_location] = '2'
  playing_field[bullet_y_location][bullet_x_location] = 'o'
def print_playing_field():
  print "x: ", player_one_x_location, "y: ", player_one_y_location, "bullet_active: ", bullet_active, "bullet direction: ", bullet_direction
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      print playing_field[x][y],
    print ""
  print "Player 1 bullets left:", player_one_bullet_count
def check_for_key_press():
  global player_one_x_location, player_one_y_location, player_two_x_location, player_two_y_location
  fd = sys.stdin.fileno()

  oldterm = termios.tcgetattr(fd)
  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)

  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

  try:
      while 1:
          try:
                print_playing_field() # move down
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
                  shoot(1)
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
                  shoot(1)
                else: print char
                update_playing_field()
                move_bullets(1)
                print_playing_field()
                time.sleep(0.05)
          except IOError:
            update_playing_field()
            move_bullets(1)
            print_playing_field()
            time.sleep(0.05)
  finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

# Auto resize terminal window (doesn't work when window is fullscreen or half_screen)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=20, cols=66))
check_for_key_press()