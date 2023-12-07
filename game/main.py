import pygame, sys
from random import choice, randint
from player import Player
from alien import Alien, Bonus
from laser import Laser
import obstacle
import config
import random


class Game:
    def __init__(self):
        # Player setup
        player_sprite = Player((screen_width / 2, screen_height - 10))
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # HUD
        self.lives = 3
        self.live_surface = pygame.image.load("image/player.png").convert_alpha()
        self.live_x_start_position = (
            self.live_surface.get_size()[0] * 2 + 20
        )  # geting the size(x,y), [0] only give the x which is width

        # Score
        self.score = 0
        self.font = pygame.font.Font("font/Pixeled.ttf", 20)

        # Obstacle setup
        self.shape = obstacle.shape
        self.blocks = pygame.sprite.Group()
        self.block_size = 6
        self.obstacle_amount = 4
        self.obstacle_position = [
            num * (config.screen_width / self.obstacle_amount)
            for num in range(self.obstacle_amount)
        ]
        self.create_multiple_obstacles(
            *self.obstacle_position, x_start=screen_width / 15, y_start=480
        )

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.aliens_speed = config.alien_default_speed
        self.aliens_setup(6, 8, 60, 40, 70, 100)
        self.aliens_lasers = pygame.sprite.Group()

        # Reward setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = random.randint(40, 80)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (0, 204, 204), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(
        self,
        *offset,
        x_start,
        y_start,
    ):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def aliens_setup(self, rows, cols, x_distance, y_distance, x_offset, y_offset):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien = Alien("yellow", x, y)
                elif row_index > 0 and row_index <= 2:
                    alien = Alien("green", x, y)
                else:
                    alien = Alien("red", x, y)
                self.aliens.add(alien)

    def alien_pos_checker(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= config.screen_width:
                self.aliens_speed = -config.alien_default_speed
                self.alien_movedown(config.alien_default_down)
            if alien.rect.left <= 0:
                self.aliens_speed = config.alien_default_speed
                self.alien_movedown(config.alien_default_down)

    def alien_movedown(self, y_distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += y_distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, config.alien_laser_speed)
            self.aliens_lasers.add(laser_sprite)

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Bonus(random.choice(["right", "left"])))
            self.extra_spawn_time = random.randint(400, 800)

    def collision_check(self):
        # player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacles collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()  # Alter for more weapon types

                # aliens collision
                hitconfirm = pygame.sprite.spritecollide(laser, self.aliens, True)
                if hitconfirm:
                    for alien in hitconfirm:
                        self.score += alien.score
                    laser.kill()

                # reward collision
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    laser.kill()

        # alien laser
        if self.aliens_lasers.sprites():
            for laser in self.aliens_lasers.sprites():
                # obstacles collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # player collision
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()

        # alien hitbox
        if self.aliens:
            for alien in self.aliens.sprites():
                pygame.sprite.spritecollide(alien, self.blocks, True)
                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for live in range(self.lives):
            x = 20 + (live * (self.live_surface.get_size()[0] + 10))
            screen.blit(self.live_surface, (x, 8))

    def display_score(self):
        score_surface = self.font.render(f"SCORE:{self.score}", False, "white")
        score_rect = score_surface.get_rect(
            topright=((config.screen_width + score_surface.get_size()[0]) / 2, 0)
        )
        screen.blit(score_surface, score_rect)

    def victory_message(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render('You won',False,'white')
            victory_rect = victory_surf.get_rect(center = (screen_width / 2, screen_height / 2))
            screen.blit(victory_surf,victory_rect)

    def run(self):
        # updates
        self.player.update()
        self.aliens.update(self.aliens_speed)
        self.alien_pos_checker()
        self.aliens_lasers.update()
        self.extra_alien_timer()
        self.extra.update()

        # player
        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.display_lives()
        self.display_score()

        # obstacle
        self.blocks.draw(screen)
        self.collision_check()

        # aliens
        self.aliens.draw(screen)
        self.aliens_lasers.draw(screen)
        self.extra.draw(screen)

        # win condition
        self.victory_message()

    

class CRT:
    def __init__(self) -> None:
        self.tv = pygame.image.load('image/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (screen_width, screen_height))

    def draw(self):
        self.tv.set_alpha(randint(60, 90))  # Randomize the transparency for a flickering effect
        screen.blit(self.tv, (0, 0))
    
if __name__ == "__main__":
    pygame.init()
    screen_width = config.screen_width
    screen_height = config.screen_height
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()
    crt = CRT()

    ALIENS_LASER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(
        ALIENS_LASER_EVENT, 800
    )  # cool down need to be changed for different level/enemy

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENS_LASER_EVENT:
                game.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()
        crt.draw()

        pygame.display.flip()
        clock.tick(60)
