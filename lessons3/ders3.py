# dosya güncelleme
# + parametresi kullanılır

with open("newfile.txt", "r+", encoding="utf8") as file:
    print(file.read())
    file.seek(20)
    file.write("test\n")

with open("newfile.txt", "a", encoding="utf8") as file:
    file.write("Minel\n")


with open("newfile.txt", "r+", encoding="utf8") as file:
    print(file.read())
