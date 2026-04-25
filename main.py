import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from logger import log_state
from logger import log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    pygame.display.set_caption(CAPTION)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)

    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32)

    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updatable.update(dt=dt)

        score = font.render(f"score: {player.score}", True, "white")
        scoreRect = score.get_rect()
        scoreRect.center = (round(SCREEN_WIDTH * 9/10),round(SCREEN_HEIGHT * 1/10))
        screen.blit(score, scoreRect)
        lives = font.render(f"lives: {player.lives}", True, "white")
        livesRect = lives.get_rect()
        livesRect.center = (round(SCREEN_WIDTH * 1/10),round(SCREEN_HEIGHT * 1/10))
        screen.blit(lives, livesRect)

        for asteroid in asteroids:
            if asteroid.colldides_with(player):
                if player.secondry_collision_check(asteroid):
                    log_event("player_hit")
                    player.got_hit()
                    for asteroid in asteroids:
                        asteroid.kill()
            
            for shot in shots:
                if asteroid.colldides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    player.score_increase()
                    shot.kill()

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
