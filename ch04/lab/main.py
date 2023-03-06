import random
import pygame
import math

pygame.init()
window = pygame.display.set_mode([864, 864])
window.fill('lightgrey')



## SCREEN: 
screensize = window.get_size()
print(screensize)
length = screensize[0]
width = screensize[1]


# circle: surface, color, center, radius
pygame.draw.circle(window, 'orange', [length / 2, width / 2], width / 2)
pygame.draw.circle(window, 'black', [length / 2, width / 2], width / 2, 2)
pygame.draw.circle(window, 'white', [length / 2, width / 2], 324)
pygame.draw.circle(window, 'orange', [length / 2, width / 2], 216)
pygame.draw.circle(window, 'white', [length / 2, width / 2], 108)

# line(surface, color, start_pos, end_pos)
pygame.draw.line(window, 'black', [length / 2, 0], [length / 2, width])
pygame.draw.line(window, 'black', [0, width / 2], [length, width / 2])


# PART B, buttons:
# surface, color, [x, y, width, height]

redbox = pygame.Rect(10, width - 120, 90, 70)
bluebox = pygame.Rect(length - 100, width - 120, 90, 70)

pygame.draw.rect(window, 'blue', bluebox)
pygame.draw.rect(window, 'black', [length - 100, width - 120, 90, 70], 2)
pygame.draw.rect(window, 'red', redbox)
pygame.draw.rect(window, 'black', [10, width - 120, 90, 70], 2)

font = pygame.font.Font(None, 48)
text = font.render("Select which player you think will win:", True, "black")
window.blit(text, (130, 20)) # where <x> and<y> are coordinates on screen
pygame.display.flip()


redpoints = 0
bluepoints = 0
guess = ""

while guess == "":
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if redbox.collidepoint(event.pos):
                guess = "red"
            elif bluebox.collidepoint(event.pos):
                guess = "blue"


for i in range(20):
    x = random.randrange(int(length))
    y = random.randrange(int(width))
    distance_from_center = math.hypot(x-length/2, y-width/2) #the distance formula
    is_in_circle = distance_from_center <= width/2 #screen width
    if is_in_circle:
        if i % 2 == 0:
            pygame.draw.circle(window, 'red', [x, y], 6)
            redpoints += 1
        else:
            pygame.draw.circle(window, 'blue', [x, y], 6)
            bluepoints += 1
    else:
        if i % 2 == 0:
            pygame.draw.circle(window, 'darkred', [x, y], 6)
        else:
            pygame.draw.circle(window, 'darkblue', [x, y], 6)
    pygame.display.flip()
    pygame.time.wait(300)

print(guess)
print("Red scored", redpoints, "points!")
print("Blue scored", bluepoints, "points!")

font = pygame.font.Font(None, 48)

if redpoints > bluepoints:
    if guess == "red":
        print("Correct! Red wins!")
        text = font.render("Correct! Red wins!", True, "black")
        window.blit(text, [length / 2 - 170, width / 2 - 16]) # where <x> and<y> are coordinates on screen
    else:
        print("Incorrect! Red wins!")
        text = font.render("Incorrect! Red wins!", True, "black")
        window.blit(text, [length / 2 - 170, width / 2 - 16])
elif bluepoints > redpoints:
    if guess == "blue":
        print("Correct! Blue wins!")
        text = font.render("Correct! Blue wins!", True, "black")
        window.blit(text, [length / 2- 170, width / 2 - 16])
    else:
        print("Incorrect! Blue wins!")
        text = font.render("Incorrect! Blue wins!", True, "black")
        window.blit(text, [length / 2- 80, width / 2 - 16])        
else:
    print("Tie!")
    text = font.render("There's a tie!", True, "black")
    window.blit(text, [length / 2- 80, width / 2 - 16])
pygame.display.flip()




pygame.display.flip()
pygame.time.wait(2500)