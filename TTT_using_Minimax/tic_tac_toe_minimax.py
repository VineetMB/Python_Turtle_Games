import turtle
import copy
import random
import time


screen = turtle.Screen()
screen.setup(800,800)
screen.title("Tic Tac Toe")
screen.setworldcoordinates(-5,-5,5,5)
screen.bgcolor('#0E1F3C')
screen.tracer(0,0)
turtle.hideturtle()

def draw_board():
    turtle.pencolor('#68748D')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
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

def draw_circle(x,y):
    turtle.up()
    turtle.goto(x,y-0.75)
    turtle.seth(0)
    turtle.color('#1CBD9E')
    turtle.down()
    turtle.circle(0.75, steps=100)

def draw_x(x,y):
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
    if p==0: return
    x,y = 2*(j-1), -2*(i-1)
    if p==1:
        draw_x(x,y)
    else:
        draw_circle(x,y)
    
def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i,j,b[i][j])
    screen.update()

def gameover(b):
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
            p += (1 if b[i][j] > 0 else 0)
    if p==9: return 3
    else: return 0
    
def play(x,y):
    global turn
    if turn=='x': return
    
    i = 3-int(y+5)//2   # This line calculates the row index (i) where the player clicked. It converts the y-coordinate (vertical position) of the click into the corresponding row index
    j = int(x+5)//2 - 1   # This line calculates the column index (j) where the player clicked.  
    if i>2 or j>2 or i<0 or j<0 or board[i][j]!=0: return  # check if the player's click is valid
    if turn == 'x': board[i][j], turn = 1, 'o' # updates the game board (board) with the player's move
    else: board[i][j], turn = 2, 'x'
    draw(board)

    result = gameover(board)
    if result==1:
        screen.textinput("Game over!","X won!")
    elif result==2:
        screen.textinput("Game over!","O won!")
    elif result==3:
        screen.textinput("Game over!", "Tie!")
    if result>0: turtle.bye()
    pen.clear()
    pen.write('Computer is thinking...', align="center", font=("candara", 25, "bold"))
    time.sleep(0.75)
    _,move = max_node(board,-2,2)
    board[move[0]][move[1]] = 1
    draw(board)
    result = gameover(board)
    if result==1:
        screen.textinput("Game over!","X won!")
    elif result==2:
        screen.textinput("Game over!","O won!")
    elif result==3:
        screen.textinput("Game over!","Tie!")
    if result>0: turtle.bye()
    turn = 'o'

    pen.clear()
    # pen.write(f'Win : {win}     Tie : {tie}     Loss : {loss}', align="center", font=("candara", 25, "bold"))
    pen.write('Its your turn', align="center", font=("candara", 25, "bold"))
    # time.sleep(1)
    # pen.clear()
    # pen.write('Computer is thinking...', align="center", font=("candara", 25, "bold"))


def max_node(cb,alpha,beta):

    # terminal and value
    result = gameover(cb)
    if result==1: return 1,None
    elif result==2: return -1,None
    elif result==3: return 0,None
    else:

        score = -2
        # find all possible next moves
        action_list = list() 
        for i in range(3):
            for j in range(3):
                if cb[i][j] == 0: action_list.append((i,j))

        for (i,j) in action_list:
            newb = copy.deepcopy(cb)
            newb[i][j] = 1
            cs,_ = min_node(newb,alpha,beta)
            if score<cs:
                score=cs
                move = (i,j)
            alpha = max(alpha,cs)
            if beta<=alpha: return score,move

        return score,move

def min_node(cb,alpha,beta):

    move = ()
    result = gameover(cb)
    if result==1: return 1,None
    elif result==2: return -1,None
    elif result==3: return 0,None
    else:

        score = 2
        # find all possible next moves
        action_list = list()
        for i in range(3):
            for j in range(3):
                if cb[i][j] == 0: action_list.append((i,j))

        for (i,j) in action_list:
            nb = copy.deepcopy(cb)
            nb[i][j] = 2
            cs,_ = max_node(nb,alpha,beta)
            if score>cs:
                score=cs
                move = (i,j)
            beta = min(beta,cs)
            if beta<=alpha: return score,move

        return score,move

global board
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]    
draw(board)

toss = random.choice(['comp', 'player'])
win = 0
loss = 0
tie = 0

pen = turtle.Turtle()
pen.ht()
pen.pu()
pen.goto(0,4)
pen.color('white')

if toss == 'player':
    pen.write("The first chance goes to you", align="center", font=("candara", 25, "bold"))
    time.sleep(1)

    turn = 'o'
    if turn == 'o':
        screen.onclick(play)
        pen.clear()
        pen.write('Its your turn', align="center", font=("candara", 25, "bold"))
    else:
        s,move = max_node(board,-2,2)
        board[move[0]][move[1]] = 1
        draw(board)
        turn = 1
        
elif toss == 'comp':
    pen.write("The first chance goes to computer", align="center", font=("candara", 25, "bold"))
    # time.sleep(1)
    
    turn = 'x'
    screen.onclick(play)
    s,move = max_node(board,-2,2)
    board[move[0]][move[1]] = 1
    draw(board)
    pen.clear()
    pen.write('Its your turn', align="center", font=("candara", 25, "bold"))
    turn = 1

screen.mainloop()