#cara menampilkan hasil

m = 10
print(m)
print("hasil m+m = ", m+m)
print("hasil m x m = ", m*m)

#menampilkan karakter
kar_1 = 'AKU KUAT'
kar_2 = 'AKU HEBAT'
kar_3 = 'HARUS SEMANGATTTT'
print(kar_1+' '+kar_2+' '+kar_3)
print(kar_1[2:10])
karakter = 'AKU KUAT AKU HEBAT AKU SEMANGATTTT'
print(karakter.split())

from math import sqrt
from math import pi

#operasi hitungan sederhana
a = 25
b = 25
c = 2.5
d = 25/5

print(a+b)
print("bentuk bilangan integer = ", int(b))
print("bentuk bilangan float = ", float(a))
print("perkalian c x d = ", c*d)
print("-----------------------")
print("contoh soal")
print("Tentukan kecepatan (v) dengan usaha (w) = 35; jarak (s) = 25; waktu(t) = 5)")
w = 35
s = 25
t = 5

#v = s/t
kecepatan = s/t
print(kecepatan, "m/s")

print("-----------------------")
print("soal 1")
print("Tentukan energi dalam J dari m = 9.31x10^-31; c = 3*10^8")
m = 9.31*10**-31
c = 3*10**8

#energi
E = m * c**2
print(E)

print("-----------------------")
print("soal 2")
print("Tentukan periode dalam s (l = 20 m ; g = 9.8 m/s^2)")
l = 20
g = 9.8

#periode = 2 x pi x sqrt (l/g)
periode = 2 * pi * sqrt (l/g)
print (periode)


