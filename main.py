from logic import *

# Set the debugging flag
DEBUG = False

pygame.init()

for _ in range(2):
    pipes.append(generate_pipe_pair())

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
        if DEBUG:
            print("Flying")

        # Check if the character reaches the ground
        if player_pos.y >= 340:
            player_pos.y = 340
            JUMPING = False
            current_character_state = 'normal'
            if DEBUG:
                print("At ground")

        elif player_pos.y <= 1:
            player_pos.y = 2
            if DEBUG:
                print("At top")

        else:
            current_character_state = 'upper'

    # Not JUMPING
    else:
        current_character_state = 'normal'
        if DEBUG:
            print("Not fly")

    screen.blit(character_images[current_character_state], player_pos)

    # Update base field position
    base_field_x -= 50 * dt

    for i in range(len(base_field_images)):
        screen.blit(base_field_images[i], (base_field_x + i * base_field_width, 365))

    if base_field_x < -base_field_width:
        base_field_x = 0

    # PIPE
    for i, (TOP_PIPE, BOTTOM_PIPE) in enumerate(pipes):
        TOP_PIPE.x -= 50 * dt
        BOTTOM_PIPE.x -= 50 * dt

        if TOP_PIPE.right < 0:
            pipes[i] = generate_pipe_pair()

        screen.blit(pipe_image, TOP_PIPE.topleft)
        screen.blit(pygame.transform.flip(pipe_image, False, True), BOTTOM_PIPE.topleft)

    time_elapsed += dt
    if time_elapsed >= 1:
        if DEBUG:
            print(f"Character position: ({int(player_pos.x)}, {int(player_pos.y)})")
        time_elapsed = 0

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()