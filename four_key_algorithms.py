'''
## SLIDING WINDOW

APPROACH
-- A) have two pointers: left and right, starting at 0
-- B) increment right until all chars in set have been encountered
-- C) when set has been completed, increment left till one char in the set no
    longer lies within left and right (if smallest found so far, store this string)
-- D) repeat A and C while right is less than the lenght of the string

RECOGNIZING
-- question involves ordered sequence of elements
-- output is supposed to be a global min or max
-- trivial solution (testing all substrings) is O(n^2)
-- order doesn't matter (you're not matching patterns)

QUESTIONS
-- minimum window substring
-- given array of ints, find subarray with the largest total sum
-- given a string + a mapping from chars -> score (integer) + an integer n. 
    find the longest string with a score less than or equal to n
'''

'''
## NESTED INTERVALS

ALGORITHM
-- initialize an empty stack
-- iterate equation, when opening bracket encountered, push the char to stack
-- if closing char encountered, the equation is valid IF: the stack is not empty
    and if the popped item in the stack matches the closing char
-- if C is never violated and the stack is empty after iterating, return true;
    otherwise, false

QUESTIONS
-- given list of start and end times, return a list of merged times.
    hint: starting inteval vals are like opening brackets and ending vals are
    like cloding brackets. think about how you would sort these endpoints.
'''

'''
## RECURSION/SEARCH: DFS

QUESTIONS:
-- num islands
-- given a 2D grid of chars and a string, return if the word exists in the grid
-- bonus: given a set of words, return whether all the words are in the grid or not
    hint: look up prefix tree
-- given array of integers, count the # of inversions in it (# of inversions is
    the number of adjacent swaps needed to sort the array)
    hint: look up merge sort
-- NOTE: do sorting!! or at least know the ways to sort in python
'''

'''
## DYNAMIC PROGRAMMING

RECOGNIZING
-- involved when there are many "overlapping" subproblems to an algorithm
-- centers on using past solutions to improve the runtime of an algorithm


'''
