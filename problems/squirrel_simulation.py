'''
There’s a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions – up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
'''

'''
SOLUTION
notes:
-- minimal distance to collect all nuts and put them under tree

input
- tree position, squirel position, nuts positions
- board width, height (board represented by 2d grid)

output
- minimal distance to collect all nuts and put them under tree
- distance = number of moves
'''

class Squirrel():
    def solve(self, tree, squirrel, nuts, height, width):
        self.init_board(tree, squirrel, nuts, height, width)

        for i in range(height):
            for j in range(width):
                print(self.board[i][j])

        return self.board

    def init_board(self, tree, squirrel, nuts, height, width):
        self.board = [["."] * width] * height
        self.board[tree[0]][tree[1]] = "T"
        self.board[squirrel[0]][squirrel[1]] = "S"
        for nut in nuts:
            self.board[nut[0]][nut[1]] = "N"

    def test_1(self):
        height = 5
        width = 7
        tree = [2, 2]
        squirrel = [4, 4]
        nuts = [[3, 0], [2, 5]]
        output = 12

        ans = self.solve(tree, squirrel, nuts, height, width)
        print(ans, ans == output)

    def run_tests(self):
        self.test_1()

def squirrel_simulation():
    solution = Squirrel()
    solution.run_tests()
