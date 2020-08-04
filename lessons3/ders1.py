# dosya işlemleri

# Dosya Açmak ve oluşturmak için open()
# Kulllanımı open(dosya_adi,dosya_erişme_modu)
# dosya erişme modu : hangi amaçla açtığımızı belirtlir

# Erişim modları

#  "w"  Write yazma modu,dosyayı belirtilen konumda oluşturur
result = open("newfile.txt", "w", encoding="utf8")
result.write("yücel")
result.close()  # işimiz bittikten sonra dosyayı  kapatalım
# Her çalıştığında tüm içeri siler yeniden oluşturur.

#  "a"  Append ekleme, dosya yoksa konumda oluşturur
result = open("newfile.txt", "a", encoding="utf8")
result.write("yücel\n")
result.close()
# Her çalıştığında veriyi silmez, o kadar veri ekler

#  "x" create oluşturma, dosya varsa  hata verir.

result = open("newfile.txt", "x", encoding="utf8")
result.write("yücel\n")
result.close()

# Çalıştığında dosyayı oluşturur,tekrar çalışırsa,dosya var olduğundan dolayı,hata verir file exist

#  "r"  okuma,varsayılan,dosya konumda yoksa hata verir

result = open("newfile.txt", "r", encoding="utf8")
# r yazmasak bile varsayılan read modunda açılır  open(
#   "newfile.txt", encoding="utf8"
result.write("yücel\n")
result.close()
print(result)

