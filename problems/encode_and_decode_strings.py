'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''

class Coder():
    def decode(self, input):
        result = ''

        i = 0

        while i < len(input):
            # get that phrase
            if input[i].isnumeric():
                times = int(input[i])

                phrase = ''
                while input[i] != ']':
                    if input[i].isalpha():
                        phrase += input[i]

                    i += 1

                result += phrase * times
                i += 1

        return result

    def test_1(self):
        input = "3[a]2[bc]"
        output = "aaabcbc"
        self.test(input, output)

    def test_2(self):
        input = "3[a2[c]]"
        output = "accaccacc"
        self.test(input, output)

    def test(self, input, output):
        ans = self.decode(input)
        print(ans, ans == output)

def encode_and_decode_strings():
    coder = Coder()
    coder.test_1()
