import random
from config import *


def generate_pipe_pair():
    HEIGHT_GAP = 300
    TOP_HIGH = random.randint(50, SCREEN_HEIGHT - HEIGHT_GAP - 50)
    BOTTOM_HIGH = SCREEN_HEIGHT - HEIGHT_GAP - TOP_HIGH

    TOP_PIPE = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, TOP_HIGH)
    BOTTOM_PIPE = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - BOTTOM_HIGH, PIPE_WIDTH, BOTTOM_HIGH)

    return TOP_PIPE, BOTTOM_PIPE
