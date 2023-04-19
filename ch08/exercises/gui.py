class Player:
    def __init__(self,pnum =1):
        """_summary_
        Initialize the player object
        args: pnum (int) the player's id number
        """

        self.player_num = pnum
        self.lives = 5 # players always starts with 5 lives
        self.is_small = True # players always starts small
        self.speed = 5

class Score:
    def __init__(score, player_name, x, y):
        """
        Initialize the score board
        Args:
            score is the players current score
        """
        score.num = 0
        score.color = "white"
        score.font = 15
        score.position = (x,y)
        score.name = player_name
        msg = " "

class Points:
    def __init__(points):
        """
        points system in the game
        Args:
            points: what the tokens look like
        """
        points.regcolor = "gold"
        points.hit = True:
        points.regnum = 10
        points.powernum = 20
        points.position = "drop"
        points.sound = "ring"
        points.powercolor = "pink"
        