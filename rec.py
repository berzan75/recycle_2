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