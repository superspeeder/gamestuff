import pygame
from pygame.locals import *

Sprite = pygame.sprite.Sprite
Group = pygame.sprite.Group

def BaseSprite(Sprite):
  def __init__(self, **kwargs):
    self.fillAttribs(**kwargs)
  
  def fillAttribs(**kwargs):
    image_type = -1
    for key, val in kwargs.items():
      if BaseSprite.attribAllowed(key):
        cat = BaseSprite.getAttribCategory(key)
        if cat == BaseSprite.CATEGORY_MAIN_VISUAL:
          if not isinstance(image, pygame.Surface):
            print("[Error] image mode true but specified image is not a pygame surface")
          if key == "image" and image_type != 1:
            self.image = image
            
          
          if key == "color" and image_type != 0:
            if "size" in kwargs:
              surf = pygame.Surface(kwargs[size])
            else:
              print("[Error] No texture size specified and fill color mode is true")
    
def generateSprite(
