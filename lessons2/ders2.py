"""
Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip
ehliyet alabilme durumunu kontrol eden python uygulamasını yapınız.

** Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
"""

username = input('Adınız :')
age = int(input('Yaşınız :'))
education = input('Eğitim Durumunuz :')

if (age >= 18):
    if(education == 'lise' or education == 'üniversite'):
        print(
            f'Merhaba {username} {age} yaşındasınız ve eğitim durumunuz {education},\n ehliyet alabilirsiniz')
    else:
        print(
            f'Merhaba {username} ehliyet alamazsınız, eğitim durumunuz {education} yetersiz')
else:
    print(f'Merhaba {username} ehliyet alamazsınız yaşınız {age} tutmuyor.')
