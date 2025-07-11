import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = [updatable, drawable]
    Asteroid.containers = [updatable, drawable, asteroids]
    AsteroidField.containers = [updatable]

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()

        # limit the framerate to 144 FPS
        dt = clock.tick(144) / 1000
        updatable.update(dt)


if __name__ == "__main__":
    main()