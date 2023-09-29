l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))

s = l * a
t = s/2

print(f'A parede tem a largura de {l}m\n'
      f'Altura de {a}m\n'
      f'Sua área total de {s}m\n'
      f'Precisando de {t:.2f}l de tinta')