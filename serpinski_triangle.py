import pygame
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,800))
gameDisplay.fill(black)
point_A=(400,100)
point_B=(100,600)
point_C=(700,600)
point=(random.randint(0,800),random.randint(0,800))
def midpoint(pointname):
    x1,y1=pointname
    x2,y2=point
    x3=(x1+x2)/2
    y3=(y1+y2)/2
    new_points=(int(x3),int(y3))
    return new_points
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.circle(gameDisplay, white, point_A, 1)
    pygame.draw.circle(gameDisplay, white, point_B, 1)
    pygame.draw.circle(gameDisplay, white, point_C, 1)
    pygame.draw.circle(gameDisplay,white,point,1)
    iteration=0
    while True:
        print(iteration)
        dice=random.randint(1,6)
        if dice==1 or dice==2:
            new_points=midpoint(point_A)
            pygame.draw.circle(gameDisplay,red,new_points,1)
            point=new_points
        if dice==3 or dice==4:
            new_points=midpoint(point_B)
            pygame.draw.circle(gameDisplay,green,new_points,1)
            point=new_points
        if dice==5 or dice==6:
            new_points=midpoint(point_C)
            pygame.draw.circle(gameDisplay,blue,new_points,1)
            point=new_points
        # pygame.time.wait(10)
        iteration+=1
        pygame.display.update()
    
