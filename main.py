import pygame
from constants import * 
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)

        screen.fill((00,00,00))

        for i in drawable:
            i.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
