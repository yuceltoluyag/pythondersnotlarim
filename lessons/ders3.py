# Pythonda String Tanımlama

name = "Yücel"
surname = "Toluyağ"
age = 31

'''print('My name is ' + name + ' ' + surname +
      '' + ' and \nI am ' + age + ' years old')'''

# \n alt satıra geçirtir
# format() metodu ile f-string isminde
# iki farklı alternatifimiz mevcut.

'''print('My name is {} {}'.format(name, surname))
 # My name is Yücel Toluyağ
'''
# indis numaraları 0 dan başlar tersten -1 den başlar
# yücel 0 toluyağ 1 dir
# yücel -1 dersek l harfi bulunur

'''print('My name is {1} {0}'.format(name, surname))'''
# My name is Toluyağ Yücel

# format() metodu içindeki değişkenlere
# takma isim de verebiliriz.
'''print("my name is {s} {n} and I ' m {a} years old.".format(
    s=name, n=surname, a=age))'''

'''print("My name is {} {} and I'm {} years old.".format(
    name, surname, age))'''


# f-String ile String Formatlama
# f-string ile kolaylıkla string birleştirme
# işlemi yapabiliriz.
# Çünkü string ifadenin içinde süslü parantezler
# içinde değişkenleri yazabiliriz.

'''print(f"My name is {name} {surname} and I'm {age} years old.")
'''

# parçalama işlemleri string Slicing

greeting = "Fıstıkçı Şahap"
'''result = greeting[0]
print(result)  # Y harfi gelecektir'''
# dizilerin eleman sayısını len() metodu ile bulabiliriz.
result = len(greeting)
print(result)  # 14

# Dolayısıyla son elemanın indeks numarası
# toplam karakter sayısından 1 eksik olur.

result = greeting[len(greeting)-1]
print(result)  #

# Bir karakter dizisini başlangıç ve bitiş aralığında
#  istediğimiz şekilde bölebiliriz.3. indeksden başlayarak
# 7. indekse kadar olan karakterleri alıyoruz.
# Son indeks işin içine katılmıyor.
result = greeting[3:7]
print(result)  # tıkç

'''Burada ise başlangıç indeksi 3 ve bitiş indeksi belirtilmediğinden
dolayı en sona kadar alınır.
result = greeting[3:]
'''

'''Burada ise 0. indeksten 10. indekse kadar alınır ancak adım sayısı
2 olarak belirtildiğinden dolayı bir karakter alınır bir diğeri alınmaz.

** Adım sayısını soldan sağa doğru olduğuna dikkat ediniz.
** Negatif sayılar kullanırsanız sağdan sola doğru ilerler
:: kullanırsan her iki taraftanda işler yapar örneğin
::result[::-1]  result içinde ki değerleri tersten yazdırır
'''
result = greeting[::-1]  # pahaŞ ıçkıtsıF
print(result)  # Fsıç

# Bir ifadeyi değiştirmek

s = 'Hello Mars'
s = s[0:6] + 'm' + s[-3:]
print(s)  # Hello mars tam indisin üstüne gelmeli yoksa ekleme yapar

result = 'baba ' * 3
print(result)
