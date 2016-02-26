from position import Position
from pygame.locals import *

## FPS ##
FPS = 60

## Score Stuff ##
SEGMENT_SCORE = 50 #score per segment of snake

## Snake Stuff ##
SNAKE_SPEED_INITIAL = 4.0 #initial speed of the snake in squares per second
SNAKE_SPEED_INCREMENT = 0.25 #amount the snake speeds up upon growing
SNAKE_START_LENGTH = 1 #initial snake length in number of segments

## World Stuff ##
WORLD_HEIGHT = 20 #number of blocks in world's height
WORLD_WIDTH = 20 #number of blocks in world's width
WORLD_SIZE = Position((WORLD_WIDTH,WORLD_HEIGHT)) #world size in number of blocks
BLOCK_SIZE = 24 #block size in pixels

## Font Stuff ##
FONT_TYPE = 'Comic sans'
FONT_SIZE = 20

## Colors ##
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
TEAL = 0,255,255
YELLOW = 255,255,0
PURPLE = 255,0,255
BACKGROUND_COLOR = 45,45,45 #slate gray
SNAKE_COLOR = BLACK
DEATH_COLOR = RED
FOOD_COLOR = GREEN
TEXT_COLOR = BLACK

## Directions ##
DIRECTION_UP = Position((0,-1))
DIRECTION_DOWN = Position((0,1))
DIRECTION_LEFT = Position((-1,0))
DIRECTION_RIGHT = Position((1,0))
DIRECTION_DR = DIRECTION_DOWN + DIRECTION_RIGHT #diagonal?

## Direction Mapping from Key Event ##
KEY_DIRECTION = {
    K_w: DIRECTION_UP,      # w
    K_UP: DIRECTION_UP,     # up-arrow
    K_s: DIRECTION_DOWN,    # s
    K_DOWN: DIRECTION_DOWN, # down-arrow
    K_a: DIRECTION_LEFT,    # a
    K_LEFT: DIRECTION_LEFT, # left-arrow
    K_d: DIRECTION_RIGHT,   # d
    K_RIGHT: DIRECTION_RIGHT# right-arrow
}

## Food Stuff ##
FOOD_PROBABILITY = 4 #1/FOOD_PROBABILITY is the chance that multiple foods will be placed at each step
