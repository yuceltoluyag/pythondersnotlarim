liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

 for x in liste:
     try:
         result = int(x)
         print(result)
     except ValueError:
         continue  #hata alan değerler es geçilir


 while True:
     sayi = input("sayı: ")
     if sayi == "q":
         break
     try:
         result = float(sayi)
         print("Girdiğiniz Sayı : ", result)
         break
     except ValueError:
         print("Geçersiz Sayı")
         continue

turkish = "şçğüöıİ"

parola = input("parola girin : ")

for i in parola:
    if i in turkish:
        raise TypeError('Parola Türkçe Karakter İçeremez')
    else:
        pass
    print("Geçerli Parola Girdiniz")
