from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", tuple(self.position), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        port = Asteroid(self.position.x, self.position.y, new_radius)
        port.velocity = self.velocity.rotate(-1 * angle) * 1.2
        starboard = Asteroid(self.position.x, self.position.y, new_radius)
        starboard.velocity = self.velocity.rotate(angle) * 1.2
