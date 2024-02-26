import pygame

# Resolution
screen = pygame.display.set_mode((300, 512))
clock = pygame.time.Clock()
running = True
dt = 0

# PLayer SPEED
PLAYER_SPEED = 300

player_pos = pygame.Vector2(25, 150)

# Load the background image
BACKGROUND = pygame.image.load("assets/sprites/background-day.png")  # Replace with your image file
BACKGROUND = pygame.transform.scale(BACKGROUND, (300, 512))

# PLayer
CHARACTER_IMAGE_NORMAL = pygame.image.load("assets/sprites/bluebird-midflap.png")
CHARACTER_IMAGE_NORMAL = pygame.transform.scale(CHARACTER_IMAGE_NORMAL, (30, 30))

# Base
BASE_FIELD = pygame.image.load("assets/sprites/base.png")
BASE_FIELD = pygame.transform.scale(BASE_FIELD, (300, 150))

# Load character images
character_images = {
    'normal': pygame.image.load("assets/sprites/bluebird-midflap.png"),
    'upper': pygame.image.load("assets/sprites/bluebird-upflap.png"),
    'down': pygame.image.load("assets/sprites/bluebird-downflap.png")
}

# Set the initial character state
current_character_state = 'normal'

# Initialize a clock to measure time
clock = pygame.time.Clock()

# Initialize a variable to track time
time_elapsed = 0

JUMPING = False
JUMP_VELOCITY = 0
GRAVITY = 1000
