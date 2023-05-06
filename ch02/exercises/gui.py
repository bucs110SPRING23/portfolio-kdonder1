import pygame

pygame.init()

screen = pygame.display.set_mode((100, 100))
screen.fill("red")
pygame.display.flip()
input("Press Enter to continue...")
screen.fill("green")
pygame.display.flip()
input("Press Enter to continue...")

# pygame keeps track of display image and next image