"""
Notes:
-- create classes as much as possible

Tests:
-- try to identify corner cases, base cases, etc and THEN design

TODO: 
-- complexity
-- write down some common algorithms/solutions for reference (i.e dfs, bfs, etc) 
-- write common python thingies (sorting, list things, dicts)
-- linked lists
-- binary search trees??

Questions they already asked
-- poker
-- social media thing check if two people are mutuals given set of relationships: dfs
-- another dfs question where you had obstacles and shit
"""

#------------------------------------------------------------------------------
'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
'''
class NumIslands():
    def dfs(self, grid, i, j):
        if i >= len(grid) or j >= len(grid) or i < 0 or j < 0:
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def count(self, grid):
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def test(self):
        cases = []

        case = {}
        case['input'] = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        case['output'] = 1
        cases.append(case)

        case = {}
        case['input'] = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ] 
        case['output'] = 3
        cases.append(case)

        for test in cases:
            print(self.count(test['input']))

def number_of_islands():
    solution = NumIslands()
    solution.test()

#------------------------------------------------------------------------------
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
class BuySellStock():
    def maxProfit(self, arr):
        print(arr)
        return 1

    # solid test format for more complex tests
    def test1(self):
        input = [7,1,5,3,6,4] 
        output = 5
        answer = self.maxProfit(input)
        print(answer, answer == output)

    # solid test format for simple tests
    def test(self):
        cases = []
        cases.append([
            [7,1,5,3,6,4],
            5
        ])
        cases.append([
            [7,6,4,3,1],
            0
        ])
        
        for case in cases:
            answer = self.maxProfit(case[0])
            print(answer, answer == case[1])

def buy_sell_stock():
    solution = BuySellStock();
    solution.test1()

#------------------------------------------------------------------------------
'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
'''
class MinWindow():
    def minWindow(self, s, t):
        countMain = {}
        # need to go through and count how many of each character
        for i, char in enumerate(s):
            if char in countMain:
                countMain[char] += 1
            else: 
                countMain[char] = 1

        countSub = {}
        for i, char in enumerate(t):
            if char in countSub:
                countSub[char] += 1
            else:
                countSub[char] = 1

        print(countMain)
        print(countSub)

        i = 0
        while i < len(s):
            if count[char] > 1:
                count[char] -= 1
                i += 1
            else:
                break

        j = len(s) - 1
        while j >= 0:
            if count[char] > 1:
                count[char] -= 1
                j -= 1
            else:
                break

        print(i, j)

        return s[i: j+1]


    def test1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        output = "BANC"
        ans = self.minWindow(s, t)
        print(ans, ans == output)

def minimum_window_substring():
    solution = MinWindow()
    solution.test1()

#------------------------------------------------------------------------------

problems = {
    0: number_of_islands, # working, test in leetcode
    1: buy_sell_stock,
    2: minimum_window_substring, 
}

def main():
    problems[2]();
    
