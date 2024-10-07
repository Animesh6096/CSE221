def select_tasks(tasks_list):
    tasks_list.sort(key=lambda x: x[1])
    selected_tasks = []
    previous_end = -1

    for task in tasks_list:
        start_time, end_time = task
        if start_time >= previous_end:
            selected_tasks.append(task)
            previous_end = end_time

    return selected_tasks

input_file = open('Lab7/input1.txt', 'r')
output_file = open('Lab7/output1.txt', 'w')

num_tasks = int(input_file.readline())
tasks_list = []
for _ in range(num_tasks):
    start_time, end_time = map(int, input_file.readline().strip().split())
    tasks_list.append((start_time, end_time))

selected_tasks = select_tasks(tasks_list)
print(len(selected_tasks), file=output_file)
for task in selected_tasks:
    print(task[0], task[1], file=output_file)
