# import random

# sayi = random.randint(1, 10)
# can = int(input('Kaç Hakkınız Olsun : '))
# hak = can
# sayac = 0

# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('tahmin: '))

#     if sayi == tahmin:
#         print(
#             f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1) }')
#         break
#     elif sayi > tahmin:
#         print('yukarı')
#     else:
#         print('aşağı')
#     if hak == 0:
#         print(f'hakkınız bitti. Tutulan sayı : {sayi}')


sayi = int(input('sayı: '))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('sayı asaldır.')
else:
    print('sayı asal değildir.')
