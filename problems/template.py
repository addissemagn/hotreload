# TODO: add questions to ask/considerations to make
# NOTES TEMPLATE

'''
- ask questions
- come up with test cases/edge cases
- describe brute force solution
- say 'can we do better?'

- work though an example
- write out approach
- double check approach
- start coding

- if too complex, break it down to simpler version and then build on it

questions to ask
- what's the most rewarding project you worked on and why
- if we were colleaques, what feedback would you give me from this session
- if you could instantly change or improve one thing about Square, what would it be
'''

'''
questions to ask
How big is the size of the input?
How big is the range of values?
What kind of values are there? Are there negative numbers? Floating points? Will there be empty inputs?
Are there duplicates within the input?
What are some extreme cases of the input?
How is the input stored? If you are given a dictionary of words, is it a list of strings or a trie?
'''

'''
things to write down
input (given):
output (goal):
test case(s):

write tests FIRST
'''

# CODE TEMPLATE
class Solution():
    def solver(self, input):
        return input

    def test_1(self):
        input = 'input'
        output = 'output'
        ans = self.solver(input)
        print(ans, ans == output)

    def run_tests():
        self.test_1()
        self.test_2()

# note: make this actually __name__=="__main__"
def __name__=="__main__": 
    solution = Solution()
    solution.run_tests()

# BACKTRACING -----------------------------------------------------------------
graph = {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']}

# this is to find one path, without cycles
def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

# find all paths, without cycles
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]           # path so far

    if start == end:                # found complete path
        return [path]

    if start not in graph:    # no steps left -> no path
        return []

    paths = []

    for node in graph[start]:
        if node not in path:        # only explore nodes not yet seen
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

# FIND ALL PATHS
#------------------------------------------------------------------------------
# if graph in DICT with arrays
paths = []

def myDFS(graph,start,end,path=[]):
    path=path+[start]
    if start==end: # found goal
        paths.append(path)
        return

    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            myDFS(graph,node,end,path)

### if in 2D array
paths = []
# right, left, down, up
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

find_all_paths(0, 0, [])

# might need to pass in grid
def find_all_paths(grid, i, j, path):
    path = path + [(i, j)]

    # if found goal
    if [goal condition] i.e. grid[i][j] == '1':
        paths.append(path)
        return 

    # keep looking
    for dir in dirs:
        i += dir[0]
        j += dir[1]
        
        # avoid cycles and out of bound coordinate
        if (i, j) not in path and in_bounds(grid, i, j):
            find_all_paths(grid, i, j, path)

    return paths # not needed cause global variable

def in_bounds(grid, i, j):
    return (0 <= i < len(grid) and 0 <= j < len(grid[0]))

#-----------------------------------------------------------------------------

# find shortest path, without cycles
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:                # found complete path
        return path

    if start not in graph:    # no steps left -> no path
        return None

    shortest = None

    for node in graph[start]:       # explore adjacent nodes...
        if node not in path:        # ... that have not yet been visited
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:             # if path found, store shortest found so far
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest

find_path(graph, 'A', 'D')

# NOTES -----------------------------------------------------------------------
'''
DICTS

dict.get() 
--  takes two params, the key you want, and a default if it doesn't exist

    my_dict = {}
    >>> my_dict[some_key] = my_dict.get(some_key, 0) + 1

LISTS
init 2D array 
    width (cols) 3, height (rows) 2
    >>> [[0] * 3] * 2 becomes [[0, 0, 0], [0, 0, 0]]

length 2D array
    rows = len(arr)
    cols = len(arr[0])

join array to string by seperator, i.e "" or ", "
    >>> "".join(array)

split string into array of chars
    >>> list(string)

filter
    >>> [x for x in numbers if is_odd(x)]
    >>> list(filter(is_odd, numbers))

'''
