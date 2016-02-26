# snake
My first attempt at making a snake game with pygame

## Files ##
#config.py
  Contains a bunch of variables to make the game run
  
  Although using global variables are frowned upon, I
  made this design choice so that I could organize
  all of the variables in one place I could easily
  access
  
#position.py
  An ADT representing an x,y position tuple
  
  Supports vector operations in addition to
  the regular operations of a tuple
  
  Examples:
  
    >> Position((5,6)) + Position((7,8))
    
    >> (12,14)
    
    >> Position((5,6)) - Position((7,8))
    
    >> (-2, -2)
    
    >> Position((5,6)) * 100
    
    >> (500, 600)
    
#snake.py
  ADT representing the snake that moves around the screen
  
#snakegame.py
  Contains the game logic, as well as the main loop for 
  actually playing the game
