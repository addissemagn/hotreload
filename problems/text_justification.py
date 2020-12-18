'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
'''

class Justify():
    def justify(self, words, maxWidth):
        return words

    def test_1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        output = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        ans = self.justify(words, maxWidth)
        print(ans, ans == output)

    def run_tests(self):
        self.test_1()

def text_justification():
    justifier = Justify()
    justifier.run_tests()
