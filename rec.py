import pygame
import time 
import random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("recycle game number 2")
WIDTH=900
HEIGHT=700

s=pygame.display.set_mode[WIDTH,HEIGHT]

def change_background(img):
    background= pygame.image.load(img)
    bg=pygame.transform.scale(background, (WIDTH, HEIGHT))
    s.blit(bg,(0,0))
    

class Bin(pygame.Sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recyclable(pygame.Sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

class Plastic(pygame.Sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plastic.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

images=["r1.png","r2.png","r3.png"]

item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

#creating recyclable items
for i in range (50):
    item=Recyclable(random.choice(images))
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    item_list.add(item)
    allsprites.add(item)

for i in range (50):
    p=Plastic()
    p.rect.x = random.randrange(WIDTH)
    p.rect.y = random.randrange(HEIGHT)
    plastic_list.add(p)
    allsprites.add(p)

bin= Bin()
allsprites.add(bin)

WHITE= (255,255,255)

playing=True
score=0
clock=pygame.time.Clock()
start_time= time.time()

myfont=pygame.font.SysFont("Times New Roman",30)
timing=pygame.font.SysFont("Times New Roman",20)
text=myfont.render("Score ="+str(score),True,WHITE)

while playing:
    clock.tick(60)

    time_elapsed = time.time()-start_time()
    if time_elapsed > 60:
        if score > 40:
            text=myfont.render("you won")
        else:
            text=myfont.render("better luck next time")
