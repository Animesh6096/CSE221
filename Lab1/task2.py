a = open("Lab1\input2.txt", "r")
b = open("Lab1\output2.txt", "w")

def bubbleSort(arr):
    flag = False
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True

length= int(a.readline())
arr= a.readline().split(" ")
bubbleSort(arr)
for n in range(length):
    b.write(f"{arr[n]} ")
a.close()
b.close()