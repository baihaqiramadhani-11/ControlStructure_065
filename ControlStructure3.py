n = int(input("masukkan nilai fibonacci: "))
a = 0
b = 1

print("deret fibonacci:")

while a < n:
    print(a, end=' ')
    a, b = b, a + b