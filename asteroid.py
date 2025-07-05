from circleshape import CircleShape
import pygame
from constants import *
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        velocity_1 = 1.2 * self.velocity.rotate(random_angle)
        velocity_2 = 1.2 * self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x + new_radius * math.sin(random_angle) , self.position.y + new_radius * math.cos(random_angle), new_radius)
        asteroid_2 = Asteroid(self.position.x - new_radius * math.sin(random_angle) , self.position.y - new_radius * math.cos(random_angle), new_radius)

        asteroid_1.velocity = velocity_1
        asteroid_2.velocity = velocity_2

    def asteroid_collision(self, asteroid_2):
        self.velocity, asteroid_2.velocity = asteroid_2.velocity, self.velocity

    