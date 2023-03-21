import pygame

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
    pygame.init()
    display = pygame.display.set_mode()
    display.fill("white")
    tup_threenplus1_iters_dict = [(n, iters) for n, iters in threenplus1_iters_dict.items()]

    scaledtup_threenplus1_iters_dict = [(10*n, 5*iters) for n, iters in threenplus1_iters_dict.items()]

    pygame.draw.lines(display, "black", True, scaledtup_threenplus1_iters_dict)
    new_display = pygame.transform.flip(display, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    display.blit(new_display, (400, 400))
    
    iters_threenplus1_iters_dict = [tup[1] for tup in tup_threenplus1_iters_dict]
    max_so_far = iters_threenplus1_iters_dict[1]
    for i in range(len(iters_threenplus1_iters_dict)):
        if iters_threenplus1_iters_dict[i] > max_so_far:
            max_so_far = iters_threenplus1_iters_dict[i]
    
    font = pygame.font.Font(None, 40)
    msg = font.render(f"This is the max value from the 3n+1 function: {max_so_far}", True, "black")
    display.blit(msg, (10, 10))
    pygame.display.flip()
    pygame.time.wait(4000)        




def main():
    upper_limit = int(input("Input a number >= 2: "))
    threenplus1_iters_dict = threenp1range(upper_limit)
    print(threenp1range(upper_limit))
    graph_coordinates(threenplus1_iters_dict)
    print(graph_coordinates(threenplus1_iters_dict))

main()