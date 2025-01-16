import pygame
import random
import math
import time

height,width = 1280,720

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
grey = (128,128,128)
pygame.init()
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("ANTS")

screen.fill(black)
clock = pygame.time.Clock()

running = True
ants =[]
vants = []
for i in range(50):
	ants.append((random.randint(0,height),random.randint(0,width)))
	pygame.draw.circle(screen,white,ants[i],10)
	pygame.display.flip()
vants.append(ants[0])
ants.pop(0)
pygame.draw.circle(screen,red,vants[-1],10)

for j in range(50):
	dict = {'0':'0'}
	ds = float('inf')
	if(len(ants)==0):
		break
	for i in range(0,50-len(vants)):
		x2,y2 = ants[i]
		x1,y1 = vants[-1]
		d1 = (x2-x1)**2
		d2 = (y2-y1)**2
		d = math.sqrt(d1+d2)
		dict[d]=i
		ds = min(ds,d)

	vants.append(ants[dict[ds]])
	ants.pop(dict[ds])
	pygame.draw.line(screen,white,vants[-2],vants[-1],2)
	pygame.display.flip()
	# time.sleep(0.5)
	pygame.draw.circle(screen,red,vants[-1],10)
	pygame.display.flip()
	# time.sleep(1.5)

	print("B: ",vants)
	print("A: ",ants)
pygame.draw.line(screen,white,vants[-1],vants[0],2)
pygame.display.flip()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

clock.tick(6)
pygame.quit()
