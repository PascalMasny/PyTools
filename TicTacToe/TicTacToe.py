#Imports
import pygame
import sys
import numpy as np

#pygame init 
pygame.init()

#---Const---
#Screen
WIDTH = 600
HEIGHT = 600

#Linie
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
SQUARE_SIZE = 200

#board frontend
BOARD_ROWS = 3
BOARD_COLS = 3

# O & X
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

#Farben 
BG_COLOR = (42, 157, 143)
LINE_COLOR = (38, 70, 83)
CIRCLE_COLOR = (231, 111, 81)
CROSS_COLOR = (233, 196, 106)

#Screen
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

#board backend
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )



#Linie zecihenen
def draw_lines():

	# h1 
	pygame.draw.line( screen, LINE_COLOR, (25, SQUARE_SIZE), (WIDTH - 25, SQUARE_SIZE), LINE_WIDTH )
	# h2
	pygame.draw.line( screen, LINE_COLOR, (25, 2 * SQUARE_SIZE), (WIDTH - 25, 2 * SQUARE_SIZE), LINE_WIDTH )

	# v1
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 25), (SQUARE_SIZE, HEIGHT - 25), LINE_WIDTH )
	# v2
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 25), (2 * SQUARE_SIZE, HEIGHT - 25), LINE_WIDTH )

# X & O Zeci
def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

#kasten setzten
def mark_square(row, col, player):
	board[row][col] = player

#kasten checken
def available_square(row, col):
	return board[row][col] == 0

#board vol check
def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False

	return True

#gewinner check
def check_win(player):
	
    #vertikaler check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	#orizontaler check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	#diagonale nach nach oben check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	#diagonale nach nach unten check
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

#zeichen vertikale linie
def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

#zeichen orizontale linie
def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

#zeichne diagonal linie nach oben
def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

#zeichne diagonal linie nach unten
def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

#restart
def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0


#grid zeichnen
draw_lines()

#game Variablen
player = 1
game_over = False


#main
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0] #X
			mouseY = event.pos[1] #Y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)


			if available_square( clicked_row, clicked_col ):

				mark_square( clicked_row, clicked_col, player )
				if check_win( player ):
					game_over = True
				player = player % 2 + 1

				draw_figures()


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()