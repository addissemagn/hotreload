'''
LESSONS:
- pay attension to where you need the dfs to be, if its searching the whole board then within the dfs itself
    otherwise: then outside
'''

'''
PROBLEM:
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
'''

class Chess():
    def __init__(self):
        self.num = 0
        self.UP = (1, 0)
        self.DOWN = (-1, 0)
        self.RIGHT = (0, 1)
        self.LEFT = (0, -1)

    def dfs(self, grid, i, j, dir):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid):
            return

        if grid[i][j] == 'p':
            self.num += 1
            return

        if grid[i][j] == 'B':
            return

        self.dfs(grid, i + dir[0], j + dir[1], dir)

    def num_captures(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 'R':
                    self.num = 0
                    self.dfs(grid, i, j, self.UP)
                    self.dfs(grid, i, j, self.DOWN)
                    self.dfs(grid, i, j, self.RIGHT)
                    self.dfs(grid, i, j, self.LEFT)

        return self.num

    def test_1(self):
        input  = [[".",".",".",".",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".","R",".",".",".","p"],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."]]
        output = 3
        self.test(input, output)

    def test_2(self):
        input = [[".",".",".",".",".",".",".","."],
                 [".","p","p","p","p","p",".","."],
                 [".","p","p","B","p","p",".","."],
                 [".","p","B","R","B","p",".","."],
                 [".","p","p","B","p","p",".","."],
                 [".","p","p","p","p","p",".","."],
                 [".",".",".",".",".",".",".","."],
                 [".",".",".",".",".",".",".","."]]
        output = 0
        self.test(input, output)

    def test_3(self):
        input = [[".",".",".",".",".",".",".","."],
                 [".",".",".","p",".",".",".","."],
                 [".",".",".","p",".",".",".","."],
                 ["p","p",".","R",".","p","B","."],
                 [".",".",".",".",".",".",".","."],
                 [".",".",".","B",".",".",".","."],
                 [".",".",".","p",".",".",".","."],
                 [".",".",".",".",".",".",".","."]]
        output = 3
        self.test(input, output)

    def test(self, input, output):
        ans = self.num_captures(input)
        print(ans, ans == output)

def rook_captures():
    chess = Chess()
    chess.test_3()
