from circleshape import *
from constants import *
from shot import * 

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius = PLAYER_RADIUS)
        self.rotation = 0 
        self.shoot_wait = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_wait += dt

        if keys[pygame.K_LEFT]:
            self.rotate(-1*dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-1*dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_wait >= PLAYER_SHOOT_COOLDOWN:
                self.shoot()
                self.shoot_wait = 0 




    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shotted = Shot(self.position[0], self.position[1])
        shotted.velocity = PLAYER_SHOOT_SPEED * pygame.Vector2(0,1).rotate(self.rotation)
        

