''' 
todo: 
'''
import sys
import tty
import time
# keyboard input
tty.setcbreak(sys.stdin)

# game variables
playing_field = [["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"],
         ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]

game_over = False
player_one_y_location = 5
player_one_x_location = 5
bullet_x_location = 0
bullet_y_location = 0
def read_single_keypress():
    """Waits for a single keypress on stdin.

    This is a silly function to call if you need to do it a lot because it has
    to store stdin's current setup, setup stdin for reading single keystrokes
    then read the single keystroke then revert stdin back after reading the
    keystroke.

    Returns the character of the key that was pressed (zero on
    KeyboardInterrupt which can happen when a signal gets handled)

    """
    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK 
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR 
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)

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
  if player == 1:
    playing_field[player_one_y_location][player_one_x_location+1] = 'o'
  elif player == 2: pass
def update_playing_field():
  playing_field[player_one_y_location][player_one_x_location] = 'p'
def print_playing_field():
  print "x: ", player_one_x_location, "y: ", player_one_y_location
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      print playing_field[x][y],
    print ""
def game_loop():
  print_playing_field() # move down
  while game_over == False:
      read_single_keypress()
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

import termios, fcntl, sys, os, time

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
                print_playing_field()
                time.sleep(0.05)
          except IOError:
            update_playing_field()
            print_playing_field()
            time.sleep(0.05)
  finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
check_for_key_press()