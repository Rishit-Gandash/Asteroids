from circleshape import CircleShape
import pygame
from constants import *
import math

class Homing_Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.q = 0 
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, -100)
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, self.radius)

    def set_velocity(self, dt, player):
        self.q += 0.02
        self.position += (player.position - self.position) * dt * self.q
        
    def update(self, dt):
        self.position += self.velocity * dt


    def asteroid_collision(self, asteroid_2):
        self.velocity, asteroid_2.velocity = asteroid_2.velocity, self.velocity

    