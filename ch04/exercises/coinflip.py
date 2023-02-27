import random
import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = screen.get_window_size()

hitbox_width = width / 2
hitbox_height = height / 2


#pygame.Rect(x, y, width, height)
# x and y are top left corner coordinates

# pygame.Rect
# x an dy coordinates
# width and height

# rectangles do not track 


hitboxes = {
    "red": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "green": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "blue": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "purple" : pygame.Rect(0, 0, hitbox_width, hitbox_height)

}

hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright

font = pygame.font.SysFont("Arial", 24)

done = False
result = []
turns = 0
order = list(hitboxes.keys())

random.shuffle(order)

while not done: # we have to respond to every possible event

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random.shuffle(order)
                turns = len(order)
        elif event.type == pygame.MOUSEBUTTONDOWN:
                turns = turns -= 1
                if hitboxes["red"].collidepoint(event.pos):
                    result.append("red")
                elif hitboxes["green"].collidepoint(event.pos):
                    result.append("green")
                elif
                elif
    if turns == 0:
        if result == order:
            font.render("You win!", True, "white")
        else:
            font.render("Your win!", True, "white")

    screen.fill((0, 0, 0))

    for c, hb in hitboxes.items():
        box = pygame.draw.rect(screen, c, hb)
        screen.blit(box, hb)
