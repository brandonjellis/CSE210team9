from gamedata.entites.entity import Entity


class Banner(Entity):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self,color, position, velocity, default_text = ""):
        super().__init__(color, position, velocity, default_text)
        self._points = 0
        self._dtxt = default_text
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        msg = self._dtxt + str(points)
        self.set_text(msg)