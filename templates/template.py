# template to get started
'''
-- figure out inputs and outputs needed
-- make a test case
'''
# NOTES TEMPLATE -------------------------------------------------------------------
'''
input (given):
output (goal):
'''


# CODE TEMPLATE --------------------------------------------------------------------

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
def main(): 
    solution = Solution()
    solution.run_tests()

# NOTES -----------------------------------------------------------------------
'''
DICTS

dict.get() 
--  takes two params, the key you want, and a default if it doesn't exist

    my_dict = {}
    my_dict[some_key] = my_dict.get(some_key, 0) + 1

LISTS
init 2D array 
    width (cols) 3, height (rows) 2
    
    [[0] * 3] * 2 ->    [[0, 0, 0],
                         [0, 0, 0]]

'''
