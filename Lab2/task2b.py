file1 = open("Lab2\input2.txt", "r")
file2 = open("Lab2\output2b.txt", "w")


def merge(a, b):
    merged = []
    i = 0
    j = 0

    for x in range(len(a) + len(b)):
        if i < len(a) and (j >= len(b) or a[i] < b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    return merged


line1 = int(file1.readline().strip())
line2 = list(map(int, file1.readline().strip().split()))

line3 = int(file1.readline().strip())
line4 = list(map(int, file1.readline().strip().split()))

merged1 = merge(line2, line4)
file2.write(str(merged1))

file1.close()
file2.close()