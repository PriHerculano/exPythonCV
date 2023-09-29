import random
alunoa = str(input('Digite o nome do primeiro aluno:'))
alunob = str(input('Digite o nome do segundo aluno:'))
alunoc = str(input('Digite o nome do terceiro aluno:'))
alunod = str(input('Digite o nome do quarto aluno:'))
lista = [alunoa, alunob, alunoc, alunod]
esc = random.choice(lista)
print(f'nome sorteado:{esc}')