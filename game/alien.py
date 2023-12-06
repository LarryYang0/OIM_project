from typing import Any
import pygame
import config

class Alien(pygame.sprite.Sprite):
    def __init__(self, alien_type, x, y) -> None:
        super().__init__()
        file_path = 'image/' + alien_type +'.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))
    
    def update(self, speed) -> None:
        self.rect.x += speed

class Bonus(pygame.sprite.Sprite):
    def __init__(self, side) -> None:
        super().__init__()
        file_path = 'image/extra.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        
        if side == 'right':
            x = config.screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3
        
        self.rect = self.image.get_rect(topleft = (x, 80))
    
    def update(self) -> None:
        self.rect.x += self.speed