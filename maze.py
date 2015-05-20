from rat import Rat

class Maze(object):
    """ A 2D maze. """

    def __init__(self, maze, rat1, rat2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        :param maze represents the maze to be initialized
        :param rat_1 the second parameter represents the contents of the maze
        :param rat_2 the third parameter represents the first rat in the maze
        :param num_sprouts_left represents the second rat in the maze

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
        ['#', '.', '.', '.', '.', '.', '#'], \
        ['#', '.', '#', '#', '#', '.', '#'], \
        ['#', '.', '.', '@', '#', '.', '#'], \
        ['#', '@', '#', '.', '@', '.', '#'], \
        ['#', '#', '#', '#', '#', '#', '#']], \
        Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze.rat1.symbol
        'J'
        >>> maze.rat2.column
        4
        """
        self.maze = maze
        self.rat1 = rat1
        self.rat2 = rat2

    def is_wall(self, row, column):
        """ (Maze, int, int) -> bool

        :param row:
        :param column:
        :return: boolean to show is the element is a wall

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
        ['#', '.', '.', '.', '.', '.', '#'], \
        ['#', '.', '#', '#', '#', '.', '#'], \
        ['#', '.', '.', '@', '#', '.', '#'], \
        ['#', '@', '#', '.', '@', '.', '#'], \
        ['#', '#', '#', '#', '#', '#', '#']], \
        Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze.is_wall(0, 0)
        True
        >>> maze.is_wall(4, 4)
        False
        """
        if self.maze[row][column] == '#':
            return True
        else:
            return False

    def __str__(self):
        """ (Maze) -> str

        :return: print maze to the screen

        >>>
        """
        return "{0} \n {1} \n {2}".format(self.maze, self.rat1.__str__, self.rat2.__str__)


if __name__ == "__main__":
    import doctest
    doctest.testmod()