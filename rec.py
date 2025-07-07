import pygame
import time 
import random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("recycle game number 2")
WIDTH=900
HEIGHT=700

s=pygame.display.set_mode([WIDTH,HEIGHT])

def change_background(img):
    background= pygame.image.load(img)
    bg=pygame.transform.scale(background, (WIDTH, HEIGHT))
    s.blit(bg,(0,0))
    

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

class Plastic(pygame.sprite.Sprite):
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

    time_elapsed = time.time()-start_time
    if time_elapsed > 60:
        if score > 40:
            text=myfont.render("you won")
        else:
            text=myfont.render("better luck next time")
    else:
        change_background("background.png")
        text=timing.render("time_elapsed:"+str(60-int(time_elapsed)),True,WHITE)
        s.blit(text,(10,10))
    
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y>0:
                bin.rect.y-=5
        if keys[pygame.K_DOWN]:
            if bin.rect.y<690:
                bin.rect.y+=6
        if keys[pygame.K_LEFT]:
            if bin.rect.x>0:
                bin.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x<890:
                bin.rect.x+=5
        
        item_hit_list=pygame.sprite.spritecollide(bin, item_list,True)
        plastic_hit_list=pygame.sprite.spritecollide(bin,plastic_list,True)

        for i in item_hit_list:
            score+=1
            text=myfont.render("score:"+str(score),True,WHITE)
        
        for i in plastic_list:
            score-=5
            text=myfont.render("score:"+str(score),True,WHITE)
        s.blit(text,(10,690))

        allsprites.draw(s)
        
    pygame.display.update()
pygame.quit()
