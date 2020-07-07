from vpython import *
from star import star
import psutil
import time

class Agent:
    def __init__(self,stars_per_label):
        self.stars_per_label = stars_per_label
        #create star instances
        self.CPUstars = [star("CPU") for i in range(stars_per_label)]
        self.RAMstars = [star("RAM") for i in range(stars_per_label)]
        self.NETstars = [star("NET") for i in range(stars_per_label)]
        #visual state track
        self.CPU_vis = 0
        self.RAM_vis = 0
        self.NET_vis = 0
        self.last_update = time.time() - 3

    def check_computer_state(self):
        cpu = self.CPU_vis * (100/self.stars_per_label)
        RAM = self.RAM_vis * (100/self.stars_per_label)
        net = self.NET_vis * (100/self.stars_per_label)
        if (time.time() - self.last_update) > 2:
            self.last_update  = time.time()
            cpu = psutil.cpu_percent()
            RAM = psutil.virtual_memory().percent
            net = 50
        return cpu,RAM,net

    def update_visibility(self, init = False):
        #get computer status
        cpu_p, RAM_p, net_p = self.check_computer_state()
        self.CPU_vis = round((cpu_p/100) * self.stars_per_label)
        self.RAM_vis = round((RAM_p/100) * self.stars_per_label)
        self.NET_vis = round((net_p/100) * self.stars_per_label)
        #update visibility
        if cpu_p != self.CPU_vis or init:
            for i in range(self.stars_per_label):
                if i < round(self.CPU_vis): self.CPUstars[i].display()
                if i >= round(self.CPU_vis): self.CPUstars[i].hide()
        if RAM_p != self.RAM_vis or init:
            for i in range(self.stars_per_label):
                if i < round(self.RAM_vis): self.RAMstars[i].display()
                if i >= round(self.RAM_vis): self.RAMstars[i].hide()
        if net_p != self.NET_vis or init:
            for i in range(self.stars_per_label):
                if i < round(self.NET_vis): self.NETstars[i].display()
                if i >= round(self.NET_vis): self.NETstars[i].hide()

    def update_positions(self):
        # cpu
        for i in range(self.CPU_vis):
            new_position = self.CPUstars[i].updatePos()
            self.CPUstars[i].obj.pos = new_position #update vpython obj
        # RAM
        for i in range(self.RAM_vis):
            new_position = self.RAMstars[i].updatePos()
            self.RAMstars[i].obj.pos = new_position  # update vpython obj
        # net
        for i in range(self.NET_vis):
            new_position = self.NETstars[i].updatePos()
            self.NETstars[i].obj.pos = new_position  # update vpython obj


def main():
    my_agent = Agent(50) #start agent with 10 stars per label
    scene.forward = vector(0, -4, -0.5)
    my_agent.update_visibility(init=True)

    while True:
        rate(200)
        my_agent.update_visibility()
        my_agent.update_positions()



if __name__ == "__main__":
    main()