import pygame, sys
from random import choice, randint
from player import Player
import config

class Game:
	def __init__(self):
		player_sprite = Player((screen_width/2,screen_height))
		self.player = pygame.sprite.GroupSingle(player_sprite)
	
	def run(self):
		self.player.update()

		self.player.draw(screen)
		self.player.sprite.lasers.draw(screen)
		




if __name__ == '__main__':
	pygame.init()
	screen_width = config.screen_width
	screen_height = config.screen_height
	screen = pygame.display.set_mode((screen_width,screen_height))
	clock = pygame.time.Clock()
	game = Game()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill((30,30,30))
		game.run()
		#crt.draw()
			
		pygame.display.flip()
		clock.tick(60)