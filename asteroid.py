from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            surface= surface,
            color= "white",
            radius= radius,
            center= (radius,radius),
            width= LINE_WIDTH
        )
        self.image = surface
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=self.position)

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = self.position
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        asteroid1 = self.velocity.rotate(angle)
        asteroid2 = self.velocity.rotate(-angle)
        new_radius = self.radius / 2

        ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast1.velocity = asteroid1 * 1.2
        ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        ast2.velocity = asteroid2 * 1.2

