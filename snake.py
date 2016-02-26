from config import *
from collections import deque

class Snake(object):
    def __init__(self,start,start_length):
        self.speed = SNAKE_SPEED_INITIAL
        self.timer = 1.0/self.speed #time remaining to next movement
        self.growth_pending = 0 #number of segments still to grow
        self.direction = DIRECTION_UP #current movement direction
        self.segments = deque([start - self.direction*i for i in xrange(start_length)])

    def __iter__(self):
        return iter(self.segments)

    def __len__(self):
        return len(self.segments)

    def change_direction(self,direction):
        ''' Update direction of the snake
        '''
        if direction != -direction: #not allowed to move opposite of current direction
            self.direction = direction
        return

    def head(self):
        ''' Get position of snake's head
        '''
        return self.segments[0]

    def update(self,dt,direction):
        ''' Update snake by dt seconds and
            possibly set direction
        '''
        self.timer -= dt
        if self.timer > 0:
            #nothing to do yet
            return
        if self.direction != -direction: #not allowed to move opposite of current direction
            self.direction = direction
        self.timer += 1/self.speed
        self.segments.appendleft(self.head() + self.direction) #add new head
        if self.growth_pending > 0:
            self.growth_pending -= 1
        else:
            self.segments.pop() #remove tail
        return

    def grow(self):
        ''' Grow snake by one segment and
            speed up
        '''
        self.growth_pending += 1
        self.speed += SNAKE_SPEED_INCREMENT
        return

    def self_intersection(self):
        ''' Is the snake currently self-
            intersecting?
        '''
        it = iter(self)
        head = next(it)
        return head in it
