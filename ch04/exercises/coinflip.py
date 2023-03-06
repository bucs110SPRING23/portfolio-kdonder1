import random
import pygame

#pygame.Rect(x, y, width, height)
# x and y are top left corner coordinates

# pygame.Rect
# x and y coordinates
# width and height

# rectangles do not track


#Initialization
pygame.init()
screen = pygame.display.set_mode()


width, height = pygame.display.get_window_size()  #(w, h)
# returns as a tuple of 2 items (w, h)

# create hitboxes
hitbox_width = width / 2  # half the screen
hitbox_height = height / 2  # half the screen
# 2 halves make quarter

# Rectangle - keep track of size and position on screen

# sets up the box objects, does not position them
hitboxes = {
    "red": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "green": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "blue": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "purple" : pygame.Rect(0, 0, hitbox_width, hitbox_height)
}

# position hitboxes
hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright

# mydictionary = {"1":1, "b":2}
# mydictionary.keys()
# dict_keys(['a', 'b'])
# type(mydictionary.keys())
# <class 'dict_keys'>
## PROTIP: procrastination is good lol

# define hitbox colors
# Define main colors
main_colors = {
 "red": (200, 0, 0),
 "green": (0, 200, 0),
 "blue": (0, 0, 200),
 "purple": (200, 0, 200),
}
# Define highlight colors
highlight_colors = {
 "red": (255, 0, 0),
 "green": (0, 255, 0),
 "blue": (0, 0, 255),
 "purple": (255, 0, 255),
}


# additional state data

# font object
# - None = default font, or 'Arial'
font = pygame.font.Font(None, 48)

# state
done = False
result = []
turns = 0

# so i can shuffle a list of colors for each run through the game
keys = hitboxes.keys()
order = list(hitboxes.keys())

# invariant variables


def eventloop():
    # Mainloop
    ## each time through the while is one frame
    while not done: # True

        def respondtoevents():
            # 1. respond to events
            # top-down programming
            for event in pygame.event.get(): # gets all events since last call
                if event.type == pygame.KEYDOWN:
                    if pygame.QUIT == event.type:
                        done = True
                    if event.key == pygame.K_SPACE:
                        random.shuffle(order)
                        turns = len(order)
                        result = []

                        for color in order:
                            for c, hb in hitboxes.items():
                                pygame.draw.rect(screen, main_colors[c], hb)
                            pygame.draw.rect(screen, highlight_colors[color], hitboxes[color])
                            pygame.display.flip()
                            pygame.time.delay(1000)

                    elif event.key == pygame.K_q:
                        done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        turns = turns - 1
                        if hitboxes["red"].collidepoint(event.pos):
                            result.append("red")
                        elif hitboxes["purple"].collidepoint(event.pos):
                            result.append("purple")
                        elif hitboxes["green"].collidepoint(event.pos):
                            result.append("green")
                        elif hitboxes["blue"].collidepoint(event.pos):
                            result.append("blue")

        def update():
            # 2. updating data
            if len(result) == len(order):
                msg = [
                    "You entered: " + str(result),
                    "the correct pattern was: " + str(order),
                ]
                if result == order:
                    msg.append("Yay! You won.")
                else:
                    msg.append("Um, no.")
            elif turns:
                msg = ["Your turn"]
            else:
                msg.append("Press spacebar to play again... (q to quit)")

    def draw():
        # 3. Draw
        screen.fill("black")
        for c, hb in hitboxes.items():
            pygame.draw.rect(screen, main_colors[c], hb)

        if result:
            last_color_selected = result[-1] # result = ['red']
            pygame.draw.rect(
                screen,
                highlight_colors[last_color_selected],
                hitboxes[last_color_selected]
            )

    ypos = 60
    for m in msg:
        text = font.render(m, True, "white") # take my message and render it
        screen.blit(text, (20, ypos)) # blitting: taking something and putting it onto the screen, position is in top left corner
        ypos += 60

    # 4. display the sreen
    pygame.display.flip()
