# Python Set

"""
Pythonda set listeleri, list' e benzer ancak fark olarak
set içindeki elemanlar sıralanamaz (sort) ve indekslenemez yani
set elemanlarına 0,1 şeklinde indeks numaraları ile ulaşamayız.
Dolayısıyla set 'e eklediğimiz bir elemanın set listesi içinde hangi sırada
olacağını bilemeyiz. Ayrıca set içerisindeki elemanlar tekrarlayamaz,
her bir elemandan sadece bir tane olmalıdır, tekrarlayanlar silinir.
Pythonda set oluşturmak için süslü parantezler kullanırız.
"""

"""fruits = {"banana", "grape", "cherry"}
print(fruits)  # {"grape", "banana", "cherry"}"""

"""
Gördüğünüz gibi listeyi ekrana yazdırdığımızda liste elemanlarının yeri karışık geliyor.
Hatta uygulamayı her çalıştırdığınızda bu sıra değişecektir.
"""

"""
Set elemanlarına indeks numarası verilmediğinden dolayı indeks numarasına
göre elemanlara ulaşamayız.
Ancak bir döngü yardımıyla ulaşabiliriz.
"""

"""fruits = {"banana", "grape", "cherry"}
for fruit in fruits:
    print(fruit)"""

"""
Set Elemanlarını Güncelleme
Set listesi oluşturulduktan sonra her hangi bir elemanını
güncelleyemeyiz ancak liste üzerine yeni eleman ekleyebiliriz.

Set' e Yeni Eleman Ekleme
Set listesine tek bir eleman eklemek için
 add() metodunu, birden fazla eleman eklemek için ise
 update() metodunu kullanabiliriz.
"""

fruits = {"banana", "grape", "cherry"}
fruits.add("orange")  # {"grape", "banana","orange","cherry"}

"""
Set' e birden fazla eleman eklemek için ise;
"""

fruits = {"banana", "grape", "cherry"}
# {"orange", "banana", "mango", "grape", "cherry"}
fruits.update(["orange", "mango"])

# Set' den bir eleman silmek için remove() ya da discard() metodu kullanılabilir.

fruits = {"banana", "grape", "cherry"}
fruits.remove("grape")  # {"banana","cherry"}

# ** Eğer ki silmek istediğimiz eleman set içerisinde yok ise
# bu durumda geriye bir exception yani hata objesi döndürülür.

fruits = {"banana", "grape", "cherry"}
fruits.discard("grape")  # {"banana","cherry"}

# remove() metodundan farklı olarak discard() metodu ile
# silmek istediğimiz değer set içerisinde yoksa bir exception
# yani hata objesi döndürülmez.

"""
Bir eleman silmek için ayrıca pop() metodunuda kullanabiliriz
ancak set listeleri indekslenmediğinden dolayı pop() ile sildiğimiz bir elemanın
 hangisi olacağını bilemeyiz.
 Dolayısıyla uygulamayı her çalıştırdığımızda set listesinin son elemanı silinir
 ancak hangi eleman olacağını bilemeyiz.
"""
fruits = {"banana", "grape", "cherry"}
fruits.pop()  # {"banana","cherry"}

# clear() metodu ile set elemanlarının hepsini silebiliriz.

fruits = {"banana", "grape", "cherry"}
fruits.clear()  # { }

# del komutu ile set listesinin referansını sileriz dolayısıyla
# set ' e tekrar ulaşmak istediğimizde hata alırız.
fruits = ["banana", "grape", "cherry"]
del fruits
print(fruits)  # NameError: name 'fruits' is not defined


# Birden fazla set listesini birleştirmek için kullanabileceğimiz
# union() ve update() metotları vardır.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)  # {"a",1,3,2,"b","c"}

# union() metodu ile birleştirilen set' ler yeni bir set objesiyle geri döner. (set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)  # {"a",1,3,2,"b","c"}

# update() metodu ile bir set'i diğer set içerisine eklemiş oluyoruz
# yeni bir set objesi oluşturulmaz. (set1)
