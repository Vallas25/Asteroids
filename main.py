import pygame
from constants import *
from player import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    
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

        player.update(dt=dt)

        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick() / 1000)

if __name__ == "__main__":
    main()
