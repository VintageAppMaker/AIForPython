
Person: 
- pygame에서 
1. 커서 좌우를 이용하여 4X4 사이즈의 박스가 하단에서 움직인다. 
2. 스페이스를 누르면 총알이 위로 날라간다. 
간단한 예제를 만들어주세요

ChatGPT: 
- 다음은 간단한 예제입니다. 이 예제는 pygame을 사용하여 커서 좌우로 움직일 수 있는 4x4 크기의 박스를 하단에서 움직이도록 구현하며, 스페이스바를 누르면 총알이 위로 날아가는 기능을 포함합니다.

```python

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
```



이 예제는 주어진 조건에 맞게 박스와 총알을 움직이는 간단한 게임을 구현한 것입니다. 주석을 참고하여 코드를 이해하고 실행해보세요.
