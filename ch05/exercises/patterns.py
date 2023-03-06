rows = int(input("Please input the # of rows in your pyrimid: "))

def star_pyrimid():
    for i in range(rows):
        print("*" * (i + 1))

star_pyrimid()


def rstar_pyrimid():
    max = rows
    for i in range(rows, 0, -1): # start, stop, step
        print("*" * i)

rstar_pyrimid()