import sys

from problems.minimum_window_substring import minimum_window_substring
from problems.calculator import calculator

# relevant
from problems.edit_distance import edit_distance
from problems.pancake_sorting import pancake_sorting
from problems.encode_and_decode_strings import encode_and_decode_strings
from problems.rook_captures import rook_captures
from problems.course_schedule import course_schedule
from problems.squirrel_simulation import squirrel_simulation
from problems.text_justification import text_justification

# index == leetcode #
p = {
    0: minimum_window_substring,
    1: calculator,
    72: edit_distance,
    969: pancake_sorting, # status: close but not quite
    271: encode_and_decode_strings,
    999: rook_captures, # done, think about + test w edge cases
    # dfs, tree traversal
    207: course_schedule, # not working
    # dfs
    573: squirrel_simulation,
    # greedy
    68: text_justification, # doing on leetcode, have logic + most of code but made code too janky
}

# ex: to run leetcode # 999 -> python problems.py 999
if __name__=='__main__':
    prob_num = int(sys.argv[1])
    p[prob_num]()

'''
- trees
- dfs
- graph traversal

TODO: 
- analyzing time/space comp
- what questions to ask 
- email carolyn

DYNAMIC PROGRAMMING ? or recursion
letter_combinations_of_a_phone_nmber
combination_sum

DFS/RECURSION
[x]number_of_islands
[x]available_captures_for_rook
[/]implement_trie                            # working on leetcode butttt time limit exceeded

edit_distance
text_justification
pancake_sorting
encode_decode_strings
decode_ways
alien_dictionary
add_strings
construct_binary_tre..
word_ladder
course_schedule_ii
3_sum
word_break
squirrel_simulation
falling_squares
'''
