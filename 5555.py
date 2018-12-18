from settings import Hero
import sys
import pygame
def run_game():
    pygame.init()
    screen=pygame.display.set_mode((800,800))
    pygame.display.set_caption('game')
    hero = Hero(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type== pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hero.orientation=1
                    hero.walk=True
                elif event.key == pygame.K_LEFT:
                    hero.orientation=2
                    hero.walk=True
                elif event.key == pygame.K_UP:
                    hero.orientation=3
                    hero.walk=True
                elif event.key == pygame.K_DOWN:
                    hero.orientation=4
                    hero.walk=True
            elif event.type== pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        print('666')
                        hero.walk = False

        screen.fill((250,250,250))



        hero.blitme()
        pygame.display.flip()
run_game()