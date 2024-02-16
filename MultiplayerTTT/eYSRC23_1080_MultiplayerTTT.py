################################################################
# This are the answers for Cycle 9 ---> multiplayer ttt
#
# Author List:      
# 					Vineet Bhojannavar
# Team ID :			1080
# Filename:         multiplayer_ttt_boilerplate.py
################################################################

import turtle
################################################################
#TODO:		Import the sheet_dot_best_manager file below	   #
################################################################
from sheet_dot_best_manager import sheet_manager
################################################################

###################################################################################
#TODO: initialize global variables (current_turn, player, connect) 				  #
###################################################################################
current_turn = None
player = None
connect = sheet_manager('https://sheet.best/api/sheets/071b8c52-4bfc-4b2a-b061-3a2fc9e54133')
###################################################################################


def initialize_screen():

	global b, player, screen, current_turn, win, lose, tie, pen

	screen = turtle.Screen() #Return the singleton screen object. If none exists at the moment, create a new one and return it, else return the existing one.
	screen.setup(800,800) #Set the size and position of the main window.
	screen.title("Tic Tac Toe - e-Yantra") #Set title of turtle-window
	screen.setworldcoordinates(-5,-5,5,5) #Set up a user defined coordinate-system
	screen.bgcolor('#0E1F3C') #Set or return backgroundcolor of the TurtleScreen.
	screen.tracer(n=2,delay=10) #Turns turtle animation on/off and set delay for update drawings.
	turtle.speed(0)
	turtle.ht()

	turtle.resetscreen()
	b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]  # Nested list representing the value inside each box of the game.
	draw_board() # Draw the board for the first time.

	win = 0
	lose = 0
	tie = 0

	pen = turtle.Turtle()
	pen.color('#68748D')
	pen.up()
	pen.ht()

	current_turn = 'x'


def draw_board():
	turtle.ht()
	turtle.pencolor('#68748D') #Set pen color
	turtle.pensize(10) #Set pen size
	turtle.up()	#It means turtle will not draw if it moves
	turtle.goto(-3,-1) #Move the portal to (x,y) position
	turtle.seth(0) #Set heading of Turtle to 0
	turtle.down() #After this command, turtle will draw when it moves
	turtle.fd(6) #Move turtle forward by 6 units
	turtle.up() 
	turtle.goto(-3,1)
	turtle.seth(0)
	turtle.down()
	turtle.fd(6)
	turtle.up()
	turtle.goto(-1,-3)
	turtle.seth(90)
	turtle.down()
	turtle.fd(6)
	turtle.up()
	turtle.goto(1,-3)
	turtle.seth(90)
	turtle.down()
	turtle.fd(6)
	turtle.pensize(20)
	turtle.update()


def draw_circle(x,y): #Following commands will help to draw o about the given center i.e. (x,y)
	turtle.ht()
	turtle.up()
	turtle.goto(x,y-0.75)
	turtle.seth(0)
	turtle.color('#1CBD9E')
	turtle.down()
	turtle.circle(radius=0.75,steps=20)


def draw_x(x,y): #Following commands will help to draw x about the given center i.e. (x,y)
	turtle.ht()
	turtle.color('#E25041')
	turtle.up()
	turtle.goto(x-0.75,y-0.75)
	turtle.down()
	turtle.goto(x+0.75,y+0.75)
	turtle.up()
	turtle.goto(x-0.75,y+0.75)
	turtle.down()
	turtle.goto(x+0.75,y-0.75)


def draw_piece(i,j,p):
	if p==0: return #'p' or b[i][j] corresponds to empty cell. Since cell is empty i.e. contains 0, there is no need to draw
	x,y = 2*(j-1), -2*(i-1) 
	if p==1:  #As per the earlier convention, if 'p' is 1, we need to draw x otherwise o
		draw_x(x,y)
	else:
		draw_circle(x,y)


def draw(i,j,b):
	draw_piece(i,j,b)
	screen.update() # Perform an update on the screen

def dis_text(text):
	global win, lose, tie

	print(text)
	pen.clear()
	pen.goto(0,4)
	pen.write(str(text), align='center', font=("candara", 25, "bold"))
	pen.goto(0,-4)
	pen.write(f'Win: {str(win)}	Lose:{str(lose)}	Tie:{str(tie)}', align='center', font=("candara", 40, "bold"))

# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
def gameover(b):
	# Conditions required to check the winner.
	if b[0][0]>0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
	if b[1][0]>0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
	if b[2][0]>0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
	if b[0][0]>0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
	if b[0][1]>0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
	if b[0][2]>0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
	if b[0][0]>0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
	if b[2][0]>0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
	p = 0
	for i in range(3):
		for j in range(3):
			p += (1 if b[i][j] > 0 else 0) # 'p=p+1 if b[i][j]>0 else p=p+0'
	if p==9: return 3
	else: return 0
	

def play(x,y):
	
	# print("X:Y",x,y)
	# Cordinate system before conversion (Top left is (-5,5) and bottom right is (5,-5)):
	'''
	y
	↑
	|
	|
	.-----→x
	(-5,5)						   (5,5)
	.----------------------------------.
	|				 |				   |
	|				 |				   |
	|				 |				   |	
	|				 |(0,0)			   |
	|----------------.-----------------|
	|				 |				   |
	|				 |				   |
	|				 |				   |
	|				 |				   |
	.----------------------------------.
	(-5,-5)						  (5,-5)
	'''
	# Cordinate system after conversion (Top left is (0,0) and bottom right is (2,2)):
	'''
	.----→j		|	  |
	|		0,0 |	  | 2,0
	|	   _____|_____|_____
	↓			|	  |
	i			| 1,1 |
		   _____|_____|_____
				|	  | 
			0,2	|	  | 2,2
				|	  |
	'''
	# Conversion from one coordinate system to another:
	'''
	Conversion of x to j:
	 x	|	j
	---------
	-3	|	0
	-1	|	1
	 1	|	2
	Conversion of y to i:
	 y	|	i
	---------
	 3	|	0
	 1	|	1
	-1	|	2
	'''

	global player,continue_playing,b, current_turn

	refresh_sheet()

	if current_turn is not player:
		print('current chance :', current_turn, '	player :', player)
		dis_text('Its not your chance. Wait for other player to play')
		return

	i = -(int(y-3))//2
	j =  (int(x+3))//2

	if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0: 
		return # Condition will be true if user will click outside the designated area 
	if player == 'x': 
		b[i][j] = 1 #Assign b[i][j] as 1 and player as 'o'
		current_turn = 'o'
		dis_text('Other plyar has to make a move')
	else: 
		b[i][j] = 2	#Assign b[i][j] as 2 and player as 'x'
		current_turn ='x'
		dis_text('Other plyar has to make a move')
	

	################################################################
	#TODO:		Send data to store in the sheet					   #
	################################################################
	draw_and_check(i, j)
	connect.send_data({'move':str(player), 'row': str(i), 'col': str(j)})
	################################################################
	

def draw_and_check(i, j):
	global b, continue_playing, win, lose, tie

	draw(i,j,b[i][j])
	r = gameover(b)
	if r==1:
		dis_text('X won the match')
		continue_playing=screen.textinput("X won!","Type 'yes'/'no' to play again.")
		if player == 'x':
			win += 1
		else:
			lose += 1
		reinitialize_screen()
	elif r==2:
		dis_text('O won the match')
		continue_playing=screen.textinput("O won!","Type 'yes'/'no' to play again.")
		if player == 'o':
			win += 1
		else:
			lose += 1
		reinitialize_screen()
	elif r==3:
		dis_text('The match was tied')
		continue_playing=screen.textinput("Tie!","Type 'yes'/'no' to play again.")
		reinitialize_screen()
		tie += 1

def reinitialize_screen():
	global b,player,continue_playing,current_turn

	if(continue_playing is not None and continue_playing.lower()=='yes'):
		turtle.clear()
		b = [[ 0,0,0 ],
			 [ 0,0,0 ],
			 [ 0,0,0 ]]  # Nested list representing the value inside each box of the game.
		draw_board() # Draw the board for the first time.
		clear_sheet()
		if player == 'x':
			dis_text('Its your turn')
		else:
			dis_text('Other plyar has to make a move')

		current_turn = 'x'
	else:
		turtle.bye()


def input_player():
	global player

	# player = (input("Play as X or O : ")).lower()
	dis_text('Play as X or O')
	player = turtle.textinput("Play as X or O", 'Choose to play as X or O')
	while not(player == 'X' or player == 'x' or player == 'O' or player == 'o'):
		player = turtle.textinput("Play as X or O", 'Choose to play as X or O')
	
	if player == 'X' or player == 'x':
		player = 'x'
	elif player == 'O' or player == 'o':
		player = 'o'

def refresh_sheet():
	global connect, b, last_move, current_turn

	dis_text("Refreshing....")
	################################################################
	#TODO: Get data from the sheet and redraw if there is new data #
	################################################################
	data = connect.get_all_data()

	print(data['Data'])
	if len(data['Data']) != 0:
		last_move = data['Data'][-1]
		if player == last_move['move']:
			dis_text('Other player has to make a move')
		else:

			if last_move['move'] == 'x':
				current_turn = 'o'
			else:
				current_turn = 'x'

			if last_move['move'] == 'x': 
				b[int(last_move['row'])][int(last_move['col'])] = 1 #Assign b[i][j] as 1
			else: 
				b[int(last_move['row'])][int(last_move['col'])]	= 2 #Assign b[i][j] as 2

		draw_and_check(int(last_move['row']), int(last_move['col']))

		dis_text('Refreshed')
	else:
		if player == 'x':
			dis_text('Its your turn')
	################################################################
	

def clear_sheet():
	global connect
	dis_text("Deleting previous data...")
	################################################################
	#TODO: Delete all previous data from the sheet				   #
	################################################################

	# online_b = connect.get_all_data()
	# for i in range(1, len(online_b[2]) + 1):
	# 	connect.delete_data(i)

	delete_x = connect.delete_filtered_data('move', 'x')
	delete_o = connect.delete_filtered_data('move', 'o')

	if delete_x['Status'] == True and delete_o['Status'] == True:
		dis_text('Deleted data')

	################################################################
	

if __name__ == "__main__":
	initialize_screen()
	clear_sheet()
	input_player()
	screen.listen()
	screen.onkeypress(refresh_sheet, 'r')
	screen.onclick(play) #Bind function to mouse-click event on canvas. Coordinates of the click are passed as an argument to the function.
	turtle.mainloop()