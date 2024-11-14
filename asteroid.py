from circleshape import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Pass x, y, radius separately
        self.velocity = pygame.Vector2(0, 0)
        
    def split(self):
        self.kill()

        # Checks the size of the asteroid and destroys it if too small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Creates a new random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Creates two new angles for the asteroids in two different directions
        new_angle_one = self.velocity.rotate(random_angle)
        new_angle_two = self.velocity.rotate(-random_angle)

        # Creates two smaller asteroids

        new_size = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_size)
        asteroid_1.velocity = new_angle_one * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_size)
        asteroid_2.velocity = new_angle_two * 1.2

        





           
        


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        #something here about self.position and self.velocity
        self.position += self.velocity * dt

