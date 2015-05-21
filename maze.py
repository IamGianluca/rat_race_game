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