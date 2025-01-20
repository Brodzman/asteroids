import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for objects in updatable:
            objects.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!") 
                sys.exit()
        
        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()





