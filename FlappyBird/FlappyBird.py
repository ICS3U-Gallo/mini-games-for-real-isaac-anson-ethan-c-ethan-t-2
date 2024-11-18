import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (40, 30))

pipe_image = pygame.image.load("pipe.png").convert_alpha()
pipe_image = pygame.transform.scale(pipe_image, (80, HEIGHT))

BIRD_WIDTH, BIRD_HEIGHT = 40, 30
GRAVITY = 0.8
JUMP_STRENGTH = -12
bird_y_velocity = 0
bird_rect = pygame.Rect(50, HEIGHT // 2, BIRD_WIDTH, BIRD_HEIGHT)

PIPE_WIDTH = 80
PIPE_GAP = 200
pipe_speed = 4
pipes = []

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
score = 0
game_started = False
game_over = False

def create_pipe():
    gap_y = random.randint(100, HEIGHT - PIPE_GAP - 100)
    top_pipe = pygame.Rect(WIDTH, 0, PIPE_WIDTH, gap_y)
    bottom_pipe = pygame.Rect(WIDTH, gap_y + PIPE_GAP, PIPE_WIDTH, HEIGHT - gap_y - PIPE_GAP)
    return top_pipe, bottom_pipe

def draw_bird():
    screen.blit(bird_image, bird_rect)

def draw_pipes():
    for pipe in pipes:
        if pipe.top == 0:
            pipe_height = pipe.height
            top_pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, pipe_height))
            top_pipe_image = pygame.transform.rotate(top_pipe_image, 180)
            screen.blit(top_pipe_image, (pipe.x, pipe.y))
        else:
            pipe_height = pipe.height
            bottom_pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, pipe_height))
            screen.blit(bottom_pipe_image, (pipe.x, pipe.y))

def check_collision():
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
        return True
    return False

def show_death_screen():
    global score
    death_text = font.render("You Died", True, (0, 0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))

    screen.blit(background_image, (0, 0))

    death_text_rect = death_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(death_text, death_text_rect)
    screen.blit(score_text, score_text_rect)

    pygame.display.flip()

running = True
while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_started and not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            game_started = True
            bird_y_velocity = 0
            pipes.clear()
            pipes.extend(create_pipe())
            score = 0

        elif game_started and event.type == pygame.MOUSEBUTTONDOWN:
            bird_y_velocity = JUMP_STRENGTH

        elif game_over and event.type == pygame.MOUSEBUTTONDOWN:
            pass

    if not game_started and not game_over:
        bird_rect.y = HEIGHT // 2
        draw_bird()

        if not pipes:
            pipes.extend(create_pipe())
        draw_pipes()

        title_text = font.render("Welcome to Flappy Bird!", True, (0, 0, 0))
        instructions_text = font.render("Click to Start", True, (0, 0, 0))

        title_text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        instructions_text_rect = instructions_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        screen.blit(title_text, title_text_rect)
        screen.blit(instructions_text, instructions_text_rect)

    elif game_started:
        bird_y_velocity += GRAVITY
        bird_rect.y += int(bird_y_velocity)

        for pipe in pipes:
            pipe.x -= pipe_speed

        pipes = [pipe for pipe in pipes if pipe.right > 0]

        if pipes and pipes[0].right < bird_rect.left:
            score += 1
            pipes = pipes[2:]
            pipes.extend(create_pipe())

        draw_bird()
        draw_pipes()

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        if check_collision():
            game_over = True
            pipes.clear()

    if game_over:
        show_death_screen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
