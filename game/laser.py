from typing import Any
import pygame
import config

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed) -> None:
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
    
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= config.screen_height:
            self.kill()

    def update(self):
        self.rect.y += self.speed
    
        
