from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            first_vect = self.velocity.rotate(random_angle)
            second_vect = self.velocity.rotate(-random_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            split_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            split_asteroid1.velocity = first_vect * 1.2
            split_asteroid2.velocity = second_vect * 1.2

