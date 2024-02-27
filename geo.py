from config import *

pygame.init()

# Initialize a clock to measure time
clock = pygame.time.Clock()

# Initialize a variable to track times
time_elapsed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(CHARACTER_IMAGE_NORMAL, player_pos)
    screen.blit(BASE_FIELD, (0, 365))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y >= 3:
        player_pos.y -= 400 * dt
    if keys[pygame.K_s] and player_pos.y <= 330:
        player_pos.y += 400 * dt
    if keys[pygame.K_a] and player_pos.x >= 2:
        player_pos.x -= 400 * dt
    if keys[pygame.K_d] and player_pos.x <= 270:
        player_pos.x += 400 * dt

    # Print (x, y) every 1 second
    time_elapsed += dt
    if time_elapsed >= 1:  # 1 second has passed
        print(f"Character position: ({int(player_pos.x)}, {int(player_pos.y)})")
        time_elapsed = 0  # Reset the timer

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
