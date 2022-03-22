# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([750,750])

# Run until the user asks to quit
running = True
print(running)
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Fill the background with white (255, 255, 255)
    screen.fill((100, 100, 100))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip

# Done - time to quit
pygame.quit()