file1 = open('Lab3/input4.txt', 'r')
file2 = open('Lab3/output4.txt', 'w')

def partition_array(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def kth_small(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_idx = partition_array(arr, low, high)
    if pivot_idx == k - 1:
        return arr[pivot_idx]
    elif pivot_idx > k - 1:
        return kth_small(arr, low, pivot_idx - 1, k)
    else:
        return kth_small(arr, pivot_idx + 1, high, k)



n = int(file1.readline())
arr = list(map(int, file1.readline().strip().split()))
m = int(file1.readline())

for x in range(m):
    k = int(file1.readline())
    kth_smallest = kth_small(arr, 0, n - 1, k)
    print(kth_smallest, file=file2)
