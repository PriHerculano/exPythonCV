# Fazendo um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

c = input('digite algo: ')
print(f'Tem número? {c.isnumeric()}')
print(f'Tem letra? {c.isalpha()}')
print(f'É alfanumérico? {c.isalnum()}')
print(f'Está em maiúsculo? {c.isupper()}')
print(f'Está em minúsculo? {c.islower()}')
