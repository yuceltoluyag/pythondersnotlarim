name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index >= 29.9) and (index <= 34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')
