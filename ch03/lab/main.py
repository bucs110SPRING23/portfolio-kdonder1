import random
import pygame
import math

pygame.init()
window = pygame.display.set_mode([864, 864])
window.fill('darkblue')

screensize = window.get_size()
print(screensize)
length = screensize[0]
width = screensize[1]

## PART A: Screen + Dartboard
# circle: surface, color, center, radius
pygame.draw.circle(window, 'red', [length / 2, width / 2], width / 2)
pygame.draw.circle(window, 'black', [length / 2, width / 2], width / 2, 4)
pygame.draw.circle(window, 'white', [length / 2, width / 2], width / 2 - 120)
pygame.draw.circle(window, 'red', [length / 2, width / 2], width / 2 - 240)
pygame.draw.circle(window, 'white', [length / 2, width / 2], width / 2 - 360)

# line(surface, color, start_pos, end_pos)
pygame.draw.line(window, 'black', [length / 2, 0], [length / 2, width], 3)
pygame.draw.line(window, 'black', [0, width / 2], [length, width / 2], 3)


## PART B: Dart throwing
# Does the dart land within the circle?
print(width / 2)

for i in range(10):
    x = random.randrange(int(length))
    y = random.randrange(int(width))
    distance_from_center = math.hypot(x-length/2, y-width/2) #the distance formula
    is_in_circle = distance_from_center <= width/2 #screen width
    if is_in_circle:
        pygame.draw.circle(window, 'green', [x, y], 6)
        print("passes", distance_from_center)
    else:
        pygame.draw.circle(window, 'orange', [x, y], 6)
        print("doesn't pass", distance_from_center)
    pygame.display.flip()
    pygame.time.wait(300)

pygame.display.flip()
pygame.time.wait(3000)

# window.exitonclick()
