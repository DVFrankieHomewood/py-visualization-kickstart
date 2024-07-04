import pygame
import math

pygame.init()

screen = pygame.display.set_mode([500, 500])

counter = 0
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    x = 250
    y = 250
    height = 100
    width = 100
    rotation = counter
    color='#ff0000'

    points = []
    radius = math.sqrt((height / 2)**2 + (width / 2)**2)
    angle = math.atan2(height / 2, width / 2)
    angles = [angle, -angle + math.pi, angle + math.pi, -angle]
    rot_radians = (math.pi / 180) * rotation

    # Calculate the coordinates of each point.
    for angle in angles:
        y_offset = -1 * radius * math.sin(angle + rot_radians)
        x_offset = radius * math.cos(angle + rot_radians)
        points.append((x + x_offset, y + y_offset))

    pygame.draw.polygon(screen, color, points)
    
    counter -= 1/5
    # Flip the display
    pygame.display.flip()

pygame.quit()
