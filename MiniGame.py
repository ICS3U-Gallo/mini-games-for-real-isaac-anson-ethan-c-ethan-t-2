import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(320, 240, 16, 16)
    def move(self, px, py):
        if px != 0:
            self.move_single_axis(px, 0)
        if py != 0:
            self.move_single_axis(0, py)
    def move_single_axis(self, px, py):
        self.rect.x += px
        self.rect.y += py
    def getposx(self):
        return self.rect.x
    def getposy(self):
        return self.rect.y
player = Player()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player.getposx() > 0:
        player.move(-2, 0)
    if key[pygame.K_RIGHT] and player.getposx() < WIDTH - player.rect.width:
        player.move(2, 0)
    if key[pygame.K_UP] and player.getposy() > 0:
        player.move(0, -2)
    if key[pygame.K_DOWN] and player.getposy() < HEIGHT - player.rect.height:
        player.move(0, 2)
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), player.rect)
    pygame.display.flip()