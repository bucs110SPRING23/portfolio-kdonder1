class Rectangle:
    """
    A class representating a rectange with instances x, y, h, w.
    """
    def __init__(self, x, y, height, width):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(height)
        self.width = abs(width)
    
    def __str__(self):
        """
        Returns the rectangle dimensions
        """
        return f"x: ({self.x}, y:{self.y}), height: {self.height}, width: {self.width}"
