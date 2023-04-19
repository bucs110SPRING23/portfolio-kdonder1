import pygame

class Snowman(pygame.sprite.Sprite):
    
    ## makes a a backsplash for code to be built on
    def __init__(self, x, y, img = "assets.snowman.png")
        super().__init__()

        self.image = pygame.image.load
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y