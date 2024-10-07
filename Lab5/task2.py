import heapq

def lexicographically_smallest_order(num_courses, prerequisites):
    course_graph = {i: [] for i in range(1, num_courses + 1)}
    in_degree = [0] * (num_courses + 1)

    for course_a, course_b in prerequisites:
        course_graph[course_a].append(course_b)
        in_degree[course_b] += 1

    heap = [i for i in range(1, num_courses + 1) if in_degree[i] == 0]
    heapq.heapify(heap)

    course_order = []
    while heap:
        current_course = heapq.heappop(heap)
        course_order.append(current_course)

        for next_course in course_graph[current_course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                heapq.heappush(heap, next_course)

    if len(course_order) == num_courses:
        return course_order
    else:
        return "IMPOSSIBLE"

input_file = open('Lab5/input2.txt', 'r')
output_file = open('Lab5/output2.txt', 'w')

num_courses, num_prerequisites = map(int, input_file.readline().strip().split())

prerequisites_list = []
for _ in range(num_prerequisites):
    prerequisite_tuple = tuple(map(int, input_file.readline().strip().split()))
    prerequisites_list.append(prerequisite_tuple)

print(*lexicographically_smallest_order(num_courses, prerequisites_list), file=output_file)
