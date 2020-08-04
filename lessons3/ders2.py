# with operotörü ile file.close kullanmamıza gerek yoktur
with open("newfile.txt", "r", encoding="utf8") as file:
    content = file.read()
    # cursorun nereye gideceğini belirtebiliriz
    file.seek(10)  # cursoru 10 . satıra gönderir
    print(content)
    # cursorun konumunu almak için tell fonksiyonu kullanır.
    print(file.tell())
