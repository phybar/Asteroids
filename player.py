import pygame
from constants import *
from circleshape import *

print("Debug - Available constants in player.py:", PLAYER_SPEED, PLAYER_SHOOT_SPEED)


#New Shot Class - Copied from Asteroid to start with
class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  # Pass x, y
        self.velocity = pygame.Vector2(0, 1)
       
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        #something here about self.position and self.velocity
        self.position += self.velocity * dt


class Player(CircleShape):
   
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots_group
        self.timer = 0
        



        


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0,1)
        direction = direction.rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        new_shot.velocity = velocity
        self.shots.add(new_shot)

    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer == 0: 
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

