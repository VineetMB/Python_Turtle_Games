import asyncio
import turtle
from math import inf
import winsound
from functools import partial
from PIL import ImageTk
import os
from sheet_dot_best_manager import sheet_manager
from random import choice,randint

# ------------------------ Initialization ----------------------------------------

os.chdir(str(os.path.dirname(os.path.abspath(__file__))) + '\\assets')

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Ultimate Tic Tac Toe")
screen.setworldcoordinates(-19,-19,19,19)
screen.bgpic('background\\'+str(randint(1,4))+'.gif')
screen.tracer(0,0)
turtle.hideturtle()


turtle.register_shape('images\\back.gif')
turtle.register_shape('images\\difficulty.gif')
turtle.register_shape('images\\easy.gif')
turtle.register_shape('images\\hard.gif')
turtle.register_shape('images\\intermediate.gif')
turtle.register_shape('images\\music.gif')
turtle.register_shape('images\\normal.gif')
turtle.register_shape('images\\options.gif')
turtle.register_shape('images\\quit.gif')
turtle.register_shape('images\\start.gif')
turtle.register_shape('images\\toggle_off.gif')
turtle.register_shape('images\\toggle_on.gif')
turtle.register_shape('images\\space_xo_2.gif')
turtle.register_shape('images\\arrow.gif')
turtle.register_shape('images\\pause.gif')
turtle.register_shape('images\\sound_on.gif')
turtle.register_shape('images\\sound_off.gif')
turtle.register_shape('images\\info.gif')
turtle.register_shape('images\\player_1.gif')
turtle.register_shape('images\\player_2.gif')
turtle.register_shape('images\\comp.gif')
turtle.register_shape('images\\single_player.gif')
turtle.register_shape('images\\offline_multi.gif')
turtle.register_shape('images\\online_multi.gif')
turtle.register_shape('images\\select_comp.gif')
turtle.register_shape('images\\select_p1.gif')
turtle.register_shape('images\\select_p2.gif')
turtle.register_shape('images\\select_random.gif')
turtle.register_shape('images\\choose_play.gif')
turtle.register_shape('images\\restart.gif')
turtle.register_shape('images\\game_paused.gif')
turtle.register_shape('images\\s_back.gif')
turtle.register_shape('images\\close.gif')
turtle.register_shape('images\\next.gif')
turtle.register_shape('images\\how_to_play.gif')
turtle.register_shape('images\\tutorial_1.gif')
turtle.register_shape('images\\tutorial_2.gif')
turtle.register_shape('images\\tutorial_3.gif')
turtle.register_shape('images\\tutorial_4.gif')
turtle.register_shape('images\\tutorial_5.gif')
turtle.register_shape('images\\player1_won.gif')
turtle.register_shape('images\\player2_won.gif')
turtle.register_shape('images\\comp_won.gif')
turtle.register_shape('images\\game_tie.gif')
turtle.register_shape('planets\\1.1.gif')
turtle.register_shape('planets\\1.2.gif')
turtle.register_shape('planets\\1.3.gif')
turtle.register_shape('planets\\2.1.gif')
turtle.register_shape('planets\\2.2.gif')
turtle.register_shape('planets\\2.3.gif')
turtle.register_shape('planets\\3.1.gif')
turtle.register_shape('planets\\3.2.gif')
turtle.register_shape('planets\\3.3.gif')
turtle.register_shape('planets\\4.1.gif')
turtle.register_shape('planets\\4.2.gif')
turtle.register_shape('planets\\4.3.gif')
turtle.register_shape('planets\\5.1.gif')
turtle.register_shape('planets\\5.2.gif')
turtle.register_shape('planets\\5.3.gif')
turtle.register_shape('planets\\6.1.gif')
turtle.register_shape('planets\\6.2.gif')
turtle.register_shape('planets\\6.3.gif')
turtle.register_shape('planets\\7.1.gif')
turtle.register_shape('planets\\7.2.gif')
turtle.register_shape('planets\\7.3.gif')
turtle.register_shape('planets\\8.1.gif')
turtle.register_shape('planets\\8.2.gif')
turtle.register_shape('planets\\8.3.gif')


# ------------------------- Global Variables ------------------------------------

canvas = turtle.getcanvas()

small_boards = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

main_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
main_highlight = []

current_turn = 0
player_1 = 1
player_2_or_comp = -1
current_board = -1

game_running = False
moves = 0 

best_move = -1
moves_list = [-inf,-inf,-inf,-inf,-inf,-inf,-inf,-inf,-inf]

is_hovering = False

level_info = [[1,2,3] , [2,3,4], '#edffcc']
planets = [['planets\\1.1.gif','planets\\1.2.gif','planets\\1.3.gif'],['planets\\2.1.gif','planets\\2.2.gif','planets\\2.3.gif']]
music = 'music\\1.wav'

connect = sheet_manager('https://sheet.best/api/sheets/071b8c52-4bfc-4b2a-b061-3a2fc9e54133')


# --------------------------- Functions for main game -------------------------------------------

# Resets the game board
def reset_board():
    global small_boards,main_board,current_turn,player_1,player_2_or_comp,current_board,game_running,moves,best_move,moves_list,is_hovering,main_highlight

    small_boards = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0] ]
    
    main_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    main_highlight = []

    player_1 = 1
    player_2_or_comp = -1
    current_board = -1

    moves = 0 

    best_move = -1
    moves_list = [-inf,-inf,-inf,-inf,-inf,-inf,-inf,-inf,-inf]

    is_hovering = False


# Function to check the condition of a given board
#    returns 1, -1 if player_1 or player_2_or_comp have won, else returns 0
def check_gameover(board):
    if board[0]!=0 and board[0] == board[1] and board[1] == board[2]: return board[0]
    if board[3]!=0 and board[3] == board[4] and board[4] == board[5]: return board[3]
    if board[6]!=0 and board[6] == board[7] and board[7] == board[8]: return board[6]
    if board[0]!=0 and board[0] == board[3] and board[3] == board[6]: return board[0]
    if board[1]!=0 and board[1] == board[4] and board[4] == board[7]: return board[1]
    if board[2]!=0 and board[2] == board[5] and board[5] == board[8]: return board[2]
    if board[0]!=0 and board[0] == board[4] and board[4] == board[8]: return board[0]
    if board[2]!=0 and board[2] == board[4] and board[4] == board[6]: return board[2]

    return 0

# It returns a numerical evaluation of the whole game in it's current state
# It evaluates the board on a abstract level and combines th value with that of detail_evaluate_small_board
def evaluate_board(big_board, current_board):
    eval_score = 0
    eval_big_board = []
    evaluator_multiplier = [1.4, 1, 1.4, 1, 1.75, 1, 1.4, 1, 1.4]

    for big_board_elements in range(9):
        eval_score += detail_evaluate_small_board(big_board[big_board_elements]) * 1.5 * evaluator_multiplier[big_board_elements]
        if(big_board_elements == current_board):
            eval_score += detail_evaluate_small_board(big_board[big_board_elements]) * evaluator_multiplier[big_board_elements]
        
        # checks for a winning condition of the small board and adds the value to a list
        temp_eval_big_board = check_gameover(big_board[big_board_elements])
        eval_score -= temp_eval_big_board * evaluator_multiplier[big_board_elements]
        eval_big_board.append(temp_eval_big_board)

    # if a winning condition is met in the main_board or big_board add or subtract 5000
    eval_score -= check_gameover(eval_big_board) * 5000

    eval_score += detail_evaluate_small_board(eval_big_board) * 150

    return eval_score

# evaluates a board in daetail based on the pieces arrangements
def detail_evaluate_small_board(small_board):
    global main_board

    eval_score = 0

    # preference for piece placement as center > corners > edges
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]
    for small_board_elements in range(len(small_board)):
        eval_score -= small_board[small_board_elements] * points[small_board_elements]
    
    # sum is used to get the placement of pieces in a row
    # eg, in [1,1,-1] or [1,-1,1] or [-1,1,1] the pieces add up to 1, and thus to check ths arrangement the value of sum is set to 1

    # check for player_1's pairs
    sum = 2

    if (small_board[0] + small_board[1] + small_board[2] == sum or
        small_board[3] + small_board[4] + small_board[5] == sum or
        small_board[6] + small_board[7] + small_board[8] == sum
        ):eval_score -= 6
    
    if (small_board[0] + small_board[3] + small_board[6] == sum or
        small_board[1] + small_board[4] + small_board[7] == sum or
        small_board[2] + small_board[5] + small_board[8] == sum
        ):eval_score -= 6

    if (small_board[0] + small_board[4] + small_board[8] == sum or
        small_board[2] + small_board[4] + small_board[6] == sum
        ):eval_score -= 7
    
    # check for player_2_or_comp's pairs blocked
    sum = -1

    if ((small_board[0] + small_board[1] == 2*sum and small_board[2] == -sum) or (small_board[1] + small_board[2] == 2*sum and small_board[0] == -sum) or (small_board[0] + small_board[2] == 2*sum and small_board[1] == -sum) or
        (small_board[3] + small_board[4] == 2*sum and small_board[5] == -sum) or (small_board[3] + small_board[5] == 2*sum and small_board[4] == -sum) or (small_board[5] + small_board[4] == 2*sum and small_board[3] == -sum) or
        (small_board[6] + small_board[7] == 2*sum and small_board[8] == -sum) or (small_board[6] + small_board[8] == 2*sum and small_board[7] == -sum) or (small_board[7] + small_board[8] == 2*sum and small_board[6] == -sum) or
        (small_board[0] + small_board[3] == 2*sum and small_board[6] == -sum) or (small_board[0] + small_board[6] == 2*sum and small_board[3] == -sum) or (small_board[3] + small_board[6] == 2*sum and small_board[0] == -sum) or
        (small_board[1] + small_board[4] == 2*sum and small_board[7] == -sum) or (small_board[1] + small_board[7] == 2*sum and small_board[4] == -sum) or (small_board[4] + small_board[7] == 2*sum and small_board[1] == -sum) or
        (small_board[2] + small_board[5] == 2*sum and small_board[8] == -sum) or (small_board[2] + small_board[8] == 2*sum and small_board[5] == -sum) or (small_board[5] + small_board[8] == 2*sum and small_board[2] == -sum) or
        (small_board[0] + small_board[4] == 2*sum and small_board[8] == -sum) or (small_board[0] + small_board[8] == 2*sum and small_board[4] == -sum) or (small_board[4] + small_board[8] == 2*sum and small_board[0] == -sum) or
        (small_board[2] + small_board[4] == 2*sum and small_board[6] == -sum) or (small_board[2] + small_board[6] == 2*sum and small_board[4] == -sum) or (small_board[4] + small_board[6] == 2*sum and small_board[2] == -sum)
        ):eval_score -= 9

    # check for player_2_or_comp's pairs
    sum = -2

    if (small_board[0] + small_board[1] + small_board[2] == sum or 
        small_board[3] + small_board[4] + small_board[5] == sum or 
        small_board[6] + small_board[7] + small_board[8] == sum
        ):eval_score += 6

    if (small_board[0] + small_board[3] + small_board[6] == sum or
        small_board[1] + small_board[4] + small_board[7] == sum or
        small_board[2] + small_board[5] + small_board[8] == sum
        ):eval_score += 6

    if (small_board[0] + small_board[4] + small_board[8] == sum or
        small_board[2] + small_board[4] + small_board[6] == sum
        ):eval_score += 7
    
    # check for player_1's pairs blocked
    sum = 1

    if ((small_board[0] + small_board[1] == 2*sum and small_board[2] == -sum) or (small_board[1] + small_board[2] == 2*sum and small_board[0] == -sum) or (small_board[0] + small_board[2] == 2*sum and small_board[1] == -sum) or
        (small_board[3] + small_board[4] == 2*sum and small_board[5] == -sum) or (small_board[3] + small_board[5] == 2*sum and small_board[4] == -sum) or (small_board[5] + small_board[4] == 2*sum and small_board[3] == -sum) or
        (small_board[6] + small_board[7] == 2*sum and small_board[8] == -sum) or (small_board[6] + small_board[8] == 2*sum and small_board[7] == -sum) or (small_board[7] + small_board[8] == 2*sum and small_board[6] == -sum) or
        (small_board[0] + small_board[3] == 2*sum and small_board[6] == -sum) or (small_board[0] + small_board[6] == 2*sum and small_board[3] == -sum) or (small_board[3] + small_board[6] == 2*sum and small_board[0] == -sum) or
        (small_board[1] + small_board[4] == 2*sum and small_board[7] == -sum) or (small_board[1] + small_board[7] == 2*sum and small_board[4] == -sum) or (small_board[4] + small_board[7] == 2*sum and small_board[1] == -sum) or
        (small_board[2] + small_board[5] == 2*sum and small_board[8] == -sum) or (small_board[2] + small_board[8] == 2*sum and small_board[5] == -sum) or (small_board[5] + small_board[8] == 2*sum and small_board[2] == -sum) or
        (small_board[0] + small_board[4] == 2*sum and small_board[8] == -sum) or (small_board[0] + small_board[8] == 2*sum and small_board[4] == -sum) or (small_board[4] + small_board[8] == 2*sum and small_board[0] == -sum) or
        (small_board[2] + small_board[4] == 2*sum and small_board[6] == -sum) or (small_board[2] + small_board[6] == 2*sum and small_board[4] == -sum) or (small_board[4] + small_board[6] == 2*sum and small_board[2] == -sum)
        ):eval_score += 9
    
    # include the condition of the small_board and main_board in the score
    eval_score -= check_gameover(small_board) * 12
    eval_score -= check_gameover(main_board) * 12

    return eval_score


# It returns a numerical evaluation of a square if a certain piece is played
# It scores the square based on its:
#   1. position on the board
#   2. forms pairs
#   3. forms 3 in a row
#   4. blocks oponents pair

def evaluateBestMove(small_board, square):
    global player_1, player_2_or_comp

    small_board[square] = player_2_or_comp
    eval_score = 0

    # list of preference for placement as center > corners > edges
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]
    eval_score += points[square]

    # sum is used to get the placement of pieces in a row
    # eg, in [1,1,-1] or [1,-1,1] or [-1,1,1] the pieces add up to 1, and thus to check ths arrangement the value of sum is set to 1

    # Prefer creating pairs
    sum = -2
    if (small_board[0] + small_board[1] + small_board[2] == sum or
        small_board[3] + small_board[4] + small_board[5] == sum or 
        small_board[6] + small_board[7] + small_board[8] == sum or 
        small_board[0] + small_board[3] + small_board[6] == sum or 
        small_board[1] + small_board[4] + small_board[7] == sum or
        small_board[2] + small_board[5] + small_board[8] == sum or 
        small_board[0] + small_board[4] + small_board[8] == sum or 
        small_board[2] + small_board[4] + small_board[6] == sum
        ):eval_score += 1
    
    # Take victories
    sum = -3
    if (small_board[0] + small_board[1] + small_board[2] == sum or
        small_board[3] + small_board[4] + small_board[5] == sum or 
        small_board[6] + small_board[7] + small_board[8] == sum or 
        small_board[0] + small_board[3] + small_board[6] == sum or 
        small_board[1] + small_board[4] + small_board[7] == sum or
        small_board[2] + small_board[5] + small_board[8] == sum or 
        small_board[0] + small_board[4] + small_board[8] == sum or 
        small_board[2] + small_board[4] + small_board[6] == sum
        ):eval_score += 5
    
    eval_score -= check_gameover(small_board) * 15

    # Block sum players turn if necessary
    small_board[square] = player_1
    sum = 3
    if (small_board[0] + small_board[1] + small_board[2] == sum or
        small_board[3] + small_board[4] + small_board[5] == sum or 
        small_board[6] + small_board[7] + small_board[8] == sum or 
        small_board[0] + small_board[3] + small_board[6] == sum or 
        small_board[1] + small_board[4] + small_board[7] == sum or
        small_board[2] + small_board[5] + small_board[8] == sum or 
        small_board[0] + small_board[4] + small_board[8] == sum or 
        small_board[2] + small_board[4] + small_board[6] == sum
        ):eval_score += 2
    
    small_board[square] = 0

    return eval_score

# A recurresive algorithm which goes through the main game tree for a certain no of turns and returns the best move for a given player
def minimax(big_board, board_to_play_on, depth, alpha, beta, is_maximizing_player):
    global player_1, player_2_or_comp
    
    temp_play_at = -1

    # stop minimax when the depth is 0 of the main_bosrd or big_board is won and return the values
    eval_score = evaluate_board(big_board, board_to_play_on)
    if depth <= 0 or abs(eval_score) > 5000:
        return [eval_score, temp_play_at]
    
    # If the board to play on is won, then you can play on any board
    if (board_to_play_on != -1 and check_gameover(big_board[board_to_play_on]) != 0):
        board_to_play_on = -1

    # If a board is full (doesn't include 0), it  sets the board to play on to -1
    if (board_to_play_on != -1 and (0 not in big_board[board_to_play_on])):
        board_to_play_on = -1
    

    if(is_maximizing_player):

        max_eval = -inf

        for big_or_small_board_element_iter in range(9):

            minimax_results_score = -inf
            # all boards
            if board_to_play_on == -1:
                for small_board_element in range(9):

                    # Exclude the table which are won
                    if check_gameover(big_board[big_or_small_board_element_iter]) == 0:

                        # here big_or_small_board_element_iter iterrates for big board elements
                        if big_board[big_or_small_board_element_iter][small_board_element] == 0:

                            big_board[big_or_small_board_element_iter][small_board_element] = player_2_or_comp

                            minimax_results_score = minimax(big_board, small_board_element, depth-1, alpha, beta, False)[0]

                            big_board[big_or_small_board_element_iter][small_board_element] = 0

                            if minimax_results_score > max_eval:
                                max_eval = minimax_results_score
                                temp_play_at = big_or_small_board_element_iter
                            alpha = max(alpha, minimax_results_score)

                    if beta <= alpha:
                        break

            # go through each squares if there is a given board to play at
            else:

                # here big_or_small_board_element_iter iterrates for small board elements
                if big_board[board_to_play_on][big_or_small_board_element_iter] == 0:

                    big_board[board_to_play_on][big_or_small_board_element_iter] = player_2_or_comp

                    minimax_results = minimax(big_board, big_or_small_board_element_iter, depth-1, alpha, beta, False)

                    big_board[board_to_play_on][big_or_small_board_element_iter] = 0

                    minimax_results_score = minimax_results[0]
                    if minimax_results_score > max_eval:
                        max_eval = minimax_results_score
                        temp_play_at = minimax_results[1]

                    alpha = max(alpha, minimax_results_score)
                    if beta <= alpha:
                        break

        return [max_eval, temp_play_at]
    

    else:

        min_eval = inf

        for big_or_small_board_element_iter in range(9):

            minimax_results_score = inf

            # all boards
            if board_to_play_on == -1:
                for small_board_element in range(9):

                    # Exclude the table which are won
                    if check_gameover(big_board[big_or_small_board_element_iter]) == 0:

                        # here big_or_small_board_element_iter iterrates for big board elements
                        if big_board[big_or_small_board_element_iter][small_board_element] == 0:

                            big_board[big_or_small_board_element_iter][small_board_element] = player_1

                            minimax_results_score = minimax(big_board, small_board_element, depth-1, alpha, beta, True)[0]

                            big_board[big_or_small_board_element_iter][small_board_element] = 0
                            if minimax_results_score < min_eval:
                                min_eval = minimax_results_score
                                temp_play_at = big_or_small_board_element_iter
                            beta = min(beta, minimax_results_score)

                    if beta <= alpha:
                        break

            # go through each squares if there is a given board to play at
            else:

                # here big_or_small_board_element_iter iterrates for small board elements
                if big_board[board_to_play_on][big_or_small_board_element_iter] == 0:

                    big_board[board_to_play_on][big_or_small_board_element_iter] = player_1

                    minimax_results = minimax(big_board, big_or_small_board_element_iter, depth-1, alpha, beta, True)

                    big_board[board_to_play_on][big_or_small_board_element_iter] = 0
                
                    minimax_results_score = minimax_results[0]
                    if minimax_results_score < min_eval:
                        min_eval = minimax_results_score
                        temp_play_at = minimax_results[1]

                    beta = min(beta, minimax_results_score)
                    if beta <= alpha:
                        break

        return [min_eval, temp_play_at]

# Draws the piece on the board, updates the current board and its graphics and checks for gameover conditions.
def draw_and_check(small_board,square):
    global main_board, current_board, current_turn, game_running

    draw(small_board,square)

    if main_board[small_board] == 0:
        small_board_status = check_gameover(small_boards[small_board])
        if small_board_status != 0:
            main_board[small_board] = small_board_status
            
    total_empty_squares = 0
    for board in range(9):
        empty_squares = 0
        for element in small_boards[board]:
            if element == 0:
                empty_squares += 1
                total_empty_squares += 1
        if empty_squares == 0:
            main_board[board] = 3

    if game_running :

        gameover_result = check_gameover(main_board)

        if gameover_result != 0:
            dis_gameover(gameover_result)
            return
        elif total_empty_squares == 0:
            dis_gameover(0)
            return
                
    current_board = square

    if 0 not in small_boards[current_board] or main_board[current_board] != 0:
        current_board = -1

    current_turn = -current_turn

    display_available_boards()
    draw_main_board_condition(small_board)


# -------------------------------------------- Mouse and coordinate conversion centeric functions -------------------------------------------------

# Converts the x,y coordinates of the world to the indicies of the small_boards list
def mouse_2_board(x,y):
    global is_hovering

    if is_hovering:
        x = int((11 + x) // 1)
        y = int((9 - y) // 1)
        x = (x - (x % 2)) + 1
        y = (y - (y % 2)) + 1

        if (x >= 1 or x <= 21) and (y >= 1 or y <= 21):
            if ((x % 8 == 1 or x % 8 == 3 or x % 8 == 5) and
                (y % 8 == 1 or y % 8 == 3 or y % 8 == 5)):
                x = (x - x//2) - (x // 8)
                y = (y - y//2) - (y // 8)

                x -= 1
                y -= 1
                board_coor = ((y//3)*27) + ((y % 3)*3) + ((x//3)*9) + (x % 3)

                small_borad = board_coor // 9
                square = board_coor % 9

                return small_borad, square

# Converts the indicies of the small_boards list to the x,y coordinates of the world
def board_2_coor(board,square):
    x = ((2 * (square % 3)) + (8 * (board % 3))) - 10
    y = 8 - ((2 * (square // 3)) + (8 * (board // 3)))
    return x,y


# Converts the x,y coordinates of the mouse when hovering to the indicies of the small_boards list and displays the hover box
def on_motion(event):
    global current_board, is_hovering, hover_box_images

    is_hovering = False
    hover_box_images = []
    # deletes all elements(images) taged hover_box
    canvas.delete('hover_box')

    if game_running:

        if game_type == 0 or game_type == 1:
            if current_turn != player_1: return

        x = (event.x - turtle.window_width() / 2)
        y = (-event.y + turtle.window_height() / 2)

        x = 11 + (x * 30 / 787)
        y = 9 - (y * 30 / 787)

        if ((x % 2) >= 0.1 and (x % 2) <= 1.95) and ((y % 2) >= 0.1 and (y % 2) <= 1.95):
            x = int((x - (x % 2)) + 1)
            y = int((y - (y % 2)) + 1)

            if (x >= 1 and x <= 21) and (y >= 1 and y <= 21):
                if ((x % 8 == 1 or x % 8 == 3 or x % 8 == 5) and
                    (y % 8 == 1 or y % 8 == 3 or y % 8 == 5)):
                    x = (x - x//2) - (x // 8)
                    y = (y - y//2) - (y // 8)

                    x -= 1
                    y -= 1
                    board_coor = ((y//3)*27) + ((y % 3)*3) + ((x//3)*9) + (x % 3)

                    board = board_coor // 9
                    square = board_coor % 9

                    if (board == current_board or (current_board == -1 and main_board[board] == 0)) and small_boards[board][square] == 0:

                        x,y = board_2_coor(board, square)

                        x = (x * 778 / 30)
                        y = -(y * 778 / 30)

                        # used to display sem-transparent images as turtle dosent support it
                        image = ImageTk.PhotoImage(file="images\\highlight_2.1.png")
                        canvas.create_image(x, y, image=image, tags='hover_box')
                        hover_box_images.append(image)

                        is_hovering = True


    
# ---------------------------------------- Computer's turn Function ------------------------------------------------------------------

def comp_game():
    global best_move, moves_list, player_2_or_comp, small_boards, current_board, moves, current_turn, game_running, board_turtle


    if current_turn == player_2_or_comp and game_running:
        
        print("Computer Started")

        moves_list = [-inf,-inf,-inf,-inf,-inf,-inf,-inf,-inf,-inf]

        empty_squares = 0
        for board in range(len(small_boards)):
            if check_gameover(small_boards[board]) == 0:
                for square in small_boards[board]:
                    if square == 0: empty_squares += 1

        # minimax is not run, but just returns the optimal board to play at when computer can play anywhere
        if (current_board == -1 or check_gameover(small_boards[current_board]) != 0):
            
            # minimax' depth must be increases as we progress into the game
            if moves < 10:
                minimax_results = minimax(small_boards, -1, min(level_info[0][0], empty_squares), -inf, inf, True)
            elif(moves < 18):
                minimax_results = minimax(small_boards, -1, min(level_info[0][1], empty_squares), -inf, inf, True)
            else:
                minimax_results = minimax(small_boards, -1, min(level_info[0][2], empty_squares), -inf, inf, True)

            current_board = minimax_results[1]

        # make quick deafualt move for the function to run
        best_move = -1
        for square in range(9):
            if small_boards[current_board][square] == 0:
                best_move = square
                break

        # best move is -1 only if the current board if full
        if best_move != -1:

            for square in range(9):

                # moves_list contains the sub-abstarct level score of each square
                if small_boards[current_board][square] == 0:
                    move_score = evaluateBestMove(small_boards[current_board], square) * 45
                    moves_list[square] = move_score

                if check_gameover(small_boards[current_board]) == 0:
                    
                    # minimax actually runs below if the square is empty
                    if small_boards[current_board][square] == 0:
                        small_boards[current_board][square] = player_2_or_comp

                        if moves < 20:
                            minimax_results = minimax(small_boards, square, min(level_info[1][0], empty_squares), -inf, inf, False)
                        elif moves < 32:
                            minimax_results = minimax(small_boards, square, min(level_info[1][1], empty_squares), -inf, inf, False)
                        else:
                            minimax_results = minimax(small_boards, square, min(level_info[1][2], empty_squares), -inf, inf, False)

                        minimax_score = minimax_results[0]
                        small_boards[current_board][square] = 0
                        moves_list[square] += minimax_score


            # choose the best move based on the results aquired
            for score in range(len(moves_list)):
                if moves_list[score] > moves_list[best_move]:
                    best_move = score

            # play the best move
            if small_boards[current_board][best_move] == 0:
                small_boards[current_board][best_move] = player_2_or_comp

                draw_and_check(current_board, best_move)


# ----------------------------------- player_1's turn function -------------------------------------------------------------

def play(mouse_x,mouse_y):
    global current_turn, main_board, current_board, game_running, board_turtle

    if game_type == 2:
        if not game_running: return
    else:
        if current_turn != player_1 or not game_running: return

    if game_type == 1:
        refresh_sheet()

    # get the indicies of small_boards on click
    small_board,square = mouse_2_board(mouse_x,mouse_y)

    # if player_1 can play on a certain board
    if current_board != -1:
        if small_board != current_board and small_boards[small_board][square] != 0: return
    else:
        if main_board[small_board] != 0 and small_boards[small_board][square] != 0: return


    small_boards[small_board][square] = current_turn

    draw_and_check(small_board,square)

    if game_type == 0:
        comp_game()
    elif game_type == 1:
        connect.send_data({'move':str(player_1), 'row': str(small_board), 'col': str(square)})


# ------------------------------------- Online Multiplayer --------------------------------------------------

def refresh_sheet():
    global connect, small_boards, main_board, last_move, current_turn

    print('refreshing')

    data = connect.get_all_data()

    if len(data['Data']) != 0:

        last_move = data['Data'][-1]

        if player_1 == last_move['move']:
            print('Other player has to make a move')
        else:

            if last_move['move'] == player_1:
                small_boards[int(last_move['row'])][int(last_move['col'])] = player_1
            else:
                small_boards[int(last_move['row'])][int(last_move['col'])] = player_2_or_comp

            draw_and_check(int(last_move['row']), int(last_move['col']))

            if int(last_move['move']) == 1:
                print(last_move['move'])
                current_turn = -1
            else:
                current_turn = 1

            print('refresed', current_turn)
    else:
        if player_1 == 1:
            print('its your turn')

def clear_sheet():
    global connect

    print('Deleting previous data...')

    delete_x = connect.delete_filtered_data('move', '1')
    delete_o = connect.delete_filtered_data('move', '-1')

    if delete_x['Status'] == True and delete_o['Status'] == True:
        print('Deleted data')


# --------------------------------------- Graphical ---------------------------------------------------

graphic_turtle = turtle.Turtle()
graphic_turtle.ht()
graphic_turtle.pu()
graphic_turtle.goto(1000,1000)

board_turtle = turtle.Turtle()
board_turtle.ht()

def draw_grid():
    board_turtle.color('red')
    x = -15
    for _ in range(31):
        board_turtle.pu()
        board_turtle.goto(x, 15)
        board_turtle.pd()
        board_turtle.goto(x, -15)
        x += 1

    y = 15
    for _ in range(31):
        board_turtle.pu()
        board_turtle.goto(-15, y)
        board_turtle.pd()
        board_turtle.goto(15, y)
        y -= 1

# draws an empty small board
def draw_single_board(start_x, start_y, end_x, end_y):

    h_gap = (end_x - start_x) / 3
    w_gap = (end_y -start_y) / 3

    for vertical_lines in range(1,3):
        board_turtle.pu()
        board_turtle.goto(start_x - (w_gap * vertical_lines), start_y)
        board_turtle.pd()
        board_turtle.goto(start_x - (w_gap * vertical_lines), end_y)

    for horizontal_lines in range(1,3):
        board_turtle.pu()
        board_turtle.goto(start_x, start_y - (h_gap * horizontal_lines))
        board_turtle.pd()
        board_turtle.goto(end_x, start_y - (h_gap * horizontal_lines))

# draws an empty full board
def draw_full_board():
    board_turtle.color(level_info[2])
    board_turtle.width(5)
    for big_board_rows in range(3):
        for big_board_cols in range(3):
            draw_single_board(-11+(8*big_board_cols),9-(8*big_board_rows),-5+(8*big_board_cols),3-(8*big_board_rows))

    board_turtle.width(10)
    draw_single_board(-12,10,12,-14)

def draw_x(x,y,type):
    if type == 'small':
        board_turtle.pu()
        board_turtle.goto(x,y)
        board_turtle.shape(planets[0][0])
        board_turtle.stamp()
    elif type == 'big':
        board_turtle.pu()
        board_turtle.goto(x,y)
        board_turtle.shape(planets[0][2])
        board_turtle.stamp()

def draw_circle(x,y,type):
    if type == 'small':
        board_turtle.pu()
        board_turtle.goto(x,y)
        board_turtle.shape(planets[1][0])
        board_turtle.stamp()
    elif type == 'big':
        board_turtle.pu()
        board_turtle.goto(x,y)
        board_turtle.shape(planets[1][2])
        board_turtle.stamp()


def display_available_boards():
    global current_board, current_turn, avail_b, main_highlight

    if current_turn == player_1:
        image = ImageTk.PhotoImage(file="images\\highlight_1.1.png")
    else:
        image = ImageTk.PhotoImage(file="images\\highlight_3.1.png")

    if current_board != -1:
        avail_b = []
        # deletes all elements(images) taged big_h
        canvas.delete('big_h')

        x,y = (board_2_coor(current_board, 4))

        x = (x * 778 / 30)
        y = -(y * 778 / 30)

        # used to display sem-transparent images as turtle dosent support it
        canvas.create_image(x, y, image=image, tags='big_h')
        avail_b.append(image)

    elif current_board == -1:
        avail_b = []
        # deletes all elements(images) taged big_h
        canvas.delete('big_h')

        for board in range(9):
            if main_board[board] == 0:

                x,y = (board_2_coor(board, 4))

                x = (x * 778 / 30)
                y = -(y * 778 / 30)
                
                # used to display sem-transparent images as turtle dosent support it
                canvas.create_image(x, y, image=image, tags='big_h')
                avail_b.append(image)

    draw_full_board()

    main_highlight = []
    # deletes all elements(images) taged big_h_p
    canvas.delete('big_h_p')

    for board in range(9):
        for square in range(9):
            draw(board,square)
        draw_main_board_condition(board)

    screen.update()


def draw_main_board_condition(board):
    global main_board, main_highlight

    if main_board[board] == 1:

        x,y = board_2_coor(board, 4)

        # used to display sem-transparent images as turtle dosent support it
        image = ImageTk.PhotoImage(file="images\\highlight_1.1.png")
        canvas.create_image((x * 778 / 30), -(y * 778 / 30), image=image, tags='big_h_p')
        main_highlight.append(image)

        for square in range(9):
            draw(board,square)

        row = board // 3
        col = board % 3

        start_x = -11 + (8 * col)
        start_y = 9 - (8 * row)
        end_x = -5 + (8 * col)
        end_y = 3 - (8 * row)

        board_turtle.width(5)

        draw_single_board(start_x,start_y,end_x,end_y)

        draw_x(x,y,'big')

    elif main_board[board] == -1:

        x,y = board_2_coor(board, 4)
        
        # used to display sem-transparent images as turtle dosent support it
        image = ImageTk.PhotoImage(file="images\\highlight_3.1.png")
        canvas.create_image((x * 778 / 30), -(y * 778 / 30), image=image, tags='big_h_p')
        main_highlight.append(image)

        for square in range(9):
            draw(board,square)

        row = board // 3
        col = board % 3

        start_x = -11 + (8 * col)
        start_y = 9 - (8 * row)
        end_x = -5 + (8 * col)
        end_y = 3 - (8 * row)

        board_turtle.width(5)

        draw_single_board(start_x,start_y,end_x,end_y)

        draw_circle(x,y,'big')


#
def draw(board,square):
    global small_boards

    x,y = board_2_coor(board,square)
    
    if small_boards[board][square] == player_1:
        draw_x(x,y,'small')
    if small_boards[board][square] == player_2_or_comp:
        draw_circle(x,y,'small')

# --------------------------------------- Menu graphics --------------------------------------------------------

button1 = turtle.Turtle()
button1.penup()
button1.goto(1000,1000)

button2 = turtle.Turtle()
button2.penup()
button2.goto(1000,1000)

button3 = turtle.Turtle()
button3.penup()
button3.goto(1000,1000)

button4 = turtle.Turtle()
button4.penup()
button4.goto(1000,1000)

button5 = turtle.Turtle()
button5.penup()
button5.goto(1000,1000)

button6 = turtle.Turtle()
button6.penup()
button6.goto(1000,1000)

button7 = turtle.Turtle()
button7.penup()
button7.goto(1000,1000)

image1 = turtle.Turtle()
image1.penup()
image1.goto(1000,1000)


def main_menu(x,y):
    global avail_b, hover_box_images, main_highlight, avail_b

    screen.onclick(None)

    board_turtle.clear()
    graphic_turtle.clear()
    avail_b = []
    hover_box_images = []
    main_highlight = []
    # deletes all elements(images) taged hover_box,big_h,big_h_p
    canvas.delete('hover_box')
    canvas.delete('big_h')
    canvas.delete('big_h_p')

    image1.goto(1000,1000)
    button5.goto(1000,1000)
    button6.goto(1000,1000)
    button7.goto(1000,1000)

    screen.update()

    reset_board()

    graphic_turtle.penup()
    graphic_turtle.goto(0,13)
    graphic_turtle.showturtle()
    graphic_turtle.shape('images\\space_xo_2.gif')

    button1.goto(0,3)
    button1.shape('images\\start.gif')
    button1.onclick(game_type_menu)

    button2.goto(0,-2)
    button2.shape('images\\options.gif')
    button2.onclick(options_menu)

    button3.goto(0,-7)
    button3.shape('images\\how_to_play.gif')
    button3.onclick(partial(how_to_play, 'menu'))

    button4.goto(0,-12)
    button4.shape('images\\quit.gif')
    button4.onclick(quit)

    screen.update()


def game_type_menu(x,y):

    button5.goto(1000,1000)
    image1.goto(1000,1000)

    button1.goto(0,3)
    button1.shape('images\\single_player.gif')
    button1.onclick(partial(setup_game, 0))

    button2.goto(0,-2)
    button2.shape('images\\online_multi.gif')
    button2.onclick(partial(setup_game, 1))

    button3.goto(0,-7)
    button3.shape('images\\offline_multi.gif')
    button3.onclick(partial(setup_game, 2))

    button4.goto(0,-12)
    button4.shape('images\\back.gif')
    button4.onclick(main_menu)

    screen.update()


def options_menu(x,y):

    button1.goto(1000,1000)
    button4.goto(1000,1000)
    button5.goto(1000,1000)
    
    image1.goto(-2,0)
    image1.shape('images\\music.gif')

    button2.goto(6,-1)
    if playing_music:
        button2.shape('images\\toggle_on.gif')
    else:
        button2.shape('images\\toggle_off.gif')
    button2.onclick(partial(music_button_graphic_update, 0))

    button3.goto(-2,-5)
    button3.shape('images\\difficulty.gif')
    button3.onclick(level_menu)

    button4.goto(-2,-10)
    button4.shape('images\\back.gif')
    button4.onclick(main_menu)

    screen.update()


def how_to_play(called_location,x,y):
    global slide_no,game_running,avail_b,hover_box_images,main_highlight

    game_running = False

    screen.onclick(None)

    board_turtle.clear()
    avail_b = []
    hover_box_images = []
    main_highlight = []
    # deletes all elements(images) taged hover_box,big_h,big_h_p
    canvas.delete('hover_box')
    canvas.delete('big_h')
    canvas.delete('big_h_p')

    button5.goto(1000,1000)
    button4.goto(1000,1000)

    slide_no = 1
    image1.goto(0,-0.5)
    image1.shape('images\\tutorial_1.gif')

    button5.goto(1000,1000)
    button5.shape('images\\s_back.gif')
    button5.onclick(partial(change_slide, 0))

    button6.goto(-5,-12)
    button6.shape('images\\close.gif')
    if called_location == 'menu':
        button6.onclick(main_menu)
    else:
        button6.onclick(continue_game)

    button7.goto(5,-12)
    button7.shape('images\\next.gif')
    button7.onclick(partial(change_slide, 1))

    screen.update()

def change_slide(button,x,y):
    global slide_no

    if button == 0:
        if slide_no != 1:
            slide_no -= 1
            image1.shape('images\\tutorial_'+str(slide_no)+'.gif')
    elif button == 1:
        if slide_no != 5:
            slide_no += 1
            image1.shape('images\\tutorial_'+str(slide_no)+'.gif')

    if slide_no != 1 and slide_no != 5:
        button5.goto(-10,-12)
        button6.goto(0,-12)
        button7.goto(10,-12)
    elif slide_no == 1:
        button5.goto(1000,1000)
        button6.goto(-5,-12)
        button7.goto(5,-12)
    elif slide_no == 5:
        button5.goto(-5,-12)
        button6.goto(5,-12)
        button7.goto(1000,1000)

    screen.update()


def flip_music_condition(condition):
    global playing_music

    if (playing_music) and (condition == False):
        playing_music = False
        winsound.PlaySound(None, winsound.SND_FILENAME)

    elif (not playing_music) and (condition == True):
        playing_music = True
        winsound.PlaySound(music,winsound.SND_LOOP + winsound.SND_ASYNC + winsound.SND_NODEFAULT)


def music_button_graphic_update(button,x,y):
    global playing_music

    if button == 0:
        button2.goto(6,-1)
        if playing_music:
            button2.shape('images\\toggle_off.gif')
            flip_music_condition(False)
        else:
            button2.shape('images\\toggle_on.gif')
            flip_music_condition(True)

    elif button == 1:
        button2.goto(17,2)
        if playing_music:
            button2.shape('images\\sound_off.gif')
            flip_music_condition(False)
        else:
            button2.shape('images\\sound_on.gif')
            flip_music_condition(True)

    screen.update()


def level_menu(x,y):

    button1.goto(-2,1)
    button1.shape('images\\easy.gif')
    button1.onclick(partial(set_level, 1))

    button2.goto(-2,-2)
    button2.shape('images\\normal.gif')
    button2.onclick(partial(set_level, 2))

    button3.goto(-2,-5)
    button3.shape('images\\intermediate.gif')
    button3.onclick(partial(set_level, 3))

    button4.goto(-2,-8)
    button4.shape('images\\hard.gif')
    button4.onclick(partial(set_level, 4))

    button5.goto(-2,-13)
    button5.shape('images\\back.gif')
    button5.onclick(options_menu)

    image1.shape('images\\arrow.gif')

    screen.update()
    update_arrow()

def update_arrow():
    image1.goto(6,4.3 - (level_info[0][0] * 3))

    screen.update()


def setup_game(input_game_type, x,y):
    global game_type

    graphic_turtle.hideturtle()

    button4.goto(1000,1000)
    button5.goto(1000,1000)
    image1.goto(1000,1000)

    button1.goto(17,5)
    button1.shape('images\\pause.gif')
    button1.onclick(pause_menu)

    button2.goto(17,2)
    if playing_music:
        button2.shape('images\\sound_on.gif')
    else:
        button2.shape('images\\sound_off.gif')
    button2.onclick(partial(music_button_graphic_update, 1))
    
    button3.goto(17,-1)
    button3.shape('images\\info.gif')
    button3.onclick(partial(how_to_play, 'in_game'))


    graphic_turtle.goto(0,14.75)
    graphic_turtle.shape('images\\space_xo_2.gif')
    graphic_turtle.stamp()
    graphic_turtle.goto(-10.25,-16)
    graphic_turtle.shape('images\\player_1.gif')
    graphic_turtle.stamp()
    graphic_turtle.goto(10,-16)
    if input_game_type == 0:
        graphic_turtle.shape('images\\comp.gif')
    else:
        graphic_turtle.shape('images\\player_2.gif')
    graphic_turtle.stamp()
    
    graphic_turtle.goto(-16.25,-15.9)
    graphic_turtle.shape(planets[0][1])
    graphic_turtle.stamp()
    graphic_turtle.goto(16.1,-15.9)
    graphic_turtle.shape(planets[1][1])
    graphic_turtle.stamp()

    
    game_type = input_game_type


    dis_choose_who_plays()  


    screen.update()


def set_level(diff_input,x,y):
    global level_info, image1, planets, music

    if diff_input == 1:
        level_info = [[1,2,3] , [2,3,4], '#edffcc']
        planets = [['planets\\1.1.gif','planets\\1.2.gif','planets\\1.3.gif'],['planets\\2.1.gif','planets\\2.2.gif','planets\\2.3.gif']]
        screen.bgpic('background\\'+str(randint(1,4))+'.gif')
        music = 'music\\1.wav'
        if playing_music:
            winsound.PlaySound(music,winsound.SND_LOOP + winsound.SND_ASYNC + winsound.SND_NODEFAULT)

    elif diff_input == 2:
        level_info = [[2,3,4] , [3,4,5], '#f6d6bc']
        planets = [['planets\\3.1.gif','planets\\3.2.gif','planets\\3.3.gif'],['planets\\4.1.gif','planets\\4.2.gif','planets\\4.3.gif']]
        screen.bgpic('background\\'+str(randint(5,8))+'.gif')
        music = 'music\\2.wav'
        if playing_music:
            winsound.PlaySound(music,winsound.SND_LOOP + winsound.SND_ASYNC + winsound.SND_NODEFAULT)

    elif diff_input == 3:
        level_info = [[3,4,5] , [4,5,6], '#f4e1ff']
        planets = [['planets\\5.1.gif','planets\\5.2.gif','planets\\5.3.gif'],['planets\\6.1.gif','planets\\6.2.gif','planets\\6.3.gif']]
        screen.bgpic('background\\'+str(randint(9,12))+'.gif')
        music = 'music\\3.wav'
        if playing_music:
            winsound.PlaySound(music,winsound.SND_LOOP + winsound.SND_ASYNC + winsound.SND_NODEFAULT)

    elif diff_input == 4:
        level_info = [[4,5,6] , [5,6,7], '#ddca7d']
        planets = [['planets\\7.1.gif','planets\\7.2.gif','planets\\7.3.gif'],['planets\\8.1.gif','planets\\8.2.gif','planets\\8.3.gif']]
        screen.bgpic('background\\'+str(randint(13,16))+'.gif')
        music = 'music\\4.wav'
        if playing_music:
            winsound.PlaySound(music,winsound.SND_LOOP + winsound.SND_ASYNC + winsound.SND_NODEFAULT)


    update_arrow()


def quit(x,y):
    turtle.bye()    


def dis_choose_who_plays():

    image1.goto(0,0)
    image1.shape('images\\choose_play.gif')

    if game_type == 0:
        button5.goto(-6,3)
        button5.shape('images\\select_p1.gif')
        button5.onclick(partial(set_and_run_who_plays, player_1))

        button6.goto(6,3)
        button6.shape('images\\select_comp.gif')
        button6.onclick(partial(set_and_run_who_plays, player_2_or_comp))

        button7.goto(0,-3)
        button7.shape('images\\select_random.gif')
        button7.onclick(partial(set_and_run_who_plays, 0))

    elif game_type == 1:
        button5.goto(-6,0)
        button5.shape('images\\select_p1.gif')
        button5.onclick(partial(set_and_run_who_plays, player_1))

        button6.goto(6,0)
        button6.shape('images\\select_p2.gif')
        button6.onclick(partial(set_and_run_who_plays, player_2_or_comp))

    elif game_type == 2:
        button5.goto(-6,3)
        button5.shape('images\\select_p1.gif')
        button5.onclick(partial(set_and_run_who_plays, player_1))

        button6.goto(6,3)
        button6.shape('images\\select_p2.gif')
        button6.onclick(partial(set_and_run_who_plays, player_2_or_comp))

        button7.goto(0,-3)
        button7.shape('images\\select_random.gif')
        button7.onclick(partial(set_and_run_who_plays, 0))


def set_and_run_who_plays(player,x,y):
    global game_running, current_turn, first_turn

    game_running = True

    image1.goto(1000,1000)
    button5.goto(1000,1000)
    button6.goto(1000,1000)
    button7.goto(1000,1000)


    if game_type == 1:
        clear_sheet()

    if player == 0:
        player = choice([1,-1])

    if player == player_1:
        current_turn = player_1
        first_turn = player_1
        display_available_boards()
    else:
        current_turn = player_2_or_comp
        first_turn = player_2_or_comp
        display_available_boards()
        comp_game()

    screen.onclick(play)
    canvas.bind("<Motion>", on_motion)

    screen.update()

def dis_gameover(winner):
    global game_running,avail_b,hover_box_images,main_highlight

    game_running = False

    screen.onclick(None)

    board_turtle.clear()
    avail_b = []
    hover_box_images = []
    main_highlight = []
    # deletes all elements(images) taged hover_box,big_h,big_h_p
    canvas.delete('hover_box')
    canvas.delete('big_h')
    canvas.delete('big_h_p')

    image1.goto(0,0)
    if winner == 0:
        image1.shape('images\\game_tie.gif')
    elif winner == 1:
        image1.shape('images\\player_1_won.gif')
    elif winner == -1:
        if game_type == 0:
            image1.shape('images\\comp_won.gif')
        else:
            image1.shape('images\\player_2_won.gif')

    button5.goto(-5,-3)
    button5.shape('images\\restart.gif')
    button5.onclick(restart)

    button6.goto(7,-3)
    button6.shape('images\\quit.gif')
    button6.onclick(main_menu)

    screen.update()

def pause_menu(x,y):
    global game_running,avail_b,hover_box_images,main_highlight

    game_running = False

    screen.onclick(None)

    board_turtle.clear()
    avail_b = []
    hover_box_images = []
    main_highlight = []
    # deletes all elements(images) taged hover_box,big_h,big_h_p
    canvas.delete('hover_box')
    canvas.delete('big_h')
    canvas.delete('big_h_p')

    image1.goto(0,0)
    image1.shape('images\\game_paused.gif')

    button5.goto(0,4.5)
    button5.shape('images\\restart.gif')
    button5.onclick(restart)

    button6.goto(0,-0.5)
    button6.shape('images\\quit.gif')
    button6.onclick(main_menu)

    button7.goto(0,-5.5)
    button7.shape('images\\back.gif')
    button7.onclick(continue_game)

    screen.update()

def restart(x,y):
    global game_running,current_turn
    game_running = True

    image1.goto(1000,1000)
    button5.goto(1000,1000)
    button6.goto(1000,1000)
    button7.goto(1000,1000)
    
    reset_board()

    current_turn = first_turn
    draw_full_board()
    display_available_boards()
    if current_turn == player_1:
        screen.onclick(play)
    else:
        comp_game()

def continue_game(x,y):
    global game_running
    game_running = True

    image1.goto(1000,1000)
    button5.goto(1000,1000)
    button6.goto(1000,1000)
    button7.goto(1000,1000)

    for board in range(9):
        for elements in range(9):
            draw(board, elements)

    display_available_boards()

    screen.onclick(play)

    screen.update()



async def main():
    global playing_music

    playing_music = False
    flip_music_condition(True)
    main_menu(None,None)

    await asyncio.sleep(0)

    turtle.mainloop()
    

asyncio.run(main())