# Simple pygame program
# Import and initialize the pygame library

import pygame
import HasamiShogiGame
import time

# CONSTANTS
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
ROWS, COLS = 9, 9
SQUARE_SIZE = WINDOW_WIDTH // ROWS
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BOARD_COLOR = (232, 212, 153)
FPS = 60

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption("Hasami Shogi v1.0")

def main(): 
    pygame.init()
    game = HasamiShogiGame.HasamiShogiGame()
    clock = pygame.time.Clock()
    # Run until there is a winner
    while game.get_game_state() == "UNFINISHED":
        clock.tick(FPS)

        # Did the user click the window close button?
        for event in pygame.event.get():
            mouse_buttons = pygame.mouse.get_pressed()
            mouse_position = pygame.mouse.get_pos()

            if mouse_buttons[0]:
                print("LEFT BUTTON PRESSED!")
                print(mouse_position)
                src = mouse_position
                if mouse_buttons[0]:
                    dst = mouse_position
        def mouse_pos_to_square(mouse_position):
            


            if event.type == pygame.QUIT:
                game = False

        # Fill the background with BOARD_COLOR
        screen.fill(BOARD_COLOR)

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        for col in range(0, COLS):
            x = col * WINDOW_WIDTH // COLS
            pygame.draw.line(screen, (0,0,0), (x,0), (x, WINDOW_HEIGHT), width=1)
        for row in range(0, ROWS):
            y = row * WINDOW_HEIGHT // ROWS
            pygame.draw.line(screen, (0,0,0), (0,y), (WINDOW_WIDTH, y), width=1)
        #
        # 
        #  print(game.get_game_board())
        
        
        for row in range(ROWS):
            for col in range(COLS):
                print("row and column is", row, col)
                space = str(row) + str(col)
                if game.get_square_occupant(game.index_to_move(space)) == "RED":
                    pygame.draw.circle(screen, RED, (SQUARE_SIZE * col + .5 * SQUARE_SIZE, SQUARE_SIZE * row + .5 * SQUARE_SIZE), .4 * SQUARE_SIZE, 1)
                    #pygame.draw.circle(screen, RED, (SQUARE_SIZE * row, SQUARE_SIZE * col), 75)
                elif game.get_square_occupant(game.index_to_move(space)) == "_":
                    pygame.draw.rect(screen, BOARD_COLOR, (SQUARE_SIZE * col + .5 * SQUARE_SIZE, SQUARE_SIZE * row + .5 * SQUARE_SIZE), .4 * SQUARE_SIZE, 1)
                    pass
                elif game.get_square_occupant(game.index_to_move(space)) == "BLACK":
                    pygame.draw.circle(screen, BLACK, (SQUARE_SIZE * col + .5 * SQUARE_SIZE, SQUARE_SIZE * row + .5 * SQUARE_SIZE), .4 * SQUARE_SIZE, 1)
        #     print(game.move_to_index])



    # Flip the display
        pygame.display.update()

    # Done! Time to quit.
    time.sleep(10)
    pygame.quit()

main()