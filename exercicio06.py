i=0
senha=0
pin=123
while senha!=pin and i<3:
    senha = int(input("Digite sua senha: "))
    i+=1
    if senha==pin:
        print("Sua senha está correta!")
    if i==3 and senha!=pin:
        print(f"Seu acesso está bloqueado!")
