from settings import Hero
from settings2 import Hero2
import sys
import pygame
def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1000,1000))
    pygame.display.set_caption('game')
    hero = Hero(screen)
    hero2 = Hero2(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type== pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hero.orientation=1
                    hero.walk=True
                elif event.key == pygame.K_a:
                    hero.orientation=2
                    hero.walk=True
                elif event.key == pygame.K_w:
                    hero.orientation=3
                    hero.walk=True
                elif event.key == pygame.K_s:
                    hero.orientation=4
                    hero.walk=True
                elif event.key == pygame.K_RIGHT:
                    hero2.orientation=1
                    hero2.walk=True
                elif event.key == pygame.K_LEFT:
                    hero2.orientation=2
                    hero2.walk=True
                elif event.key == pygame.K_UP:
                    hero2.orientation=3
                    hero2.walk=True
                elif event.key == pygame.K_DOWN:
                    hero2.orientation=4
                    hero2.walk=True
            elif event.type== pygame.KEYUP:
                    if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_w or event.key == pygame.K_s:
                        hero.walk=False
        screen.fill((250,250,250))


        hero2.blitme()

        hero.blitme()
        pygame.display.flip()
run_game()