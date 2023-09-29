import random
alunoa = str(input('Digite o nome do primeiro aluno:'))
alunob = str(input('Digite o nome do segundo aluno:'))
alunoc = str(input('Digite o nome do terceiro aluno:'))
alunod = str(input('Digite o nome do quarto aluno:'))
lista = [alunoa, alunob, alunoc, alunod]
random.shuffle(lista)
print(f'A ordem será:{lista}')