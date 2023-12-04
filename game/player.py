import pygame
import config
from laser import Laser

class Player (pygame.sprite.Sprite): # Inherited from pygame
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.image.load('image/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = 5
        self.max_x_constraint = config.screen_width
        self.laser_cd = 600
        self.laser_ready = True
        self.laser_counter = 0

        self.lasers = pygame.sprite.Group()
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.laser_ready:
            self.shoot_laser()
            self.laser_ready = False
            self.laser_counter = pygame.time.get_ticks()
    
    def recharge(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_counter >= self.laser_cd:
                self.laser_ready = True


    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
    
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
