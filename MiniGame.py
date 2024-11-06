import pygame
import random 

pygame.init()

WIDTH, HEIGHT = 640, 480
TILE_SIZE = 16
MAXWIDTH, MAXHEIGHT = 1280, 960
encounter = 0.1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
battle = False
#pokemon
class Pokemon:
    def __init__(self, name, poke_type, level, hp, attack, defense, speed, maxxp):
        self.name = name                
        self.poke_type = poke_type      
        self.level = level              
        self.hp = hp                    
        self.max_hp = hp               
        self.attack = attack            
        self.defense = defense          
        self.speed = speed              
        self.current_hp = hp  
        self.xp = 0
        self.maxxp = maxxp
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense  # Basic damage calculation
        if damage < 0:
            damage = 0  # Ensure damage is not negative
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)
    def level_up(self):
        self.level += 1
        self.max_hp += 5
        self.attack += 2
        self.defense += 1
        self.speed += 1
        self.current_hp = self.max_hp  # Fully heal on level up
        print( self.name + " leveled up to level " + self.level + "!")

    def display_stats(self):
        print(self.name + " - Level: " + self.level)
        print("HP: " + self.current_hp/self.max_hp)
        print("Attack: " + self.attack)
        print("Defense: " + self.defense)
        print("Speed: " + self.speed)
#player
class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(320, 240, TILE_SIZE, TILE_SIZE)
        self.speed = TILE_SIZE  # Move one tile at a time
        self.move_delay = 150
        self.last_move = pygame.time.get_ticks()

    def move(self, dx, dy, barriers):
        # Calculate the next position
        time_now = pygame.time.get_ticks()
        if time_now - self.last_move >= self.move_delay:
            next_rect = self.rect.move(dx * self.speed, dy * self.speed)
            if not any(next_rect.colliderect(barrier) for barrier in barriers):
                self.rect = next_rect  # Update position if no collision
                if self.rect.right > camera_rect.right:
                    camera_rect.x = min(camera_rect.x + self.speed, MAXWIDTH - WIDTH)
                elif self.rect.left < camera_rect.left:
                    camera_rect.x = max(camera_rect.x - self.speed, 0)
                if self.rect.bottom > camera_rect.bottom:
                    camera_rect.y = min(camera_rect.y + self.speed, MAXHEIGHT - HEIGHT)
                elif self.rect.top < camera_rect.top:
                    camera_rect.y = max(camera_rect.y - self.speed, 0)
            self.last_move = time_now
        return camera_rect
    def getposx(self):
        return self.rect.x
    def getposy(self):
        return self.rect.y
player = Player()
camera_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
# Example barriers (like trees or walls in Pokémon)
barriers = [
    pygame.Rect(100, 100, TILE_SIZE, TILE_SIZE),
    pygame.Rect(200, 200, TILE_SIZE, TILE_SIZE),
    pygame.Rect(300, 400, TILE_SIZE, TILE_SIZE)
]
#grass 
grass = [
    pygame.Rect(1000, 200, TILE_SIZE, TILE_SIZE),
    pygame.Rect(500, 700, TILE_SIZE, TILE_SIZE),
    pygame.Rect(300, 300, TILE_SIZE, TILE_SIZE)
]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and player.getposx() > 0:
        player.move(-1, 0, barriers)
    if keys[pygame.K_RIGHT] and player.getposx() < MAXWIDTH - player.rect.width:
        player.move(1, 0, barriers)
    if keys[pygame.K_UP] and player.getposy() > 0:
        player.move(0, -1, barriers)
    if keys[pygame.K_DOWN]and player.getposy() < MAXHEIGHT - player.rect.height:
        player.move(0, 1, barriers)

    screen.fill((255, 255, 255))

    # Draw the player and barriers
    player_on_screen = player.rect.move(-camera_rect.x, -camera_rect.y)
    pygame.draw.rect(screen, (0, 0, 255), player_on_screen)
    for barrier in barriers:
        barrier_on_screen = barrier.move(-camera_rect.x, -camera_rect.y)
        pygame.draw.rect(screen, (255, 0, 0), barrier_on_screen)  # Green barriers
    for grass_tile in grass:
        grass_on_screen = grass_tile.move(-camera_rect.x, -camera_rect.y)
        pygame.draw.rect(screen, (0, 255, 0), grass_on_screen)
        if player.rect.colliderect(grass_tile):
            if random.random() < encounter:
                battle = True
    while battle:

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
