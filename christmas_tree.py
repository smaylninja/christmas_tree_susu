
f = open('tree_1.txt', 'r')
f2 = open('tree_2.txt', 'r')
x = f.readlines()
y = f2.readlines()
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0

f.close()
f2.close()

for i in range(0, 10):
    for j in range(len(x[i])):
        if x[i][j] != y[i][j]:
            x1 += 1
for i in range(10, 21):
    for j in range(len(x[i])):
        if x[i][j] != y[i][j]:
            x2 += 1
for i in range(21, 33):
    for j in range(len(x[i])):
        if x[i][j] != y[i][j]:
            x3 += 1
for i in range(33, 46):
    for j in range(len(x[i])):
        if x[i][j] != y[i][j]:
            x4 += 1
for i in range(46, 60):
    for j in range(len(x[i])):
        if x[i][j] != y[i][j]:
            x5 += 1

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)

print(x1**2 + x2**4 * x5**3 + x3**3 * x4**5)
print(x[59][7])