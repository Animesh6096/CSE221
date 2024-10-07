file1 = open("Lab2\input1.txt", "r")
file2 = open("Lab2\output1b.txt", "w")


def sum_pair(arr, sum):
    
    dict = {}
    for i, j in enumerate(arr):
        x = int(sum) - (j)
        if x in dict:
            return (dict[x]+1, i+1)
        dict[j] = i

    return "Impossible"         
          
                      
     

line1 = file1.readline().strip().split(" ")
line2 = list(map(int, file1.readline().strip().split(" ")))

result = sum_pair(line2, line1[1])
if result != "Impossible":
    file2.write(f"{result[0]} {result[1]}")
else:
     file2.write("Impossible")


file1.close()
file2.close()