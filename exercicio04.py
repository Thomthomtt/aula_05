alunos=int(input("Quantos Aluno tem na sala: "))
soma=0
i=1
while i<=alunos:
    i+=1
    input_nota=float(input("Qual foi a nota do aluno?"))
    soma=soma+input_nota
media=soma/alunos
print(f"A média geral dos alunos é: {media}")