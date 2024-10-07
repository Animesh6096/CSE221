file1 = open("Lab2\input4.txt", "r")
file2 = open("Lab2\output4.txt", "w")

def maxV(array, low, high):
    if low == high:
        return array[low]
    mid = (low + high) // 2
    left_max = maxV(array, low, mid)
    right_max = maxV(array, mid + 1, high)
    maximum = max(left_max, right_max)
    return maximum

line1 = int(file1.readline().strip())
line2 = list(map(int, file1.readline().strip().split(" ")))

maximum = maxV(line2, 0, line1 - 1)
file2.write(str(maximum))

file1.close()
file2.close()

"""The algorithm recursively divide the array into half until its length become 1.
So, the time complexity of the code is O(logn)."""