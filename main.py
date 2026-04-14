import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from logger import log_state
from logger import log_event
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updatable.update(dt=dt)

        for asteroid in asteroids:
            if asteroid.colldides_with(player):
                log_event("player_hit")
                sys.exit()

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
