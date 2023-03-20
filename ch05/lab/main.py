import pygame

pygame.init()
display = pygame.display.set_mode()

## Part A:

def threenp1(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count


def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1, 1):
        value = threenp1(i)
        objs_in_sequence[i] = value
    return objs_in_sequence


## Part B:
def graph_coordinates(threenplus1_iters_dict):

    pygame.draw.lines(display, "black", True, threenplus1_iters_dict)
    new_display = pygame.transform.flip(display, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    display.blit(new_display, (0, 0))
    
    max_so_far = 0
    for i in range(upper_limit):
        






def main():
    display.fill("white")
    upper_limit = int(input("Input a number >= 2: "))
    print(threenp1range(upper_limit))
    threenplus1_iters_dict = threenp1range(upper_limit)
    graph_coordinates(threenplus1_iters_dict)

main()