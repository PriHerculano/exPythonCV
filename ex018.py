import math

num = float(input('Digite o ângulo escolhido:'))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan((math.radians(num)))
print(f'O seno de {num} é: {seno:.2f}\n'
      f'O cosseno de {num} é: {cosseno:.2f}\n'
      f'A tangente de {num} é: {tangente:.2f}')
