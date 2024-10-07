file1 = open('Lab3/input2.txt', 'r')
file2 = open('Lab3/output2.txt', 'w')
max_value = float('-inf')

def calculate_max(a, b):
    return [max(a) + max(b, key=abs)**2]

def find_max_value(arr):
    global max_value
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = find_max_value(arr[:mid])
        a2 = find_max_value(arr[mid:])
        max_value = max(max_value, calculate_max(a1, a2)[0])
        return a1 + a2

n = int(file1.readline())
arr = list(map(int, file1.readline().strip().split()))

result = find_max_value(arr)
print(max_value, file=file2)

file1.close()
file2.close()