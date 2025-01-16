import pygame
import random
import math
import time
from collections import deque

height, width = 720, 1280

black = (0,0,0)
pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Galaxy Simulation")

clock = pygame.time.Clock()

running = True
color_list = [(255, 210, 125), (255, 163, 113), (166, 168, 255), (255, 250, 134), (168, 123, 255),(255, 255, 255), (245, 245, 245), (255, 250, 250), (250, 255, 255), (255, 255, 240), (240, 255, 255)]

class Star:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def calculate_radius():
    max_radius = 3.0
    min_radius = 0.0
    radius = min_radius + random.random() * (max_radius - min_radius)
    return radius

def generate_star():
    x = random.randint(0, width)  
    y = random.randint(0, height)  
    color = random.choice(color_list)  
    radius = calculate_radius()
    return Star(x, y, color, radius)

max_stars = 400
star_queue = deque(maxlen=max_stars)

for _ in range(max_stars):
    star_queue.append(generate_star())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    star_queue.popleft() 
    star_queue.append(generate_star())  

    for star in star_queue:
        star.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
