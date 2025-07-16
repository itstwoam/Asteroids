from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init_-(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (x,y), radius)

    def update(self, dt):
        self.position = self.velocity * dt
