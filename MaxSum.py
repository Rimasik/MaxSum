N = int(input())
a = []

for i in range(6):
    a.append(int(input()))

Max1 = 0
Max2 = 0
MaxSum = 0

for i in range(6, N):
    x = int(input())
    if a[0] > Max1:
        Max1 = a[0]
    if x > Max2:
        Max2 = x
    if Max1 + Max2 > MaxSum:
        MaxSum = Max1 + Max2
    for j in range(6 - 1):
        a[j] = a[j + 1]

print(MaxSum)