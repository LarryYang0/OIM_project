import pygame, sys
from random import choice, randint
 
class Game:
	def __init__(self):
		pass
	
	def run(self):
	    pass



if __name__ == '__main__':
	pygame.init()
	screen_width = 900
	screen_height = 600
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