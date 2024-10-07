file1 = open("Lab2\input3.txt", "r")
file2 = open("Lab2\output3.txt", "w")

def merge(a, b):
    merged = []
    i = 0
    j = 0
    
    for _ in range(len(a) + len(b)):
        if i < len(a) and (j >= len(b) or a[i] < b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    return merged

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

line1 = int(file1.readline().strip())
line2 = list(map(int, file1.readline().strip().split(" ")))

x = mergeSort(line2)
file2.write(str(x))

file1.close()
file2.close()