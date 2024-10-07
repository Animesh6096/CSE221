def depth_first_search(course, adjacency, visited, result_stack):
    if visited[course] == 1:
        return False
    if visited[course] == 2:
        return True

    visited[course] = 1

    for next_course in adjacency[course]:
        if not depth_first_search(next_course, adjacency, visited, result_stack):
            return False

    visited[course] = 2
    result_stack.append(course)
    return True

def find_course_order(num_courses, prerequisites):
    adjacency = {i: [] for i in range(1, num_courses + 1)}
    for a, b in prerequisites:
        adjacency[a].append(b)

    visited = [0] * (num_courses + 1)
    result_stack = []

    for course in range(1, num_courses + 1):
        if not visited[course]:
            if not depth_first_search(course, adjacency, visited, result_stack):
                return "IMPOSSIBLE"

    return result_stack[::-1]

input_file = open('Lab5/input1a.txt', 'r')
output_file = open('Lab5/output1a.txt', 'w')

num_courses, num_prerequisites = map(int, input_file.readline().strip().split())

prerequisites_list = []
for _ in range(num_prerequisites):
    prerequisite_tuple = tuple(map(int, input_file.readline().strip().split()))
    prerequisites_list.append(prerequisite_tuple)

print(*find_course_order(num_courses, prerequisites_list), file=output_file)
