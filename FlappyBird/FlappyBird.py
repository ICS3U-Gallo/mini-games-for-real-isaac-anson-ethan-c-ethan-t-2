import pygame

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

background_color = (136, 194, 219)
ground_color = (34, 139, 34)
ground_height = 100

white = (255, 255, 255)
black = (0, 0, 0)
brown = (139, 69, 19)
light_brown = (205, 133, 63)
red = (255, 0, 0)
blue = (192, 245, 239)
bluer = (56, 66, 205)
green = (30, 104, 30)
sky_blue = (135, 206, 235)

bird1_x = -50
bird1_y = 100
bird2_x = -150  
bird2_y = 120
bird3_x = -250  
bird3_y = 140
bird_speed = 5  

def draw_cloud(screen, x, y):
    pygame.draw.circle(screen, white, (x, y), 30)
    pygame.draw.circle(screen, white, (x + 30, y), 40)
    pygame.draw.circle(screen, white, (x + 60, y), 30)
    pygame.draw.circle(screen, white, (x + 20, y - 20), 25)
    pygame.draw.circle(screen, white, (x + 45, y - 20), 25)

def draw_tree(screen, x, y):
    trunk_width = 20
    trunk_height = 60
    pygame.draw.rect(screen, brown, (x, y, trunk_width, trunk_height))
    pygame.draw.circle(screen, green, (x + 10, y - 20), 30)
    pygame.draw.circle(screen, green, (x - 20, y - 10), 25)
    pygame.draw.circle(screen, green, (x + 40, y - 10), 25)
    pygame.draw.circle(screen, green, (x + 10, y - 40), 25)

def draw_bird_v(screen, x, y, size=20):
    left_wing = [(x, y), (x - size, y - size), (x, y - size // 2)]
    right_wing = [(x, y), (x + size, y - size), (x, y - size // 2)]
    pygame.draw.polygon(screen, black, left_wing)
    pygame.draw.polygon(screen, black, right_wing)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bird1_x += bird_speed
    bird2_x += bird_speed
    bird3_x += bird_speed

    if bird1_x > WIDTH:
        bird1_x = -50
    if bird2_x > WIDTH:
        bird2_x = -50
    if bird3_x > WIDTH:
        bird3_x = -50

    screen.fill(background_color)
    pygame.draw.rect(screen, (106, 181, 106), (0, 300, 640, 100))
    pygame.draw.rect(screen, ground_color, (0, 350, 640, 150))

    draw_cloud(screen, 30, 40)
    draw_cloud(screen, 270, 60)
    draw_cloud(screen, 550, 50)
    draw_cloud(screen, 400, 100)
    draw_cloud(screen, 170, 120)

    draw_tree(screen, 100, HEIGHT - ground_height - 60)
    draw_tree(screen, 300, HEIGHT - ground_height - 60)
    draw_tree(screen, 500, HEIGHT - ground_height - 60)

    house_x, house_y = 150, 300
    house_width, house_height = 100, 75
    pygame.draw.rect(screen, light_brown, (house_x, house_y, house_width, house_height))
    roof_points = [(house_x, house_y), (house_x + house_width, house_y), (house_x + house_width // 2, house_y - 50)]
    pygame.draw.polygon(screen, bluer, roof_points)
    door_x, door_y = house_x + house_width // 2 - 12, house_y + house_height - 30
    door_width, door_height = 25, 30
    pygame.draw.rect(screen, brown, (door_x, door_y, door_width, door_height))
    window_size = 20
    pygame.draw.rect(screen, blue, (house_x + 10, house_y + 10, window_size, window_size))
    pygame.draw.rect(screen, blue, (house_x + house_width - 30, house_y + 10, window_size, window_size))

    house_x, house_y = 300, 300
    house_width, house_height = 200, 150
    pygame.draw.rect(screen, light_brown, (house_x, house_y, house_width, house_height))
    roof_points = [(house_x, house_y), (house_x + house_width, house_y), (house_x + house_width // 2, house_y - 100)]
    pygame.draw.polygon(screen, red, roof_points)
    door_x, door_y = house_x + house_width // 2 - 25, house_y + house_height - 60
    door_width, door_height = 50, 60
    pygame.draw.rect(screen, brown, (door_x, door_y, door_width, door_height))
    window_size = 40
    pygame.draw.rect(screen, blue, (house_x + 20, house_y + 20, window_size, window_size))
    pygame.draw.rect(screen, blue, (house_x + house_width - 60, house_y + 20, window_size, window_size))

    draw_bird_v(screen, bird1_x, bird1_y, size=20)
    draw_bird_v(screen, bird2_x, bird2_y, size=20)
    draw_bird_v(screen, bird3_x, bird3_y, size=20)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()