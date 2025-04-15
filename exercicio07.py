resp="s"
while resp=="s":
    nota1 = float(input("Digite a primeira nota do aluno: "))
    while nota1<0 or nota1>10:
        nota1 = float(input("Nota inválida, insira novamente: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    while nota2>10 or nota2<0:
        nota2 = float(input("Nota inválida, insira novamente: "))
    media=(nota1+nota2)/2
    print(media)
    resp=input("Deseja Refazer o cálculo? s/n ")
