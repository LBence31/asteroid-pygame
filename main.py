# pyright: reportUnknownVariableType=false, reportUnknownMemberType=false
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Asteroid.containers = (asteroid_group, drawable_group, updatable_group)
    Player.containers = (drawable_group, updatable_group)
    AsteroidField.containers = updatable_group
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill((0, 0, 0))

        updatable_group.update(dt)

        for asteroid in asteroid_group:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit(0)

        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
