# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *  # Keep constants first
from circleshape import *  # Add this if you need it
from asteroid import *
from asteroidfield import *
from player import *  # Move player to the end




def main():
	pygame.init()
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots_group)

	dt = 0
	
	
	print ("Starting asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), shots_group)
	asteroid_field = AsteroidField()

	
	
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		
		for obj in updatable:
			obj.update(dt)
			

		for obj in asteroids:
			if obj.collision(player) == True:
				print ("Game over!")
				event.type == pygame.QUIT
				return


		screen.fill((0, 0, 0))

		for obj in drawable:
			obj.draw(screen)
		

		pygame.display.flip()

		# Limit FPS to 60
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
