from vpython import *
import random

type_to_color = {"NET":color.blue,"CPU":color.red,"RAM":color.green}
PATHCONST = 4
POSCONST = 3
SPEEDCONST = 0.01
STARSIZE = 0.15

class star:
    """
    3 star types:
    - blue = network
    - red = CPU
    - green = RAM
    """
    def __init__(self,type):
        assert type_to_color[type]
        self.color = type_to_color[type]
        self.obj = sphere(pos=vector(random.random()*POSCONST, random.random()*POSCONST, random.random()*POSCONST),
                            radius=STARSIZE,
                            color=self.color,
                            make_trail=False,
                            interval=10, #interval to update trail
                            retain=2) #trail retain time
        self.theta = 0
        self.t_axis = vector(random.random()*POSCONST, random.random()*POSCONST, random.random()*POSCONST) #3d dot in space, to create plane, init pos + 0,0,0 + current
        self.radius = self.obj.pos.mag
        self.obj.visible = False

    def display(self):
        self.obj.visible = True

    def hide(self):
        self.obj.visible = False

    def updatePos(self):
        radius =  self.radius#path radius
        current_position = self.obj.pos #current pos vector
        dist_delta = radius * SPEEDCONST #speed
        #perpendicular vector should satisfy = pos * new_vector = 0
        path_dir = current_position.cross(self.t_axis).norm()
        new_position = (current_position + path_dir * dist_delta).norm() * radius
        return new_position

