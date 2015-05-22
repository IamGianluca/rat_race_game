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

        :param row: row to check
        :param column: column to check
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

    def get_character(self, row, column):
        """ (Maze, int, int) -> str

        :param row: row to check
        :param column: column to check
        :return Return the character in the maze at the given row and column. If there is a rat at that location,
          then its character should be returned rather than HALL.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
        ['#', '.', '.', '.', '.', '.', '#'], \
        ['#', '.', '#', '#', '#', '.', '#'], \
        ['#', '.', '.', '@', '#', '.', '#'], \
        ['#', '@', '#', '.', '@', '.', '#'], \
        ['#', '#', '#', '#', '#', '#', '#']], \
        Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.get_character(0, 0)
        '#'
        """
        if (row, column) == (self.rat1.row, self.rat1.column):
            return self.rat1.symbol
        elif (row, column) == (self.rat2.row, self.rat2.column):
            return self.rat2.symbol
        else:
            return self.maze[row][column]

    def move(self, rat, row, column):
        """ (Maze, Rat, int, int) -> bool

        :param rat:
        :param row: a vertical direction change (UP, NO_CHANGE or DOWN)
        :param column: a horizontal direction change (LEFT, NO_CHANGE or RIGHT)
        :return: Move the rat in the given direction, unless there is a wall in the way. Also, check for a Brussels
          sprout at that location and, if present: have the rat eat the Brussels sprout, make that location a HALL, and
          decrease the value that num_sprouts_left refers to by one. Return True if and only if there wasn't a wall
          in the way.

        >>>
        """

    def __str__(self):
        """ (Maze) -> str
        TO-DO (grossi): Use unitest module to do proper unit tests. Doctest is a more visual way to do this, which is
          not always advisable. For instance in this case I cannot check the output of maze.__str__ but have to use
          the print command

        :return: print maze to the screen

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
        ['#', '.', '.', '.', '.', '.', '#'], \
        ['#', '.', '#', '#', '#', '.', '#'], \
        ['#', '.', '.', '@', '#', '.', '#'], \
        ['#', '@', '#', '.', '@', '.', '#'], \
        ['#', '#', '#', '#', '#', '#', '#']], \
        Rat('J', 1, 1), Rat('P', 1, 4))
        >>> print maze
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        # Place rats in the maze
        self.maze[self.rat1.row][self.rat1.column] = self.rat1.symbol
        self.maze[self.rat2.row][self.rat2.column] = self.rat2.symbol

        # Cast maze to string format
        maze_string = ""
        for row in self.maze:
            for c in row:
                maze_string += str(c)
            maze_string += "\n"

        # TO-DO (grossi): find a less hacky way to do this
        # Remove last newline
        maze_string = maze_string[:-1]

        return "{0}\n{1}.\n{2}.".format(str(maze_string), str(self.rat1), str(self.rat2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()