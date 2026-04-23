import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from constants import LINE_WIDTH
from asteroids import Asteroids
from asteroidfield import AsteroidField
from player import Player
from logger import log_state
from logger import log_event
import sys

def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION} ")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Sets the clock to pygame.time.Clock and sets variable dt for delta time

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  
    
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    asteroidfield = AsteroidField()

    
    player = Player(
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2
    )

    #player.containers = (updatable, drawable)

    # Infinite Game Loop

    while True:
        log_state()

        # Makes the X-Button of the game window close the application
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Makes the screen black

        updatable.update(dt)

        for objects in asteroids:
            if player.collides_with(objects) == True:            
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            



        screen.fill("black")

        for things in drawable:
            things.draw(screen)
        pygame.display.flip()     

        # Limits the FPS to 60 and sets the delta time to the latest delta and coverts output of
        # clock tick from milliseconds to seconds

        dt = clock.tick(60) /1000.0






if __name__ == "__main__":
    main()
    
 