def count_ways_to_climb_stairs(n):
    if n <= 1:
        return 1

    ways = [0] * (n + 1)
    ways[0] = ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

input_file = open('Lab8/input2.txt', 'r')
output_file = open('Lab8/output2.txt', 'w')

n = int(input_file.readline())
print(count_ways_to_climb_stairs(n), file=output_file)
