"""
Graphical user interface to play the Hasami Shogi Game built in CS 162 using the PyGame module. 
Requires pygame module to be installed on the running system/platform.
Written by Steven Tran
Date: 3/24/2022
"""

import pygame
import HasamiShogiGame
import math

# CONSTANTS
WINDOW_WIDTH = 760
WINDOW_HEIGHT = 760
ROWS, COLS = 9, 9
SQUARE_SIZE = WINDOW_WIDTH / ROWS
RED = (180, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_COLOR = (252, 242, 183)
HIGHLIGHT = (0,255,255)
FPS = 20
TITLE_FONT_SIZE = 90

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption("Hasami Shogi v1.0 by Steven Tran")

# Game Piece Images, scaled to fit the square size
red_piece_og = pygame.image.load("red_shogi.png")
red_piece = pygame.transform.scale(red_piece_og, (SQUARE_SIZE, SQUARE_SIZE))

black_piece_og = pygame.image.load("black_shogi.png")
black_piece = pygame.transform.scale(black_piece_og, (SQUARE_SIZE, SQUARE_SIZE))

def main(): 
    def soundEffect(soundFile):
        """Plays a sound effect file

        Args:
            soundFile (*.wav, *.ogg): audio file for the sound effect
        """
        soundFx = pygame.mixer.Sound(soundFile)
        soundFx.play()

    def showText(display_surface, textToDisplay, textColor):
        """Displays the text on the surface of the pygame window

        Args:
            display_surface (_type_): the pygame surface to be drawn on
            textToDisplay (str): desired text to be displayed
            textColor (tuple): RGB colors (0~255, 0~255, 0~255)
        """
        custom_font = pygame.font.Font('Kamikaze.ttf', TITLE_FONT_SIZE)
        title_text = custom_font.render(textToDisplay, True, textColor)
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        display_surface.blit(title_text, title_text_rect)
        pygame.display.update()

    def mouse_pos_to_square(position):
        """Converts pygame's mouse click selection to a valid index for HasamiShogiGame.py

        Args:
            position (tuple): pygame's mouse position event

        Returns:
            str: the square's index that is selected
        """
        mouse_y = math.floor(position[0] / (WINDOW_WIDTH / ROWS))
        mouse_x = math.floor(position[1] / (WINDOW_HEIGHT / COLS))
        return str(mouse_x) + str(mouse_y)

    game = HasamiShogiGame.HasamiShogiGame()
    clock = pygame.time.Clock()
    soundEffect("japanese_yooo.wav")
    showText(screen, "HASAMI SHOGI", WHITE)
    pygame.time.wait(2500)

    clicks = []
    move_started = False
    while game.get_game_state() == "UNFINISHED":
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # Exits if the user clicks on the Exit window button.
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                selection = (mouse_pos_to_square(event.pos))
                allowed_sq = game.index_to_move(selection)
                if len(clicks) == 0 and game.get_square_occupant(allowed_sq) == game.get_active_player():
                    clicks.append(selection)
                    # ACTION: Add highlighted square for desired piece to be moved. Would also require removal.
                    # pygame.draw.rect(screen, HIGHLIGHT, pygame.rect(SQUARE_SIZE * int(selection[0]),  SQUARE_SIZE, SQUARE_SIZE * int(selection[0]) + .5 * SQUARE_SIZE), .4 * SQUARE_SIZE, 1)
                    # pygame.draw.rect(screen, HIGHLIGHT, pygame.Rect(50, 50, 100, 100), 5)
                elif len(clicks) == 1 and game.get_square_occupant(allowed_sq) == "NONE":
                    clicks.append(selection)
                    source = game.index_to_move(clicks[0])
                    destination = game.index_to_move(clicks[1])
                    move = game.make_move(source, destination)
                    if move == True:
                        print(f"Moving {source} → {destination}")
                    clicks = []

        # Fill the background with BOARD_COLOR
        screen.fill(BOARD_COLOR)

        # Draws the grid lines of the board
        for col in range(0, COLS):
            x = col * WINDOW_WIDTH // COLS
            pygame.draw.line(screen, (0,0,0), (x,0), (x, WINDOW_HEIGHT), width=1)
        for row in range(0, ROWS):
            y = row * WINDOW_HEIGHT // ROWS
            pygame.draw.line(screen, (0,0,0), (0,y), (WINDOW_WIDTH, y), width=1)     
        
        # Displays the pieces on the game board
        for row in range(ROWS):
            for col in range(COLS):
                space = str(row) + str(col)
                if game.get_square_occupant(game.index_to_move(space)) == "RED":
                    # pygame.draw.circle(screen, RED, (SQUARE_SIZE * col + .5 * SQUARE_SIZE, SQUARE_SIZE * row + .5 * SQUARE_SIZE), .4 * SQUARE_SIZE, 40)
                    # BLIT the red piece surface object in the correct square
                    screen.blit(red_piece, (SQUARE_SIZE * col , SQUARE_SIZE * row))
                    #pygame.draw.circle(screen, RED, (SQUARE_SIZE * row, SQUARE_SIZE * col), 75)
                
                elif game.get_square_occupant(game.index_to_move(space)) == "BLACK":
                    # pygame.draw.circle(screen, BLACK, (SQUARE_SIZE * col + .5 * SQUARE_SIZE, SQUARE_SIZE * row + .5 * SQUARE_SIZE), .4 * SQUARE_SIZE, 40)
                    screen.blit(black_piece, (SQUARE_SIZE * col, SQUARE_SIZE * row))
                else:
                    pass
        
        # Displays the match winner
        if game.get_game_state() == "RED_WON":
            showText(screen, "RED WINS", RED)
            soundEffect("japanese_clapper.wav")
        elif game.get_game_state() == "BLACK_WON":
            showText(screen, "BLACK WINS", BLACK)
            soundEffect("japanese_clapper.wav")

        # Updates the game screen
        pygame.display.update()
        pygame.time.wait(60)
        
    print("Thank you for playing! The game will be closing shortly.")
    pygame.time.wait(5500)
    pygame.quit()

if __name__ == "__main__":
    main()