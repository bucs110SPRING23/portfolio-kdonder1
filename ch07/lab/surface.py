import rectangle

class Surface:
    """
    Defines the x, y, h, and w coordinates of a rectangle.
    """
    def __init__(self, filename, x, y, height, width):
        self.rect = rectangle.Rectangle(x, y, height, width)
        self.image = filename

    """
    Returns the dimensions of the rectangle.
    """
    def getRect(self):
        return self.rect
