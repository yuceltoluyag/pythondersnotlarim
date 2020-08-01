# Python Collections (Arrays)
"""
Pythonda 4 farklı liste tipi vardır.
Bunlar; List, Tuple, Set ve Dictionary veri tipleridir.

List, elemanları sıralanabilir, güncellenebilir ayrıca
her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Tuple, elemanları sıralanabilir ancak güncellenemez ve
her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Set, elemanları sıralanamaz ve indekslenemez ayrıca
her bir eleman liste içerisinde sadece bir tane olabilir.

Dictionary, key ve value şeklinde değer alırlar.
Aynı key bilgisiyle birden fazla eleman olamaz.
"""
# Pythonda Liste
"""
String veri tipindeki her bir karakter bir grubun yani
string karakter dizisinin bir elemanıdır ve her bir elemana indeks numarası ile ulaşabiliriz.

Gene aynı mantıkla list veri tipinde ise tek bir karakter yerine farklı veri tiplerindeki
bilgileri gruplayabiliyoruz. Karakter dizilerinde (string) olduğu gibi
her bir eleman indekslenebilir.
"""
# message ismindeki bir karakter dizisini
# (string) split() metodu ile bir listeye çevirebiliriz ve
# listenin 0.indeksindeki elemanı ekrana yazdırırsak karşımıza
# 'Hello' ifadesi gelir. Çünkü artık elimizde bir list mevcuttur.

"""message = 'Hello There. My name is Yücel Toluyağ'.split()
print(message)    # ['Hello', 'There.', 'My', 'name', 'is', 'Yücel', 'Toluyağ']
print(message[0])  # Hello"""

# liste metodları

# listenin sonuna append  metodu ile ekleme yapabiliriz liste.append("apple")
# Listenin belirtilen bir indeks'e eleman eklemek için insert() metodu kullanılır. liste.insert(2,"apple")
# Listeden bir eleman silmek için remove() metodunu kullanabiliriz. liste.remove("grape")
# Belirtilen bir indeks' deki elemanı silmek için pop() metodu kullanılır. Eğer indeks numarası belirtmezsek listenin son elemanı silinir.
# del() metodu ile her hangi bir indeks numarasındaki elemanı silebiliriz. del liste[2]
# Eğer ki del() metoduna indeks numarası vermezsek listeyi olduğu gibi siler. del liste
# Bir liste içeriğini başka bir listeye atamak için copy() metodunu kullanabiliriz. a = b.copy()
# Liste elemanlarını sıralamak için sort() metodu kullanılır.
# Tersten sıralamak istediğimizde ise reverse=True parametresini gönderebiliriz.
# Bir liste içerisindeki minimum ve maksimum değeri ister sayısal ister alfabetik olarak alabiliriz. min max
# Bir liste içerisindeki tekrarlayan elemanların sayısını almak için count() metodunu kullanırız.

# Python Dictionary

"""
Python collection veri tiplerinden olan dictionary yani sözlük veri yapısı
key ve value şeklinde verileri saklayabileceğimiz bir veri yapısıdır.
Dictionary veri yapısı Json veri yapısına oldukça benzerdir.

Dictionary liste elemanlarına key ve value değerlerine göre ulaşıp
elemanlar üzerinde güncelleme yapabiliriz.
(araç plakası ve il bilgisi gibi. {31: "Hatay"})
"""

"""ogrenci = {
    "numara": "120",
    "ad":   "Taylan",
    "soyad": "Otyer",
    "Meslek": "Laravel Dev"
}"""

# { "numara": "120", "ad": "Taylan", "soyad": "Otyer", "meslek": "Laravel Dev" }
"""print(ogrenci)"""


"""sehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]"""

"""Eğer ki
istanbul' un plaka kodunu almak istersek şu şekilde yapabiliriz

Örnek"""

"""print(plakalar[sehirler.index('istanbul')])  # 34"""


ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
