import pgzrun
import itertools #meant for itration or repetition
import random

WIDTH= 400
HEIGHT= 400
TITLE= "Ship verses Bee"
BLOCK_POSITIONS= [(50,50), (350,50), (350,350), (50,350)]

bp= itertools.cycle(BLOCK_POSITIONS)
ship= Actor("shiip.png", center= (WIDTH/ 2, HEIGHT/ 2))
bee= Actor("bee.png", center= (50,50))

def move_bee():
    animate(bee, "bounce_end", duration= 1,pos= next(bp))

def draw():
    screen.clear()
    ship.draw()
    bee.draw()

move_bee()
clock.schedule_interval(move_bee, 2)

def next_ship_target():
    x= random.randint(100, 300)
    y= random.randint(100, 300)
    ship.target= x,y
    target_angle= ship.angle_to(ship.target)
    animate(ship, angle= target_angle, duration= 0.3, on_finished= move_ship())

def move_ship():
    a= animate(ship, tween= "accel_decel", duration= ship.distance_to(ship.target)/ 200,pos= ship.target, on_finished= next_ship_target)

next_ship_target()


pgzrun.go()