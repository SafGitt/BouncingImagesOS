import pygame
import json
import sys
import tkinter

config = open('Config.json')

data = json.load(config)
for i in data['iconProperties']:
    speedX = i['speedX']
    speedY = i['speedY']

for dxz in data['iconFile']:
    imgFile = dxz['fullImgName']
pygame.init()


speed = [speedX, speedY]
black = 0, 0, 0
root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
size = width, height

ball = pygame.image.load(imgFile)
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()