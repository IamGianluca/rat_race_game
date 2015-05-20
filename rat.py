# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat(object):
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, column, num_sprouts_eaten = 0):
        """ (Rat, str, int, int) -> NoneType

        Initialise an instance of class Rat

        :param symbol: the 1-character symbol for the rat
        :param row: the row where the rat is located
        :param column: the column where the rate is located

        >>> jesse = Rat("J", 1, 1, 0)
        >>> jesse.row
        1
        >>> jesse.symbol
        'J'
        """
        self.symbol = symbol
        self.row = row
        self.column = column
        self.num_sprouts_eaten = num_sprouts_eaten  # the number of sprouts that this rat has eaten, which is initially 0

    def set_location(self, row, column):
        """ (Rat, int, int) -> NoneType

        Set the Rat's row and col instance variables to the given row and column.

        >>> jesse = Rat("J", 1, 1, 0)
        >>> jesse.set_location(1, 2)
        >>> jesse.row
        1
        >>> jesse.column
        2
        """
        self.row = row
        self.column = column

    def eat_sprout(self):
        """ (Rat) -> NoneType

        The first parameter represents a rat. Add one to the rat's instance variable

        >>> jesse = Rat("J", 1, 1, 0)
        >>> jesse.eat_sprout()
        >>> jesse.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        The first parameter represents a rat. Return a string representation of the rat, in this format:
          symbol at (row, col) ate num_sprouts_eaten sprouts.

        A legit output could be something like: 'J at (4, 3) ate 2 sprouts.'
        Do not put a newline character ('\n') at the end of the string.

        >>> jesse = Rat("J", 1, 1, 0)
        >>> jesse.__str__()
        'J at (1, 1) ate 0 sprouts'
        """
        return '{0} at ({1}, {2}) ate {3} sprouts'.format(self.symbol, self.row, self.column, self.num_sprouts_eaten)


if __name__ == "__main__":
    import doctest
    doctest.testmod()