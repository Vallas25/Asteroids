from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            surface= screen,
            color= "white",
            center= self.position,
            radius= self.radius,
            width= LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        asteroid1 = self.velocity.rotate(angle)
        asteroid2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast1.velocity = asteroid1 * 1.2
        ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        ast2.velocity = asteroid2 * 1.2

