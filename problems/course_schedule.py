'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
'''

'''
SOLUTION:
case: passes
    input [1, 0] [0, 5]
    explanation: to take 1, you need 0. to take 0, you need 5.
    graph:
        1 -> 0
        0 -> 5
        
        need 3 courses
    solve:
        make graph
        start w first course needed in the input
        if in graph, then has a prereq. if not, then done.
        move to prereq. 
            if this course has already been encountered then cycle -> break -> impossible
            else then increment count of courses need
        rinse and repeat till no prereq found

        # initialize
        curr_course = 1
        count = 1
        has_prereq = True
        courses_need = [1]

        curr_course = 0 # prereq
        cycle = curr_course in courses_needed = False
        count = 2
        has_prereq = True # 0 exists on the graph (i.e. dict)
        couses_needed = [1, 0]

        curr_course = 5 # prereq
        cycle = False
        count = 3
        has_prereq = False # is not in the graph
        courses_needed = [1, 0, 5]

case: cycle
    input [1, 0] [0, 1]
    graph   1 -> 0
            0 -> 1


'''

class Scheduler():
    def scheduler(self, num_courses, reqs):
        if len(reqs) == 0:
            return

        self.courses = {} # key: the course you want to take, val: the prereq for it

        # make reqs into dict tree
        for req in reqs:
            self.courses[req[0]] = req[1]

        count = 0
        needed = []

        # initialize
        curr_course = reqs[0][0]
        needed.append(curr_course)
        count += 1

        while count <= num_courses:

            # does this have a prereq
            if curr_course in self.courses:
                curr_course = self.courses[curr_course]
            else: # done, no prereqs
                return True

            # detect cycle
            if curr_course in needed:
                return False

            needed.append(curr_course)
            count += 1

    def test_1(self):
        num = 2
        reqs = [[1, 0]]
        output = True
        ans = self.scheduler(num, reqs)
        print(ans, ans == output)

    def test_2(self):
        num = 2
        reqs = [[1, 0], [0, 1]]
        output = False
        ans = self.scheduler(num, reqs)
        print(ans, ans == output)

    def run_tests(self):
        self.test_1()
        self.test_2()

def course_schedule():
    scheduler = Scheduler()
    scheduler.run_tests()
