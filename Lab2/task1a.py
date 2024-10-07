file1 = open("Lab2\input1.txt", "r")
file2 = open("Lab2\output1a.txt", "w")

def sum_pair(array, sum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if int(array[i]) + int(array[j]) == int(sum):
                return i+1, j+1
    return "Impossible"


line1 = file1.readline().strip().split(" ")
line2 = file1.readline().strip().split(" ")

result = sum_pair(line2, line1[1])
if result != "Impossible":
    file2.write(f"{result[0]} {result[1]}")
else:
     file2.write("Impossible")


file1.close()
file2.close()