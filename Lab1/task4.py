a = open("Lab1\input4.txt", "r")
b = open("Lab1\output4.txt", "w")

length = int(a.readline())
array = a.read().split("\n")

def bsort(arr, length):
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j].split(" ")[0] > arr[j+1].split(" ")[0]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
            elif arr[j].split(" ")[0] == arr[j+1].split(" ")[0]:
                if arr[j].split(" ")[-1] < arr[j+1].split(" ")[-1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

bsort(array, length)
for i in range(length):
    b.write(f"{array[i]}\n")
a.close()
b.close()