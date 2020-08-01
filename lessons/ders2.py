# veri tip dönüşümleri
'''
sayi1 = input('first number: ')
sayi2 = input('second number: ')

ptotal = int(sayi1) + int(sayi2)
print(ptotal)
'''
# inputtan gelen değerler stringtir.
# İnt e çevirilmezse toplama işlemi yerine birleştirme işlemi yapar

# çeviriler & Veri Dönüşümleri
'''
x = 10
y = 20.5
isOnline = True

#  int veri türünden float veri türüne,

x = float(x)     # int to float
print(x)         # 10.0
print(type(x))   # <class 'float'>

#  float veri türünden int veri türüne,

y = int(y)     # float to int
print(y)       # 20
print(type(y))  # <class 'int'>

#  int veri türünden string veri türüne,

result = str(x) + str(y)   # int to string
print(result)              # 1020.5
print(type(result))        # <class 'str'>

#  bool veri türünden string veri türüne,

isOnline = str(isOnline)   # bool to str
print(isOnline)            # True (string bir kelime)
print(type(isOnline))      # <class 'str'>

# bool veri türünden int veri türüne,

isOnline = int(isOnline)   # bool to int
print(isOnline)            # 1 (True için 1, False için 0)
print(type(isOnline))      # <class 'int'>
'''

pi = 3.14
r = float(input("yarı çap: "))

alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

print("alan: " + str(alan) + " çevre: " + str(cevre))

# Kullanıcıdan aldığımız değerler bize string veri tipinde gelir.
# Gelen ondalıklı değerleri float() metodu ile float değerlere dönüştürmemiz lazım.
# Hesaplama işlemi bittikten sonra da ekranda sonucu string şeklinde göstermeliyiz
# Çünkü string birleştirme işlemine sadece string değerler girer.
