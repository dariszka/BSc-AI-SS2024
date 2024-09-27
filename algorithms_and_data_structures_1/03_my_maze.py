from typing import List, Tuple

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class MyMaze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str = ''):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string,
            where rows are separated by newlines (\n).

        Raises:
            ValueError, if maze_str is empty.
        """
        if len(maze_str) == 0:
            raise ValueError
        else:
            # We internally treat this as a List[List[str]], as it makes indexing easier.
            self._maze = list(list(row) for row in maze_str.splitlines())
            self._row_range = len(self._maze)
            self._col_range = len(self._maze[0])
            self._exits: List[Tuple[int, int]] = []
            self._max_recursion_depth = 0

    def find_exits(self, start_row: int, start_col: int, depth: int = 0) -> bool:
        """Find and save all exits into `self._exits` using recursion, save 
        the maximum recursion depth into 'self._max_recursion_depth' and mark the maze.

        An exit is an accessible from S empty cell on the outer rims of the maze.

        Args:
            start_row (int): row to start from. 0 represents the topmost cell.
            start_col (int): column to start from; 0 represents the leftmost cell.
            depth (int): Depth of current iteration.

        Raises:
            ValueError: If the starting position is out of range or not walkable path.
        """
        # handle errors

        valid_row = 0 <= start_row < self._row_range 
        valid_col = 0 <= start_col < self._col_range

        if depth == 0:
            if not valid_row or not valid_col or self._maze[start_row][start_col] != PATH:
                raise ValueError('The starting position is out of range or not walkable path.')
  
        found_exit = False

        # handle finding an exit

        outer_rims_row = start_row == 0 or start_row == (self._row_range - 1)
        outer_rims_col = start_col == 0 or start_col == (self._col_range - 1)

        if outer_rims_row or outer_rims_col:                                                # recursion anchor
            self._maze[start_row][start_col] = EXIT
            self._exits.append((start_row, start_col))
            return True
        
        # handle neighbors iteration

        self._maze[start_row][start_col] = START if depth==0 else VISITED

        neighbors = [(start_row, start_col+1),  # east
                    (start_row+1, start_col+1), # southeast
                    (start_row+1, start_col),   # south
                    (start_row+1, start_col-1), # southwest
                    (start_row, start_col-1),   # west
                    (start_row-1, start_col-1), # northwest
                    (start_row-1, start_col),   # north
                    (start_row-1, start_col+1)] # northeast 
        
        depth+=1
        self._max_recursion_depth = max(depth, self._max_recursion_depth)

        for row, col in neighbors:
            if 0 <= row < self._row_range and 0 <= start_col < self._col_range:
                if self._maze[row][col] == PATH:
                    found_exit = self.find_exits(row, col, depth) or found_exit            # recursive call
                    
        return found_exit

    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__


if __name__ == '__main__':
    
    maze15= '''###############
#      #      #
###   ######  #
#     ####### #
# ##          #
#   #######   #
### #         #
              #
#          ## #
##### #  ###   
#         ##  #
# ########## ##
#          # ##
#   ##       ##
########## ####'''

    maze20= '''####################
#      ########### #
###        ######  #
#     ####     ### #
# ##               #
#   #######        #
### #############  #
                   #
#               ## #
##### #  ###        
#         ##       #
# ##########      ##
#          #      ##
#   ##  ######### ##
#                  #
###############    #
#   #              #
#   #               
######### #######  #
####################'''

    maze15 = MyMaze(maze15)
    maze20 = MyMaze(maze20)

    start_row, start_col = 1,1

    found_exit15 = maze15.find_exits(start_row, start_col)
    max_rd15 = maze15.max_recursion_depth
    exits15 = maze15.exits

    print(found_exit15, max_rd15, exits15)
    print(maze15.__str__())

    found_exit20 = maze20.find_exits(start_row, start_col)
    max_rd20 = maze20.max_recursion_depth
    exits20 = maze20.exits

    print(found_exit20, max_rd20, exits20)
    print(maze20.__str__())