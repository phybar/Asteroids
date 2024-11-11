from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Pass x, y, radius separately
        self.velocity = pygame.Vector2(0, 0)
        
        
        


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        #something here about self.position and self.velocity
        self.position += self.velocity * dt

        