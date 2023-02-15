import pygame

pygame.init()
screen = pygame.display.set_mode()

screen_size = screen.get_size()

screen.fill("blue")

print(screen_size)

# Ground
# [x, y, width, height]
pygame.draw.rect(screen, "white", [0, 600, screen_size[0], 300])
pygame.draw.rect(screen, "black", [0, 600, screen_size[0], 300], 3)

# Trees
# surface, color, center, radius
pygame.draw.rect(screen, "brown", [60, 0, 60, 825])
pygame.draw.rect(screen, "black", [60, 0, 60, 825], 3)
pygame.draw.circle(screen, "green", [60, 10], 300)
pygame.draw.circle(screen, "black", [60, 10], 300, 3)
pygame.draw.circle(screen, "green", [120, 500], 60)
pygame.draw.circle(screen, "black", [120, 500], 60, 3)

pygame.draw.rect(screen, "brown", [370, 0, 60, 810])
pygame.draw.rect(screen, "black", [370, 0, 60, 810], 3)
pygame.draw.circle(screen, "green", [370, 10], 200)
pygame.draw.circle(screen, "black", [370, 10], 200, 3)
pygame.draw.circle(screen, "green", [450, 500], 60)
pygame.draw.circle(screen, "black", [450, 500], 60, 3)

pygame.draw.rect(screen, "brown", [200, 0, 60, 750])
pygame.draw.rect(screen, "black", [200, 0, 60, 750], 3)
pygame.draw.circle(screen, "green", [200, 10], 200)
pygame.draw.circle(screen, "black", [200, 10], 200, 3)
pygame.draw.circle(screen, "green", [190, 350], 60)
pygame.draw.circle(screen, "black", [190, 350], 60, 3)

pygame.draw.rect(screen, "brown", [1300, 0, 60, 705])
pygame.draw.rect(screen, "black", [1300, 0, 60, 705], 3)
pygame.draw.circle(screen, "green", [1250, 350], 60)
pygame.draw.circle(screen, "black", [1250, 350], 60, 3)
pygame.draw.circle(screen, "green", [1250, 60], 220)
pygame.draw.circle(screen, "black", [1250, 60], 220, 3)

pygame.draw.rect(screen, "brown", [1400, 0, 60, 840])
pygame.draw.rect(screen, "black", [1400, 0, 60, 840], 3)
pygame.draw.circle(screen, "green", [1480, 200], 60)
pygame.draw.circle(screen, "black", [1480, 200], 60, 3)
pygame.draw.circle(screen, "green", [1480, 50], 200)
pygame.draw.circle(screen, "black", [1480, 50], 200, 3)
pygame.draw.circle(screen, "green", [1500, 500], 60)
pygame.draw.circle(screen, "black", [1500, 500], 60, 3)

pygame.draw.rect(screen, "brown", [1150, 0, 60, 650])
pygame.draw.rect(screen, "black", [1150, 0, 60, 650], 3)
pygame.draw.circle(screen, "green", [1120, 500], 60)
pygame.draw.circle(screen, "black", [1120, 500], 60, 3)
pygame.draw.circle(screen, "green", [1120, 40], 170)
pygame.draw.circle(screen, "black", [1120, 40], 170, 3)



# Snowman
pygame.draw.circle(screen, "white", [screen_size[0] / 2, 530], 100)
pygame.draw.circle(screen, "black", [screen_size[0] / 2, 530], 100, 3)

pygame.draw.circle(screen, "white", [screen_size[0] / 2, 400], 70)
pygame.draw.circle(screen, "black", [screen_size[0] / 2, 400], 70, 3)

pygame.draw.circle(screen, "white", [screen_size[0] / 2, 300], 50)
pygame.draw.circle(screen, "black", [screen_size[0] / 2, 300], 50, 3)
pygame.display.flip()
pygame.time.wait(2500)