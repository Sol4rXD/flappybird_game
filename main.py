from config import *

pygame.init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                JUMPING = True
                JUMP_VELOCITY = -400

    screen.blit(BACKGROUND, (0, 0))

    # Check JUMPING
    if JUMPING:
        player_pos.y += JUMP_VELOCITY * dt
        JUMP_VELOCITY += GRAVITY * dt
        print("Flying")

        # Check if the character reaches the ground
        if player_pos.y >= 330:
            player_pos.y = 330
            JUMPING = False
            current_character_state = 'normal'
            print("At ground")

        elif player_pos.y <= 1:
            player_pos.y = 1
            print("At top")

        else:
            current_character_state = 'upper'

    # Not JUMPING
    else:
        current_character_state = 'normal'
        print("Not fly")

    screen.blit(character_images[current_character_state], player_pos)
    screen.blit(BASE_FIELD, (0, 365))

    time_elapsed += dt
    if time_elapsed >= 1:
        print(f"Character position: ({int(player_pos.x)}, {int(player_pos.y)})")
        time_elapsed = 0

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
