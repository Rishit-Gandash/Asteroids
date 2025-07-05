import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from AsteroidField import *
from shot import * 
from homing_asteroids import *
import random



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    q = 1

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    homing_velocity = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Homing_Asteroid.containers = (asteroids, drawable, homing_velocity)
    # AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable) 
    # asteroidfield = AsteroidField()

    asteroid_array = []
    for i in range(5):
        asteroid_array.append(Homing_Asteroid(random.choice([random.randint(-100,-10), random.randint(1300,1400)]), random.choice([random.randint(-100,-10), random.randint(800,900)]) , ASTEROID_MIN_RADIUS))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)
        for i in asteroid_array:
            i.set_velocity(dt, player)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over! :C")
                q = 0
                break
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.kill()
            
            # checked_asteroids = set()
            # for asteroid_2 in asteroids:
            #     if asteroid == asteroid_2: 
            #         break 

            #     if asteroid.check_collision(asteroid_2):  # "and asteroid not in checked_asteroids and asteroid_2 not in checked_asteroids:
            #         asteroid.asteroid_collision(asteroid_2)
                    # checked_asteroids.add(asteroid)
                    # checked_asteroids.add(asteroid_2)

        if q == 0:
            break
        screen.fill((00,00,00))

        for i in drawable: 
            i.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()