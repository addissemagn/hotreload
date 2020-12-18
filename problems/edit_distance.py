'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''

class WordConvert():
    def convert(self, w1, w2):
        return w1

    def test_1(self):
        w1 = "horse"
        w2 = "ros"
        output = 3

        ans = self.convert(w1, w2)
        print(ans, ans == output)

    def test_2(self):
        w1 = "intention"
        w2 = "execution"
        output = 5

        ans = self.convert(w1, w2)
        print(ans, ans == output)

def edit_distance():
    solution = WordConvert()
    solution.test_2()
