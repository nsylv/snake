import pygame
from random import randrange
from config import *
from snake import Snake

class SnakeGame(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.block_size = BLOCK_SIZE
        self.window = pygame.display.set_mode(WORLD_SIZE*self.block_size)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(FONT_TYPE,FONT_SIZE)
        self.world = Rect((0,0),WORLD_SIZE)
        self.reset()

    def reset(self):
        ''' Start a new game
        '''
        self.playing = True
        self.next_direction = DIRECTION_UP
        self.score = 0
        self.snake = Snake(self.world.center, SNAKE_START_LENGTH)
        self.food = set()
        self.add_food()
        return

    def add_food(self):
        ''' Add food, and with a small
            probability add more than
            one
        '''
        while not (self.food and randrange(FOOD_PROBABILITY)):
            food = Position(map(randrange,self.world.bottomright))
            if food not in self.food and food not in self.snake:
                self.food.add(food)
        return

    def inp(self,e):
        ''' Process keyboard event e
        '''
        if e.key in KEY_DIRECTION:
            self.next_direction = KEY_DIRECTION[e.key]
        elif e.key == K_SPACE and not self.playing: # space to reset
            self.reset()
        return

    def update(self,dt):
        ''' Update the game by dt seconds
        '''
        self.snake.update(dt, self.next_direction)

        head = self.snake.head()
        if head in self.food: #if snake hits food with head
            self.food.remove(head) #consume the food
            self.add_food() #add more food
            self.snake.grow() #grow the snake
            self.score += len(self.snake) * SEGMENT_SCORE

        if self.snake.self_intersection() or not self.world.collidepoint(self.snake.head()): #colliding with self of boundaries is game over
            self.playing = False

        return

    def block(self,p):
        ''' Return the screen rectangle
            corresponding to the position
            p
        '''
        return Rect(p*self.block_size, DIRECTION_DR*self.block_size)

    def draw_text(self,text,p):
        ''' Draw text at position p
        '''
        self.screen.blit(self.font.render(text, 1, TEXT_COLOR),p)
        return

    def draw(self):
        ''' Draw the game
        '''
        self.screen.fill(BACKGROUND_COLOR)
        for p in self.snake:
            pygame.draw.rect(self.screen,SNAKE_COLOR, self.block(p))
        for f in self.food:
            pygame.draw.rect(self.screen, FOOD_COLOR,self.block(f))
        self.draw_text('Score: {}'.format(self.score),(20,20))
        return

    def draw_death(self):
        ''' Draw game after game over
        '''
        self.screen.fill(DEATH_COLOR)
        self.draw_text('Game over! Press space to start a new game',(20,150))
        self.draw_text('Your score is {}'.format(self.score),(140,140))
        return

    def process_events(self):
        ''' Process key events and
            return bool saying if
            we should quit
        '''
        for e in pygame.event.get():
            if e.type == QUIT:
                return True
            elif e.type == KEYUP:
                self.inp(e)
        return False

    def play(self):
        done = False
        while not done:
            dt = self.clock.tick(FPS)/1000.0 #convert to seconds
            done = self.process_events()
            if self.playing:
                self.update(dt)
                self.draw()
            else:
                self.draw_death()
            pygame.display.flip()
        pygame.quit() #exit pygame nicely so no hang-up in IDLE
        return

def main():
    SnakeGame().play()
    
if __name__ == '__main__':
    main()
