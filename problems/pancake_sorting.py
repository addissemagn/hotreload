'''
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[1...k].
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.
'''

'''
STATUS:
-- close but not quite
'''

class Sorter():
    def __init__(self):
        self.nums = {} # using this to track of where everything is

    # reverse arr from i to j inclusive
    def reverse(self, arr, j):
        i = 0

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            self.nums[arr[i]] = i
            self.nums[arr[j]] = j

            i += 1
            j -= 1

        print(arr)

    # assumptions: integers in arr are unique; all nums from 1 to len(arr) present
    def sort(self, arr):
        # find max in array
        max_num = -1 * float('inf')

        # O(n)
        for i, num in enumerate(arr):
            self.nums[num] = i
            max_num = max(max_num, num)

        # bring max to beginning

        result = []

        while max_num >= 1:
            if self.nums[max_num] is not 0:
                result.append(self.nums[max_num])
                self.reverse(arr, self.nums[max_num])
           
            if self.nums[max_num] is not max_num - 1:
                result.append(self.nums[max_num])
                self.reverse(arr, max_num - 1)

            max_num -= 1

        return result

    def test_1(self):
        input = [3,2,4,1]
        output = [4,2,4,3]

        ans = self.sort(input)
        print(ans, ans == output)

def pancake_sorting():
    sorter = Sorter()
    sorter.test_1()
