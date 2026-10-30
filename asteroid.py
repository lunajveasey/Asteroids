import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            
            angle: float = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(angle)
            second_velocity = self.velocity.rotate(-angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            
            split_1 = Asteroid(self.position.x, self.position.y, split_radius)
            split_2 = Asteroid(self.position.x, self.position.y, split_radius)

            split_1.velocity = first_velocity * 1.2
            split_2.velocity = second_velocity * 1.2