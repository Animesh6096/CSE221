a = open("Lab1\input1a.txt", "r")
b = open("Lab1\output1a.txt", "w")
x = int(a.readline())
for i in range(x):
    m = (int(a.readline()))
    if m % 2 == 0:
        b.write(f"{m} is an even Number\n")
    else:
        b.write(f"{m} is an Odd Number\n")
a.close()
b.close()
