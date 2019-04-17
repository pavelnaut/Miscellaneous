# Real life tree
 
import math
from turtle import *
from random import randint
 
# harcoded values are for aesthetic purposes only
def draw_branch(branch_length, angle, thick, complexity):
    if branch_length > complexity:
        # random shades of brown
        pencolor(randint(160, 164), randint(65, 85), randint(1, 5))
        width(thick)
        forward(branch_length)
        right(angle)
        draw_branch(math.floor(branch_length * (60 + randint(0, 20))/100), angle, thick * 0.75, complexity)
        left(2 * angle)
        draw_branch(math.floor(branch_length * (60 + randint(0, 20))/100), angle, thick * 0.75, complexity)
        right(angle)
        # this makes the end branches green and keeps the trunk brown
        if branch_length < 60:
            pencolor(0, randint(130, 230), 0)
        else:
            pencolor(randint(160, 164), randint(65, 85), randint(1, 5))
        backward(branch_length)
 
# complexity parameter is actually how many leaves there will be at the top        
def draw_tree(trunk_length, angle, thick, complexity):
    colormode(255)
    speed("fastest")    
    left(90)    
    up()
    backward(trunk_length)    
    down()
    draw_branch(trunk_length, angle, thick, complexity)
    exitonclick()
 
draw_tree(110, 22, 11, 5)
