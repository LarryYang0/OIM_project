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
        player_sprite = Player((screen_width / 2, screen_height))
        self.player = pygame.sprite.GroupSingle(player_sprite)

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
            self.extra_spawn_time = random.randint(40, 80)

    def run(self):
        self.player.update()
        self.aliens.update(self.aliens_speed)
        self.alien_pos_checker()
        self.aliens_lasers.update()
        self.extra_alien_timer()
        self.extra.update()

        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)

        self.blocks.draw(screen)

        self.aliens.draw(screen)
        self.aliens_lasers.draw(screen)
        self.extra.draw(screen)


if __name__ == "__main__":
    pygame.init()
    screen_width = config.screen_width
    screen_height = config.screen_height
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

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
        # crt.draw()

        pygame.display.flip()
        clock.tick(60)
