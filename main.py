from pygame.sprite import Group
from typing import Any
from pygame.surface import Surface
from pygame import display
import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver }")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    updatable: Group[Any] = pygame.sprite.Group()
    drawable: Group[Any] = pygame.sprite.Group()
    asteroids: Group[Any] = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for object in drawable:
            object.draw(screen)

        display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
