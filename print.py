playing_field = [
					[" ", "_", "_", " ", " "], 
					[" ", "(", ")", " ", " "], 
					["/", "|", "|", "\\", "_"], 
					[" ", "|", "|", " ", " "], 
					["/", " ", " ", "\\", " "]
				  ]


'''
  __
  () 
 /||\_
  ||
 /  \





'''
def print_playing_field():
  for x in range(len(playing_field)):
    for y in range(len(playing_field[0])):
      print playing_field[x][y],
    print ""

print_playing_field()