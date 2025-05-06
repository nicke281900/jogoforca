def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

palavra_oculta = "camarão"
enforcou = False
acertou = False

while (not enforcou and not acertou):
    chute = input("Qual e a letra?")

index = 0 
for letra in palavra_oculta:
        if(chute == letra):
            print (f'incontrei a letra{letra}na posicao{index}')
            index = index + 1
    print ("jogando...")

print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
