a = open("Lab1\input1b.txt", "r")
b = open("Lab1\output1b.txt", "w")
x = int(a.readline())
for i in range(x):
    m = a.readline()
    n = m[10:-1].split(" ")
    if n[1] == "+":
        b.write(f"The Result of {m[10:-1]} is {int(n[0]) + int(n[2])}\n")
    elif n[1] == "-":
        b.write(f"The Result of {m[10:-1]} is {int(n[0]) - int(n[2])}\n")
    elif n[1] == "*":
        b.write(f"The Result of {m[10:-1]} is {int(n[0]) * int(n[2])}\n")
    elif n[1] == "/":
        b.write(f"The Result of {m[10:-1]} is {int(n[0]) / int(n[2])}\n")

a.close()
b.close()