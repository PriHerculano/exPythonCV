quilometros = float(input('Quantos Km o carro percorreu?:'))
print('(Se passar da meia noite, será cobrado como um dia inteiro)')
dias = int(input('Por quantos dias ele permaneceu alugado?:'))

v = 60 * dias
v2 = 0.15 * quilometros
x = v + v2

print(f'Como você percorreu {quilometros}km, você deverá pagar R${v2}\n'
      f'E por ele ter permanecido {dias} dias com você, o valor a ser cobrado pelos dias será R${v}\n'
      f'O total será de R${x:.2f}')