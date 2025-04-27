import pygame

from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, 
ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS)

from player import Player

def game_loop(screen, updatable, drawable):
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get(): #makes window close button work
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000 #pauses game loop to 1/60 second
        screen.fill(color="black")
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip() # refreshes screen
        
        
        print(f"Delta time: {dt} seconds")


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player( SCREEN_WIDTH/2,  SCREEN_HEIGHT /2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen, updatable, drawable)

if __name__ == "__main__":
    main()