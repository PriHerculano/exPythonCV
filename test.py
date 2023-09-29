n1 = int(input('digite um numero:'))
n2 = int(input('digite outro número:'))
c = n1 + n2
print(f'a soma de {n1} com {n2} é igual a {c}')

p = float(input('Qual o preço do produto? '))
x = int(input('De quanto será o desconto? '))
d = (p/100) * x
v = p-d
print(f'O produto que custava R${p:.2f}, com {x}% de desconto vai custar R${v:.2f}')