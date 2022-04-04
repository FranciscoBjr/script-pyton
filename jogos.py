import forca
import adivinhacao

print("***************")
print("Escolha o jogo")
print("***************")

print("jogo 1: forca, jogo 2: adivinahcao")

jogo = int(input("qual jogo?"))

if(jogo == 1):
    print("jogo da forca")
    forca.jogar()
elif(jogo == 2):
    print("jogo de adivinhacao")
    adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()