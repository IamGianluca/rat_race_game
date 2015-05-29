# Constants for the contents of the maze.
WALL = '#'
HALL = '.'
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.
LEFT = -1
RIGHT = 1
NO_CHANGE = 0
UP = -1
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
        self.num_sprouts_eaten = num_sprouts_eaten

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

class Maze(object):
    """ A 2D maze. """

    def __init__(self, maze, rat1, rat2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        :param maze represents the maze to be initialized
        :param rat1 the second parameter represents the contents of the maze
        :param rat2 the third parameter represents the first rat in the maze
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
        >>> maze.num_sprouts_left
        3
        """
        self.maze = maze
        self.rat1 = rat1
        self.rat2 = rat2

        count = 0
        for i in range(0, len(maze)):
            for n in range(0, len(maze[0])):
                if maze[i][n] == SPROUT:
                    count += 1

        self.num_sprouts_left = count

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
        if self.maze[row][column] == WALL:
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

    def move(self, rat_temp, row, column):
        """ (Maze, Rat, int, int) -> bool

        :param rat_temp: the rat we want to move
        :param row: a vertical direction change (UP, NO_CHANGE or DOWN)
        :param column: a horizontal direction change (LEFT, NO_CHANGE or RIGHT)
        :return: Move the rat in the given direction, unless there is a wall in the way. Also, check for a Brussels
          sprout at that location and, if present: have the rat eat the Brussels sprout, make that location a HALL, and
          decrease the value that num_sprouts_left refers to by one. Return True if and only if there wasn't a wall
          in the way.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
        ['#', '.', '.', '.', '.', '.', '#'], \
        ['#', '.', '#', '#', '#', '.', '#'], \
        ['#', '.', '.', '@', '#', '.', '#'], \
        ['#', '@', '#', '.', '@', '.', '#'], \
        ['#', '#', '#', '#', '#', '#', '#']], \
        Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze.move(Rat('J', 1, 1), UP, NO_CHANGE)
        False
        >>> maze.move(Rat('J', 1, 1), DOWN, NO_CHANGE)
        True
        """

        # 1. First you want to find out which position "the rat" currently has (save the position, "somewhere").
        # 2. Then "check" the vertical and the horizontal variables and perform the position changes provided.
        # 3. Then you have to check if that new position is a wall, if it is a wall return false (in other words, no movement occurs and the function call terminates).
        # 4. Otherwise you know that the movement is allowed and can therefore check if the new position contains a sprout. If the new position contains a sprout you will have to "eat it", delete it from the maze and lower the total number of sprouts left.
        # 5. Regardless of whether the new position contained a sprout or not, you should now change the position of your rat to that new position.
        # 6. Then simply return true, because the move was successful.

        initial_position_row = rat_temp.row
        initial_position_column = rat_temp.column

        if row == UP:
            rat_temp.set_location(initial_position_row - 1, initial_position_column)
        if row == DOWN:
            rat_temp.set_location(initial_position_row + 1, initial_position_column)
        if column == LEFT:
            rat_temp.set_location(initial_position_row, initial_position_column - 1)
        if column == RIGHT:
            rat_temp.set_location(initial_position_row, initial_position_column + 1)

        # Check if
        if self.is_wall(rat_temp.row, rat_temp.column):
            return False
        else:
            if self.get_character(rat_temp.row, rat_temp.column) == SPROUT:
                rat_temp.eat_sprout()
                self.num_sprouts_left -= 1
            return True

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
        >>> maze.move(Rat('J', 1, 1), 'DOWN', 'NO_CHANGE')
        #######
        #...P.#
        #J###.#
        #..@#.#
        #@#.@.#
        #######
        J at (2, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        # Place rats in the maze
        self.maze[self.rat1.row][self.rat1.column] = RAT_1_CHAR
        self.maze[self.rat2.row][self.rat2.column] = RAT_2_CHAR

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