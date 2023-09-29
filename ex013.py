s = int(input('Digite o salário:'))

a = s * 0.15
t = s + a

print(f'O salário foi de {s} para {t}, com aumento de {a:.2f} reais')

 #Outra maneira

s = float(input('Qual é o salário do funcionário? R$'))
n = s + (s * 15/100)

print(f'O salário era de R${s} e foi para R${n}')