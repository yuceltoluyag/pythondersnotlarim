# Pythonda string metotları nelerdir ve nasıl kullanırız?

# Split metodu, karakter dizisinde belirtilen bir karaktere göre
# parçalama işlemi yapar.
# Karakter dizisini ','
# karakterinden parçalara ayırır ve bize bir liste gönderir.

message = 'Hello, There.'
message = message.split(',')   # ['Hello',' There']
print(message)  # ['Hello', ' There.']

# Split metoduna bir parametre göndermediğimizde ise,
#  boşluk karakterinden parçalama yapılır.
message = 'Hello, There.'
message = message.split()   # ['Hello,', 'There.']

# Upper Metodu
# Upper metodu, karakterleri büyük harfe çevirir.

message = 'Hello There.'
message = message.upper()  # HELLO THERE.

# Lower Metodu
# Lower metodu, karakterleri Küçük harfe çevirir.

message = 'HELLO THERE.'
message = message.lower()  # hello there.
print(message)

# ** title() metodu, karakter dizisindeki her kelimenin
# baş harfini büyük harfe çevirir.
# ** capitalize(), karakter dizisindeki
# sadece ilk kelimenin baş harfini büyük harfe çevirir.

# Strip Metodu
# Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler.

username = "     yücelbaba     "
x = username.strip()
print("my username is " + x)  # my username is yücelbaba

# Eğer strip() metodunun belirttiğimiz karakterleri
# Silmesini istersek bu karakteri parametre olarak göndermemiz gerekir.

username = ",,,,...!!yucel***"
x = username.strip(',.!*')
print("my username is " + x)  # my username is yucel

# Replace metodu karakter güncellemesi için kullanılır.Replace Metodu
message = 'Benim Adım Minel Bebek'
message = message.replace('Bebek', 'Toluyağ')  # Benim Adım Minel Toluyağ
print(message)

# replace() metotlarını ard arda kullanabiliriz.
message = 'Benim Adım Minel Bebek'
message = message.replace('Bebek', 'Toluyağ').replace(
    'Minel', 'Baba')  # Benim Adım Baba Toluyağ
print(message)

# Find Metodu
# Find metodu verilen string ifade içinde arama yapar
# Ve bulduğu ilk indeks numarasını döndürür.
# Eğer bulamazsa exception döndürür.

txt = "My name is Minel Toluyağ."
x = txt.find("name")
print(x)  # x = 3 3 numara olduğunu gösteriyor,bulamaz ise -1 gelecekti
# name string içerisinde 3.indeks numarasından itibaren başladığından dolayı
# 3 değeri yazdırılır.


# Index Metodu
# index metodu verilen string ifade içinde arama yapar ve bulduğu
# ilk indeks numarasını döndürür.
# Eğer bulamazsa find metodundan farklı olarak geriye - 1 değerini döndürür.

txt = "My name is Minel Toluyağ."
x = txt.find("Minel")
print(x)  # 11 döner

# ** Ayrıca index ve find metodu için bir arama kapsamı belirtebiliriz.
# index("aranılacak ifade", "başlangıç indeksi","bitiş indeksi")

txt = "My name is Minel Toluyağ."
x = txt.index("Toluyağ", 0, 24)
print(x)  # 17 döner

# uygulama

website = "https://www.yuceltoluyag.github.io/"
description = " Hi, my name is Yücel and I love playing games , building things and I probably drink too much tea "

# baş ve sondaki boşluk karakterleri silinir.
'''result = description.strip()
result1 = description.lstrip()    # baştaki boşluk karakterleri silinir.
result2 = description.rstrip()    # sondaki boşluk karakterleri silinir.
# baştan itibaren '/:ptths' karakteri silinir. result "www.yuceltoluyag.github.io" değerini alır.
result3 = website.lstrip('/:ptths')

print(result, result1, result2, result3)'''

#
'''
result = website.count('y')         # y karakteri sayılır.
result1 = website.count('www')       # www karakterleri sayılır.
# 0 ile 10. indeks arasında www ifadesi sayılır.
result2 = website.count('www', 0, 10)
print(result, result1, result2)  # 2 1 0'''


'''result = website.startswith('www')    # website www ile başlıyor mu ? False
result1 = website.startswith('http')   # website http ile başlıyor mu ? True
result2 = website.endswith('io/')      # website io ile bitiyor mu ? True
print(result, result1, result2)        # False True True'''


# website içerisinde 'io' ifadesini arar ve geriye 22 döner.
result = website.find('io')
# 0 ile 10 arasında io ifadesini bulamaz ve exception döndürür.
result1 = website.find('io', 0, 10)
# 0.indeksten itibaren bulduğu ilk Python için 0 değeri döner.
result2 = description.find('hi')
# Aramaya sağdan başlayacağından dolayı 2. Python' i 26. indekste bulur.
result3 = description.rfind('yucel')
# website içerisinde 'io' ifadesini arar ve geriye 22 döner.
result4 = website.index('io')
# website içerisinde 'io' ifadesini arar ve geriye 22 döner.
result5 = website.rindex('io')
# io bulunamadığından "ValueError: substring not found" hatası gelir.
result6 = website.rindex('io')
print(result, result1, result2, result3, result4,
      result5, result6)  # 32 -1 59 -1 32 32 32

# tüm karakterler alfabetik mi diye sorar ve False gelir.
result = description.isalpha()
result = 'Hello'.isalpha()  # tüm karakterler alfabetik olduğundan True gelir.
# tüm karakterler rakam mı diye sorar ve False gelir.
result = description.isdigit()
# tüm karakterler rakam mı diye sorar ve True gelir.
result = '123'.isdigit()

# **** Contents **** şeklinde toplam 50 karakter olur.
result = 'Contents'.center(50, '*')
# Contents ********* şeklinde toplam 50 karakter olur.
result = 'Contents'.ljust(50, '*')
# ********* Contents şeklinde toplam 50 karakter olur.
result = 'Contents'.rjust(50, '*')

# tüm boşluk karakterleri '-' ile değiştirilir.
result = description.replace(' ', '-')
# ilk 5 boşluk karakterleri '-' ile değiştirilir.
result = description.replace(' ', '-', 5)
result = description.replace(' ', '')     # tüm boşluk karakteri silinir.
