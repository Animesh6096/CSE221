file1 = open("Lab3/input1.txt", "r")
file2 = open("Lab3/output1.txt", 'w')

def merge_count(left, right):
    pair_count = 0
    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            pair_count += len(left) - i
            j += 1

    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return pair_count, merged_list

def pair_count(height):
    if len(height) <= 1:
        return 0, height

    mid = len(height) // 2
    left_count, left_list = pair_count(height[:mid])
    right_count, right_list = pair_count(height[mid:])
    merged_count, merged_list = merge_count(left_list, right_list)
    return left_count + right_count + merged_count, merged_list


N = int(file1.readline().strip())
heights = list(map(int, file1.readline().strip().split()))

pair_count, sorted_permutations = pair_count(heights)

file2.write(str(pair_count))

file1.close()
file2.close()
