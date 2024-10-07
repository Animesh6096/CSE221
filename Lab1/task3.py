a = open("Lab1\input3.txt", "r")
b = open("Lab1\output3.txt", "w")

def ssort(obtained_mark, id, length):
    for i in range(length):
        min_1 = min_2 = i
        for j in range(i+1, length):
            if obtained_mark[min_1] < obtained_mark[j]:
                min_1 = min_2 = j
            elif obtained_mark[min_1] == obtained_mark[j]:
                if id[min_2] > id[j]:
                    min_2 = j

        obtained_mark[min_1], obtained_mark[i] = obtained_mark[i], obtained_mark[min_1]
        id[min_2], id[i] = id[i], id[min_2]


length = int(a.readline())
id = a.readline()[:-1].split()
obtained_mark = a.readline().split()
ssort(obtained_mark,id,length)
for i in range(length):
    b.write(f'ID: {id[i]} Mark: {obtained_mark[i]}\n')
a.close()
b.close()