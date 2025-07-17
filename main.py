#this allows us to use code from
#the open-source pygame library
#throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
#import circleshape

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (drawable_group, updateable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updateable_group, drawable_group, asteroids_group)
    AsteroidField.containers = (updateable_group,)
    asteroidfield = AsteroidField()
    
    Shot.containers = (shots_group, drawable_group, updateable_group)
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        updateable_group.update(dt)

        for thing in asteroids_group:
            if thing.check_collision(player):
                print("Game over!")
                return 0
            for bullet in shots_group:
                if bullet.check_collision(thing):
                    bullet.kill()
                    thing.split()
            
        for thing in drawable_group:
            thing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
