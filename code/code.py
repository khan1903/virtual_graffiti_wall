import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virtual Graffiti Wall")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPRAY_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]

# Set up spray effect
spray_radius = 15  # The radius of each spray
spray_density = 50  # Number of spray particles per "click"

# Set up the brush position
brush_pos = (0, 0)

# Create the clock object for controlling the frame rate
clock = pygame.time.Clock()

# Create the graffiti wall
screen.fill(WHITE)

# Flag to check if eraser is active
eraser_active = False
# Flag to check if move mode is active
move_mode = False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Toggle eraser mode with the 'E' key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                eraser_active = not eraser_active  # Toggle eraser on/off
                print(f"Eraser {'Activated' if eraser_active else 'Deactivated'}")
            # Toggle move mode with the 'M' key
            if event.key == pygame.K_m:
                move_mode = not move_mode  # Toggle move mode on/off
                print(f"Move Mode {'Activated' if move_mode else 'Deactivated'}")

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # If move mode is activated, don't paint or erase, just move the cursor freely
    if not move_mode:
        # If the mouse button is pressed, either spray paint or erase
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            if eraser_active:
                # Erase paint by drawing white circles (erase effect)
                for _ in range(spray_density):
                    offset_x = random.randint(-spray_radius, spray_radius)
                    offset_y = random.randint(-spray_radius, spray_radius)
                    if 0 <= mouse_x + offset_x < screen_width and 0 <= mouse_y + offset_y < screen_height:
                        pygame.draw.circle(screen, WHITE, (mouse_x + offset_x, mouse_y + offset_y), random.randint(2, 5))
            else:
                # Spray paint by drawing colored circles
                for _ in range(spray_density):
                    offset_x = random.randint(-spray_radius, spray_radius)
                    offset_y = random.randint(-spray_radius, spray_radius)
                    if 0 <= mouse_x + offset_x < screen_width and 0 <= mouse_y + offset_y < screen_height:
                        color = random.choice(SPRAY_COLORS)
                        pygame.draw.circle(screen, color, (mouse_x + offset_x, mouse_y + offset_y), random.randint(2, 5))

    # Draw the current position of the brush (optional)
    if not move_mode:
        pygame.draw.circle(screen, BLACK, (mouse_x, mouse_y), spray_radius // 2, 1)

    # Update the screen
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
