import pygame
import random

# Initsialiseeri pygame
pygame.init()

# Mänguakna suurus
WIDTH, HEIGHT = 640, 480
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 120, 20
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
PADDLE_SPEED = 5
FONT_SIZE = 30

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)

# Loo mänguaken
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Mäng")

# Lae pildid
ball_img = pygame.image.load("img/ball.png")
paddle_img = pygame.image.load("img/pad.png")

# Muuda piltide suurust
ball_img = pygame.transform.scale(ball_img, (BALL_SIZE, BALL_SIZE))
paddle_img = pygame.transform.scale(paddle_img, (PADDLE_WIDTH, PADDLE_HEIGHT))

# Loo pall ja alus
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT // 1.5, PADDLE_WIDTH, PADDLE_HEIGHT)

# Palli liikumise kiirus ja suund
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = abs(BALL_SPEED_Y)  # Pall liigub alati alla alguses

# Aluse liikumise suund
paddle_direction = 1

# Skoor
score = 0
font = pygame.font.Font(None, FONT_SIZE)

# Mängu tsükkel
running = True
while running:
    pygame.time.delay(10)
    screen.fill(BLUE)  # Taustavärv

    # Kontrolli kasutaja sisendit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liiguta alust
    paddle.x += PADDLE_SPEED * paddle_direction
    if paddle.right >= WIDTH or paddle.left <= 0:
        paddle_direction *= -1  # Muuda suunda

    # Liiguta palli
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Palli põrkumine seintelt
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y = abs(ball_speed_y)  # Muudab suunda allapoole

    # Palli põrkumine alusega
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -abs(ball_speed_y)  # Muudab suunda üles
        ball_speed_x = random.choice([-BALL_SPEED_X, BALL_SPEED_X])  # Suvaline horisontaalne suund
        score += 1  # Suurenda skoori

    # Kui pall läheb ekraanilt välja (kaotuspunkt), suuname selle tagasi alusele
    if ball.bottom >= HEIGHT:
        score -= 1  # Vähenda skoori
        ball.x = paddle.x + PADDLE_WIDTH // 2 - BALL_SIZE // 2  # Pall läheb aluse keskele
        ball.y = paddle.y - BALL_SIZE  # Pall asetatakse aluse kohale
        ball_speed_x = random.choice([-BALL_SPEED_X, BALL_SPEED_X])  # Suvaline horisontaalne suund
        ball_speed_y = -abs(BALL_SPEED_Y)  # Liigub üles

    # Joonista mänguelemendid
    screen.blit(paddle_img, (paddle.x, paddle.y))
    screen.blit(ball_img, (ball.x, ball.y))

    # Kuva skoor ekraani ülaservas
    score_text = font.render(f"Skoor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Uuenda ekraani
    pygame.display.flip()

pygame.quit()
