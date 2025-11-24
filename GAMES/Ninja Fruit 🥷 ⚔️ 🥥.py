import pygame
import random
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# Colors
WHITE = (255, 255, 255)
RED = (200, 50, 50)
BLACK = (0, 0, 0)
YELLOW = (240, 230, 40)

# Game data
fruits = []
score = 0
game_over = False

def spawn_fruit():
    """Create fruit objects."""
    x = random.randint(100, WIDTH - 100)
    y = HEIGHT + 50
    speed_x = random.uniform(-3, 3)
    speed_y = random.uniform(-10, -15)
    fruit_type = random.choice(["fruit", "fruit", "fruit", "bomb"])  # bombs are rarer
    fruits.append({
        "x": x,
        "y": y,
        "vx": speed_x,
        "vy": speed_y,
        "type": fruit_type
    })

def draw_fruit(f):
    if f["type"] == "fruit":
        pygame.draw.circle(screen, RED, (int(f["x"]), int(f["y"])), 25)
    else:
        pygame.draw.circle(screen, BLACK, (int(f["x"]), int(f["y"])), 25)
        pygame.draw.circle(screen, YELLOW, (int(f["x"]), int(f["y"])), 10)

def update_fruit(f):
    f["x"] += f["vx"]
    f["y"] += f["vy"]
    f["vy"] += 0.4  # gravity

def slice_check(f, mouse_path):
    """Check if mouse swiped across the fruit."""
    if len(mouse_path) < 2:
        return False

    for i in range(len(mouse_path) - 1):
        x1, y1 = mouse_path[i]
        x2, y2 = mouse_path[i+1]
        dist = abs((x2-x1)*(f["y"]-y1) - (y2-y1)*(f["x"]-x1)) / (
            math.hypot(x2-x1, y2-y1) + 0.001
        )
        if dist < 30:  # slice width
            return True
    return False

mouse_path = []

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 700)

while True:
    screen.fill((30, 30, 30))
    mouse_path = mouse_path[-15:] + [pygame.mouse.get_pos()]  # trailing swipe path
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and event.type == pygame.MOUSEBUTTONDOWN:
            # restart game
            fruits = []
            score = 0
            game_over = False

        if event.type == SPAWN_EVENT and not game_over:
            spawn_fruit()

    if not game_over:
        # Update & draw fruits
        for f in fruits[:]:
            update_fruit(f)
            draw_fruit(f)

            if slice_check(f, mouse_path):
                if f["type"] == "bomb":
                    game_over = True
                else:
                    score += 1
                fruits.remove(f)

            if f["y"] > HEIGHT + 100:
                fruits.remove(f)

        # Draw swipe trail
        if len(mouse_path) > 1:
            pygame.draw.lines(screen, WHITE, False, mouse_path, 2)

        # Score
        s_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(s_text, (10, 10))

    else:
        over_text = font.render("GAME OVER - Click to restart", True, WHITE)
        screen.blit(over_text, (200, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
