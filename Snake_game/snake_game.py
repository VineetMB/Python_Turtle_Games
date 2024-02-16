import turtle as t
import time
import random
import os


os.chdir(str(os.path.dirname(os.path.abspath(__file__))) + '\\assets')

# Create the game window
wn = t.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
# the width and height can be put as user's choice
wn.setup(width=600, height=700)
wn.bgpic("bg.gif")
wn.tracer(0)

# initialize shape
apple = "apple.gif"
h_up = "head_up.gif"
h_down = "head_down.gif"
h_left = "head_left.gif"
h_right = "head_right.gif"
m_up = "mouth_up.gif"
m_down = "mouth_down.gif"
m_left = "mouth_left.gif"
m_right = "mouth_right.gif"
se_up = "segment_end_up.gif"
se_down = "segment_end_down.gif"
se_left = "segment_end_left.gif"
se_right = "segment_end_right.gif"
s_straight = "segment_straight.gif"
s_side = "segment_side.gif"
t_leftdown = "turn_leftdown.gif"
t_leftup = "turn_leftup.gif"
t_rightdown = "turn_rightdown.gif"
t_rightup = "turn_rightup.gif"
obstacle = "obstacle.gif"

t.register_shape(apple)
t.register_shape(h_up)
t.register_shape(h_down)
t.register_shape(h_left)
t.register_shape(h_right)
t.register_shape(m_up)
t.register_shape(m_down)
t.register_shape(m_left)
t.register_shape(m_right)
t.register_shape(se_up)
t.register_shape(se_down)
t.register_shape(se_left)
t.register_shape(se_right)
t.register_shape(s_straight)
t.register_shape(s_side)
t.register_shape(t_leftdown)
t.register_shape(t_leftup)
t.register_shape(t_rightdown)
t.register_shape(t_rightup)
t.register_shape(obstacle)


# the start menu
def menu():

    pen.color('black')
    pen.goto(0,100)
    pen.write('How to play:', align="center", font=("candara", 20, "bold"))
    pen.goto(0,0)
    pen.write('Use the arrow keys or \'wsad\' keys \n                to move the snake', align="center", font=("candara", 20, "bold"))
    pen.goto(0,-100)
    pen.write('Collect the apples to gain points \n       and aim for the highest', align="center", font=("candara", 20, "bold"))
    pen.goto(0,-200)
    pen.write('Do not crash the snake\'s head to the \nsnakes body or the stones(obstacles)', align="center", font=("candara", 20, "bold"))
    pen.goto(0,-300)

    global lvl
    lvl = wn.textinput(title='Choose level', prompt='Level 1 (type 1) : obstacle count = 1, speed = slow \n Level 2 (type 2) : obstacle count = 3, speed = normal \n Level 3 (type 3) : obstacle count = 5, speed = fast')
    while lvl == None or lvl == '':
        lvl = wn.textinput(title='Choose level', prompt='Level 1 (type 1) : obstacle count = 1, speed = slow \n Level 2 (type 2) : obstacle count = 3, speed = normal \n Level 3 (type 3) : obstacle count = 5, speed = fast')
    
    global obstacles_nos
    global delay
    if lvl == '1':
        obstacles_nos = 1
        delay = 0.1
    elif lvl == '2':
        obstacles_nos = 2
        delay = 0.075
    elif lvl == '3':
        obstacles_nos = 3
        delay = 0.05
    else:
        lvl = wn.textinput(title='Choose level', prompt='Level 1 (type 1) : obstacle count = 1, speed = slow \n Level 2 (type 2) : obstacle count = 3, speed = normal \n Level 3 (type 3) : obstacle count = 5, speed = fast')

    pen.color('white')
    pen.goto(0,250)

# make a grid dict
def make_grid():
    global grid
    grid = {}
    x = -260
    y = 210
    for row in range(1, 28):
        for col in range(1, 28):
            grid[row,col] = (x,y)
            x += 20
        x = -260
        y -= 20


# Define snake movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# move the snake head
def move():

    if head.distance(food) < 80:
        if head.direction == "up":
            head.shape(m_up)
            head.row -= 1
        elif head.direction == "down":
            head.shape(m_down)
            head.row += 1
        elif head.direction == "left":
            head.shape(m_left)
            head.col -= 1
        elif head.direction == "right":
            head.shape(m_right)
            head.col += 1
    else:
        if head.direction == "up":
            head.shape(h_up)
            head.row -= 1
        elif head.direction == "down":
            head.shape(h_down)
            head.row += 1
        elif head.direction == "left":
            head.shape(h_left)
            head.col -= 1
        elif head.direction == "right":
            head.shape(h_right)
            head.col += 1

    if head.row < 1:
        head.row = 27
    if head.row > 27:
        head.row = 1
    if head.col < 1:
        head.col = 27    
    if head.col > 27:
        head.col = 1

    head.goto(grid[head.row,head.col])


# move the snake's segments
def move_snake_body():

    snake_pos_list.clear()

    temp_segment_coor = []
    for index in range(len(snake_body)):
        if index == 0:
            x = head.xcor()
            y = head.ycor()
            temp_segment_coor.append((x,y))
        else:
            x = snake_body[index-1].xcor()
            y = snake_body[index-1].ycor()
            temp_segment_coor.append((x,y)) 

    snake_pos_list.append((head.row, head.col))

    for index in range(len(temp_segment_coor) - 1, -1, -1):

        for i in grid:
            if grid[i] == temp_segment_coor[index]:
                snake_pos_list.append(i)

        if index == 0:
            snake_body[0].goto(temp_segment_coor[index])
            if head.direction != snake_body[0].direction[-1]:
                if len(snake_body[0].direction) >= 2:
                    snake_body[0].direction = [snake_body[0].direction[-1],head.direction]
                else:
                    snake_body[0].direction = [snake_body[0].direction[0],head.direction]
            else:
                snake_body[0].direction = [head.direction]
        else:
            snake_body[index].goto(temp_segment_coor[index])
            snake_body[index].direction = snake_body[index-1].direction 

        if index != len(temp_segment_coor) - 1:
            if snake_body[index].direction == ['up'] or snake_body[index].direction == ['down']:
                snake_body[index].shape(s_straight)
            elif snake_body[index].direction == ['left'] or snake_body[index].direction == ['right']:
                snake_body[index].shape(s_side)
            elif snake_body[index].direction == ['up','left'] or snake_body[index].direction == ['right','down']:
                snake_body[index].shape(t_leftdown)
            elif snake_body[index].direction == ['up','right'] or snake_body[index].direction == ['left','down']:
                snake_body[index].shape(t_rightdown)
            elif snake_body[index].direction == ['down','left'] or snake_body[index].direction == ['right','up']:
                snake_body[index].shape(t_leftup)
            elif snake_body[index].direction == ['down','right'] or snake_body[index].direction == ['left','up']:
                snake_body[index].shape(t_rightup)
        if index == len(temp_segment_coor) - 1:
            if snake_body[index].direction == ['up'] or snake_body[index].direction == ['left','up'] or snake_body[index].direction == ['right','up']:
                snake_body[index].shape(se_up)
            elif snake_body[index].direction == ['down'] or snake_body[index].direction == ['left','down'] or snake_body[index].direction == ['right','down']:
                snake_body[index].shape(se_down)
            elif snake_body[index].direction == ['left'] or snake_body[index].direction == ['up','left'] or snake_body[index].direction == ['down','left']:
                snake_body[index].shape(se_left)
            elif snake_body[index].direction == ['right'] or snake_body[index].direction == ['up','right'] or snake_body[index].direction == ['down','right']:
                snake_body[index].shape(se_right)

# initialize the game startup
def initialize():
    time.sleep(1)
    head.row = 14
    head.col = 14
    head.goto(grid[head.row,head.col])
    head.direction = "stop"
    head.shape(h_up)
    for segment in snake_body:
        segment.goto(1000, 1000)
    snake_body.clear()
    segment = t.Turtle()
    segment.speed(0)
    segment.shape(s_straight)
    segment.penup()
    segment.goto(grid[head.row + 1, head.col])
    segment.direction = 'up'
    snake_body.append(segment)
    segment = t.Turtle()
    segment.speed(0)
    segment.shape(se_up)
    segment.penup()
    segment.goto(grid[head.row + 2, head.col])
    segment.direction = 'up'
    snake_body.append(segment)

    for obstacles in obstacle_list:
        obstacles.goto(1000,1000)
    obstacle_list.clear()
    snake_pos_list.clear()
    
    food.goto(grid[6, 14])
    
    global score
    score = 0

    pen.clear()
    pen.write(" Snake Game   Level : {} \nScore : {} High Score : {} ".format(
        lvl, score, high_score), align="center", font=("candara", 30, "bold"))

# check if cell is empty
def check_empty(row, col):
    for obstacles in obstacle_list:
            if obstacles.distance(grid[(row,col)]) < 20 or (row,col) in snake_pos_list:
                row = random.randint(1,27)
                col = random.randint(1,27)
                check_empty(row, col)
    return row, col


# create grid
make_grid()

# Create the snake head
head = t.Turtle()
head.shape(h_up)
head.penup()
# 'snake_head.direction' stores the direction in which the snake is/will moving
head.direction = "Stop"
head.row = 13
head.col = 13

# Create the food
food = t.Turtle()
food.speed(0)
food.shape(apple)
food.shapesize(2,2)
food.penup()

# Create the score display
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0, 250)
pen.write(" Snake Game   Level :   \nScore : 0 High Score : 0 ", align="center", font=("candara", 30, "bold")) 
        

# Initialize the body list for snake's body
snake_body=[]

obstacle_list = []

snake_pos_list = []

high_score = 0

menu()
initialize()

# Main Gameplay
while True:

    # Keyboard listeners
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")

    wn.update()

    # if head is touching food
    if head.distance(food) < 20:
            
        for i in range(obstacles_nos):
            o_row, o_col = check_empty(random.randint(1,27), random.randint(1,27))
            obstacles = t.Turtle()
            obstacles.penup()
            obstacles.speed(0)
            obstacles.shape(obstacle)
            obstacles.goto(grid[o_row, o_col])
            obstacle_list.append(obstacles)

        f_row, f_col = check_empty(random.randint(1,27), random.randint(1,27))
        food.goto(grid[f_row, f_col])


        # Adding segment
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape(s_straight)
        new_segment.penup()
        new_segment.direction = []
        snake_body.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(" Snake Game   Level : {} \nScore : {} High Score : {} ".format(
                    lvl, score, high_score), align="center", font=("candara", 30, "bold"))

    move_snake_body()
    move()

    # Checking for head collisions with body snake body or obstacle
    for segment in snake_body:
        if segment.distance(head) < 20: 
            initialize()
    for obstacles in obstacle_list:
        if obstacles.distance(head) < 20:
            initialize()

    time.sleep(delay)
