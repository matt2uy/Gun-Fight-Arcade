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
player_one_y_location = 5
player_one_x_location = 5

bullet_x_location = 0
bullet_y_location = 0
bullet_direction = "Right-Up"
bullet_active = False

bullet_loop_count = 0

def move_player(player, direction):
  global player_one_x_location, player_one_y_location
  if player == 1:
    if direction == "up":
      if player_one_y_location != 1:  
        playing_field[player_one_y_location][player_one_x_location] = " "
        player_one_y_location-=1

    elif direction == "down":
      if player_one_y_location != len(playing_field)-2:
        playing_field[player_one_y_location][player_one_x_location] = " "
        player_one_y_location+=1

    elif direction == "left":
      if player_one_x_location != 1:
        playing_field[player_one_y_location][player_one_x_location] = " "
        player_one_x_location-=1

    elif direction == "right":
      if player_one_x_location != len(playing_field[0])-2:
        playing_field[player_one_y_location][player_one_x_location] = " "
        player_one_x_location+=1
  #elif player == 2:
def shoot(player): 
  global bullet_active, bullet_x_location, bullet_y_location
  if player == 1 and bullet_active == False:
    bullet_active = True
    bullet_x_location = player_one_x_location + 1
    bullet_y_location = player_one_y_location - 1
  elif player == 2: pass
  else: 
    bullet_active = True

def move_bullets(player): 
  global bullet_loop_count
  global bullet_direction
  if bullet_loop_count > 0:
    bullet_loop_count = 0
    if player == 1 and bullet_active == True: 
      global bullet_y_location, bullet_x_location
      # clear previous bullet 
      playing_field[bullet_y_location][bullet_x_location] = " "
      
      # side boundary
      if bullet_x_location == len(playing_field)+1:
        bullet_direction = "Right-Up"
      elif bullet_x_location < 1: 
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
  playing_field[player_one_y_location][player_one_x_location] = 'p'
  playing_field[bullet_y_location][bullet_x_location] = 'o'
def print_playing_field():
  print "x: ", player_one_x_location, "y: ", player_one_y_location, "bullet_active: ", bullet_active, "bullet direction: ", bullet_direction
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      print playing_field[x][y],
    print ""
def game_loop():
  print_playing_field() # move down
  while game_over == False:
      char = ord(sys.stdin.read(1))
      if char=='\x1b[A':
        print "up"
      elif char == 119:
        move_player(1,"up")
        print 'w'     
      elif char == 115:
        move_player(1,"down")
        print 's'
      elif char==97:
        move_player(1,"left")
        print 'a'
      elif char == 100:
        move_player(1,"right")
        print 'd'
      elif char == 102:
        print 'f'
      else: print char
      update_playing_field()
      print_playing_field()
      time.sleep(0.01)
def check_for_key_press():
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
                if char=='\x1b[A':
                  print "up"
                elif char == 119:
                  move_player(1,"up")
                  print 'w'     
                elif char == 115:
                  move_player(1,"down")
                  print 's'
                elif char==97:
                  move_player(1,"left")
                  print 'a'
                elif char == 100:
                  move_player(1,"right")
                  print 'd'
                elif char == 102:
                  shoot(1)
                  print 'f'
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

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=18, cols=66))   
check_for_key_press()