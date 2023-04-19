import os

print('***Seja Bem-Vindo ao Sistema Escolar***')

opcao = 1
total_de_alunos = 0
alunos = 0

while(opcao == 1):

    n1 = float(input('Nota do Primeiro Bimestre: '))
    n2 = float(input('Nota do Segundo Bimestre: '))
    n3 = float(input('Nota do Terceiro Bimestre: '))
    n4 = float(input('Nota do Quarto Bimestre: '))

    media = (n1 + n2 + n3 + n4) / 4
    print('A média do aluno é:',media)
    if(media < 4 ):
        print("Ele está reprovado")

    elif(media > 4 and media <= 6):
        print('Ele está em dependencia')

    elif (media >= 6):
        print('Ele está aprovado')
    
    alunos = alunos + 1
    total_de_alunos = total_de_alunos + media

    opcao = int(input('Digite "0" para finalizar e digite "1" para continuar '))
    os.system('cls')

total_de_alunos = total_de_alunos / alunos 

print('Total de Alunos:',alunos)
print('Media Total:', total_de_alunos)

input()




    

