p = float(input('Preço do produto: R$'))

d = p * 0.05
t = p - d

print(f'O desconto será de: {d:.2f}\n'
      f'Valor total: {t:.2f}')

#Outra mandeira de usar porcentagem

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5/100)
print(f'O produto irá de R${preço}, para R${novo}')