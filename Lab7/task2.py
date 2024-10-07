def maximize_tasks(task_list, num_resources):
    task_list.sort(key=lambda x: x[1])

    selected_tasks = [[] for _ in range(num_resources)]

    for task in task_list:
        for resource in range(num_resources):
            start_time, end_time = task

            if not selected_tasks[resource] or start_time >= selected_tasks[resource][-1][1]:
                selected_tasks[resource].append((start_time, end_time))
                break

    return sum(len(task) for task in selected_tasks)


input_file = open('Lab7/input2.txt', 'r')
output_file = open('Lab7/output2.txt', 'w')

num_tasks, num_resources = map(int, input_file.readline().strip().split())
task_list = []
for _ in range(num_tasks):
    start_time, end_time = map(int, input_file.readline().strip().split())
    task_list.append((start_time, end_time))

max_completed_tasks = maximize_tasks(task_list, num_resources)
print(max_completed_tasks, file=output_file)
