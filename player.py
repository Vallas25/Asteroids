import pygame
import sys
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0
        self.score = START_SCORE
        self.lives = LIVES
        self.org_ship = pygame.image.load("assets/asteroid_ship.png").convert_alpha()
        self.ship = pygame.transform.rotozoom(self.org_ship, self.rotation, 2)
        self.rect = self.ship.get_rect(center = self.position)
    
    # in the Player class
    
    def hit_box(self):
        pass

    def draw(self, screen):
       screen.blit(self.ship, self.rect)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.ship = pygame.transform.rotozoom(self.org_ship, self.rotation, 2)
        self.rect = self.ship.get_rect(center=self.position)
    
    def update(self, dt):
        self.cooldown_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt = dt)

        if keys[pygame.K_d]:
            self.rotate(dt = -dt)
        
        if keys[pygame.K_w]:
            self.move(dt = dt)
        
        if keys[pygame.K_s]:
            self.move(dt = -dt)
        
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer > 0:
                pass
            else:
                self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, -1)
        direction = unit_vector.rotate(-self.rotation)
        self.position += direction * PLAYER_SPEED * dt
        self.rect.center = self.position

    def shoot(self):
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = (pygame.Vector2(0,-1).rotate(-self.rotation) * PLAYER_SHOOT_SPEED)
    
    def score_increase(self):
        self.score += 1
        print(f"hit! {self.score}")

    def got_hit(self):
        self.lives -= 1
        self.score -= int(self.score * 0.1)
        if self.lives < 1:
            print("killed by asteroid")
            sys.exit()
    
    def secondry_collision_check(self, other):
        pass
