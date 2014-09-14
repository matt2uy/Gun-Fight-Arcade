# todo: simplify print_playing _field
import sys
import tty


# keyboard input
tty.setcbreak(sys.stdin)

# game variables
playing_field = [["-","-","-","-","-","-","-","-","-","-"],
				 [" "," "," "," "," "," "," "," "," "," "],
				 [" "," "," "," "," "," "," "," "," "," "],
				 [" "," "," "," "," "," "," "," "," "," "],
				 [" "," "," "," "," "," "," "," "," "," "],
				 [" "," "," "," "," "," "," "," "," "," "],
				 [" "," "," "," "," "," "," "," "," "," "],
				 [" "," "," "," "," "," "," "," "," "," "],
				 [" "," "," "," "," "," "," "," "," "," "],
				 ["-","-","-","-","-","-","-","-","-","-"]]

game_over = False
player_one_y_location = 5
player_one_x_location = 5
def move_player(player, direction):
	global player_one_x_location, player_one_y_location
	if player == 1:
		if direction == "up":
			player_one_y_location-=1
		elif direction == "down":
			player_one_y_location+=1
		elif direction == "left":
			player_one_x_location-=1
		elif direction == "right":
			player_one_x_location+=1
	#elif player == 2:
def update_playing_field():
	playing_field[player_one_y_location][player_one_x_location] = 'p'
def print_playing_field():
	print '';
	for x in range(10):
		print playing_field[x][0], playing_field[x][1], playing_field[x][2], playing_field[x][3], playing_field[x][4], playing_field[x][5], playing_field[x][6], playing_field[x][7], playing_field[x][8], playing_field[x][9]
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

game_loop()
