import pygame

pygame.init()

screen = pygame.display.set_mode()

dimensions = screen.get_size() # [width, and height]
print(dimensions)
starting_point = [dimensions[0] // 2, (dimensions[1] // 2)]
# element 0 is width (x-value), element 1 is length (y-value)

# draw library
# [where to draw it, color, starting point, radius]
# where to draw it
# color: "red", [r,g,b] (0-255)
# starting opint [x,y]
# radius

screen.fill("blue")
radius = 100
for _ in range(9):
    pygame.draw.circle(screen, "white", starting_point, radius)
    pygame.draw.circle(screen, "black", starting_point, radius, 2)
    starting_point[1] = starting_point[1] - radius
    radius = radius // 2
    starting_point[1] = starting_point[1] - radius

pygame.display.flip()
pygame.time.wait(2000)