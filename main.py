import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from score import *
from logger import log_state
from logger import log_event
import sys

def main():
    pygame.display.set_caption(CAPTION)

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)
    score = START_SCORE

    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"score: {score}", True, "white")
    textRect = text.get_rect()
    textRect.center = (round(SCREEN_WIDTH * 9/10),round(SCREEN_HEIGHT * 1/10))

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
        
        screen.blit(text, textRect)

        for asteroid in asteroids:
            if asteroid.colldides_with(player):
                log_event("player_hit")
                sys.exit()
            
            for shot in shots:
                if asteroid.colldides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    score += 1
                    shot.kill()

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
