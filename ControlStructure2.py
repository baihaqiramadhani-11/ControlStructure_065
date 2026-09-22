a = float(input("masukkan angka pertama: "))
b = float(input("masukkan angka kedua: "))  
c = float(input("masukkan angka ketiga: "))

if a > b and a > c:
    terbesar = a
    print("angka terbesar adalah:", terbesar)
elif b > a and b > c:
    terbesar = b
    print("angka terbesar adalah:", terbesar)
elif c > a and c > b:
    terbesar = c21
    print("angka terbesar adalah:", terbesar)
else:
    print("tidak ada angka terbesar")