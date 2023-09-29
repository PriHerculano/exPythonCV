from math import pow, sqrt

num = float(input('Digite a medida de um lado:'))
num2 = float(input('Digite a medida do outro lado:'))
x = (pow(num, 2) + pow(num2, 2))
res = sqrt(x)

print(f'O resultado da hipotenusa será:{res:.2f}')

 #OUTRA MANEIRA DE FAZER
import math #ou math import hypot
num = float(input('Digite a medida de um lado:'))
num2 = float(input('Digite a medida do outro lado:'))
hi = math.hypot(num, num2)

print(f'O resultado da hipotenusa será:{hi:.2f}')
