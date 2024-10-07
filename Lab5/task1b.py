def breadth_first_search(num_courses, prerequisites):
    graph = {i: [] for i in range(1, num_courses + 1)}
    in_degree = [0] * (num_courses + 1)

    for course_a, course_b in prerequisites:
        graph[course_b].append(course_a)
        in_degree[course_a] += 1

    queue = []
    for course in range(1, num_courses + 1):
        if in_degree[course] == 0:
            queue.append(course)

    course_order = []
    while queue:
        course = queue.pop(0)
        course_order.append(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    if len(course_order) != num_courses:
        return "IMPOSSIBLE"

    return course_order[::-1]

input_file = open('Lab5/input1b.txt', 'r')
output_file = open('Lab5/output1b.txt', 'w')

num_courses, num_prerequisites = map(int, input_file.readline().strip().split())

prerequisites_list = []
for _ in range(num_prerequisites):
    prerequisite_tuple = tuple(map(int, input_file.readline().strip().split()))
    prerequisites_list.append(prerequisite_tuple)

print(*breadth_first_search(num_courses, prerequisites_list), file=output_file)
