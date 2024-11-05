import random
import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
stars = []
for _ in range(100):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    pos = (x, y)
    stars.append(pos)

player_x = WIDTH // 2
player_y = HEIGHT - 50

bullets = []
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            # create a bullet - add to bullet list
            bullet = [player_x, player_y - 25]
            bullets.append(bullet)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player_x = mouse_x
    
    for pos in bullets:
        pos[1] -= 10


    # DRAWING
    screen.fill((0, 0, 0))  # always the first drawing command

    for x, y in stars:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 2, 2))

    
    # PLAYER
    pygame.draw.rect(screen, (0,255,0), (mouse_x -30,685,5,25))
    pygame.draw.rect(screen, (0,255,0), (mouse_x -25,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x -20,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x -15,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x -10,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x -5,670,5,40))
    pygame.draw.rect(screen, (0,255,0), (mouse_x,665,5,45))
    pygame.draw.rect(screen, (0,255,0), (mouse_x +5,670,5,40))
    pygame.draw.rect(screen, (0,255,0), (mouse_x +10,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x +15,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x +20,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x +25,680,5,30))
    pygame.draw.rect(screen, (0,255,0), (mouse_x +30,685,5,25))
    
    # BULLETS
    for center in bullets:
        pygame.draw.circle(screen, (255, 0, 0), center, 10)
        #pygame.draw.rect(screen, (255,255,255), (center,5,25))

    # Must be the last two liness
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()