import pygame
import sys

# 게임 초기화
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 박스 초기화
box_width, box_height = 40, 40
box_x = WIDTH // 2 - box_width // 2
box_y = HEIGHT - box_height
box_speed = 5

# 총알 초기화
bullet_width, bullet_height = 10, 20
bullet_x = box_x + box_width // 2 - bullet_width // 2
bullet_y = box_y - bullet_height
bullet_speed = 10
bullet_state = "ready"  # "ready"는 총알이 화면 상단에 있음을 의미

# 게임 루프
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = box_x + box_width // 2 - bullet_width // 2
                    bullet_y = box_y - bullet_height
                    bullet_state = "fire"  # "fire"는 총알이 발사되고 있음을 의미

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and box_x > 0:
        box_x -= box_speed
    if keys[pygame.K_RIGHT] and box_x < WIDTH - box_width:
        box_x += box_speed

    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = "ready"

    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height))
    if bullet_state == "fire":
        pygame.draw.rect(screen, (255, 0, 0), (bullet_x, bullet_y, bullet_width, bullet_height))

    pygame.display.update()
    clock.tick(60)