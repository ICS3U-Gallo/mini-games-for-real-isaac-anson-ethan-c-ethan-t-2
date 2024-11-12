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
player_y = HEIGHT - 25

bullets = []
lives = 3
alienx = 0
speed = 5
score = 0
# ---------------------------
if lives <= 0:
    running = False
    
running = True
while running == True:
    # EVENT HANDLING
    if lives <= 0:
        running = False
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
    alienx += speed
    if alienx >= 585:
        speed *= -1
    elif alienx <= -640:
        speed *= -1
    
    for pos in bullets:
        pos[1] -= 20
    
    player =1
    alien =1
    
    # DRAWING
    screen.fill((0, 0, 0))  # always the first drawing command

    for x, y in stars:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 2, 2))

    #Alien
    body = pygame.draw.rect(screen, (0,255,0), (alienx+645,5,55,45))
    
    pygame.draw.rect(screen, (0,0,0), (alienx+645,5,5,20))
    pygame.draw.rect(screen, (0,0,0), (alienx+645,40,5,10))
    pygame.draw.rect(screen, (0,0,0), (alienx+650,5,5,15))
    pygame.draw.rect(screen, (0,0,0), (alienx+650,30,5,20))
    pygame.draw.rect(screen, (0,0,0), (alienx+655,10,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+655,45,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+660,5,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+660,20,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+660,40,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+665,5,5,10))
    pygame.draw.rect(screen, (0,0,0), (alienx+665,40,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+670,5,5,10))
    pygame.draw.rect(screen, (0,0,0), (alienx+670,40,5,10))
    pygame.draw.rect(screen, (0,0,0), (alienx+675,5,5,10))
    pygame.draw.rect(screen, (0,0,0), (alienx+675,40,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+680,5,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+680,20,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+680,40,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+685,10,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+685,45,5,5))
    pygame.draw.rect(screen, (0,0,0), (alienx+690,5,5,15))
    pygame.draw.rect(screen, (0,0,0), (alienx+690,30,5,20))
    pygame.draw.rect(screen, (0,0,0), (alienx+695,5,5,20))
    pygame.draw.rect(screen, (0,0,0), (alienx+695,40,5,10))
    
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
        laser = pygame.draw.rect(screen, (255,0,0), (center[0], center[1], 5, 25))
        #print(bullet)
        #print(center)
    #Collision
        hit = pygame.Rect.colliderect(body, laser)
    
        if hit == True:
            score += 1
            running = False
      
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()