"""Object oriented Battle Ships game.

Writen using GitHub Copilot. 
This project was to complex for Copilot to generate the whole code.
I had to force the data structure and do some debugging.

For example Copilot used referens comparison for points but value comparision was needed.
"""

class Point:
    """Point in 2D space."""
    def __init__(self, column = 0, row = 0):
        """Call constructor to create a point in 2D space.
        
        Keyword arguments:
        column: int
        row: int
        """
        self.column = column
        self.row = row

    def __eq__(self, other):
        """Check if two points are equal.
        
        For example point_1 == point_2
        """
        return self.column == other.column and self.row == other.row

class ShipPart:
    """Part of a ship."""
    def __init__(self, point):
        """Call constructor to create a ship part.
        
        Keyword arguments:
        point: Point in 2D space.
        """
        self.point = point
        self.hit = False

    def try_hit(self, point):
        """Returns True if the given point is the same as the ship part point. """
        if point.row == self.point.row and point.column == self.point.column:
            self.hit = True
            return True
        return False

    def is_hit(self):
        """Returns True if the ship part has been hit. """
        return self.hit

class Ship:
    """Ship in the game."""
    def __init__(self, length=2, start_point=Point(0,0), orientation='right'):
        """Call constructor to create a ship.

        Keyword arguments:
        length: int -- length of the ship.
        start_point: Point -- starting point of the ship.
        orientation: str -- orientation of the ship. 'right' or 'down'.
        """
        self.length = length

        self.hits = 0
        self.ship_parts = []
        if orientation == 'right':
            for x in range(length):
                self.ship_parts.append(ShipPart(Point(start_point.column + x, start_point.row)))
        elif orientation == 'down':
            for y in range(length):
                self.ship_parts.append(ShipPart(Point(start_point.column, start_point.row + y)))

    def try_hit(self, point):
        """Returns True if the given point is within the ship."""
        for ship_part in self.ship_parts:
            if ship_part.try_hit(point):
                self.hits += 1
                return True
        return False
            

    def is_sunk(self):
        """Returns True if all ship parts have been hit."""
        return self.hits == self.length
    
class Board:
    """Game board."""
    def __init__(self, width = 8, height = 8):
        """Call constructor to create a game board.
        
        Keyword arguments:
        width: int -- width of the board.
        height: int -- height of the board.
        """
        self.width = width
        self.height = height
        self.ships = []
        self.hits = []
        self.misses = []

    def add_ship(self, ship):
        """Add a ship to the board.
        
        Keyword arguments:
        ship: Ship -- ship to add to the board."""
        self.ships.append(ship)

    def try_hit(self, point):
        """Try to hit an oponents ship.
        
        Keyword arguments:
        point: Point -- point to try hit.´
        
        Returns True if the given point is a hit.
        """
        for ship in self.ships:
            if ship.try_hit(point):
                self.hits.append(point)
                return True
        self.misses.append(point)
        return False

    def is_game_over(self):
        """Returns True if all ships have been sunk."""
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def print(self):
        """Print the board."""
        for y in range(self.height):
            for x in range(self.width):
                point = Point(x, y)
                if point in self.hits:
                    print('X', end='')
                elif point in self.misses:
                    print('O', end='')
                else:
                    print('.', end='')
            print()

class Game:
    """Game of Battle Ships."""
    def __init__(self, width, height):
        """Call constructor to create a game of Battle Ships."""
        self.board = Board(width, height)

    def add_ship(self, length, start_point, orientation):
        """Add a ship to the game board.
        
        Keyword arguments:
        length: int -- length of the ship.
        start_point: Point -- starting point of the ship.
        orientation: str -- orientation of the ship. 'right' or 'down'.
        """
        self.board.add_ship(Ship(length, start_point, orientation))

    def play(self):
        """Start the game."""
        while not self.board.is_game_over():
            self.board.print()
            column = int(input('Enter column: '))
            row = int(input('Enter row: '))
            point = Point(column, row)
            if self.board.try_hit(point):
                print('Hit!')
            else:
                print('Miss!')
        self.board.print()
        print('Game over!')

game = Game(8, 8)
game.add_ship(3, Point(0, 0), 'right')
game.play()
