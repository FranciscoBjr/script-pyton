import random


def jogar():
    imprimeAbertura()
    palavraSecreta = carregaPalavraSecreta()

    letrasAcertadas = iniciaLetrasAcertadas(palavraSecreta)
    print(letrasAcertadas)

    enforcou = False
    acertou  = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pedeChute()

        if(chute in palavraSecreta):
            marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta)
        else:
            erros += 1
            desenhaForca(erros)

        enforcou = erros == 7
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)

    if(acertou):
        imprimeMVitoria()
    else:
        imprimeMDerrota(palavraSecreta)


def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimeMVitoria():
    print("Voce ganhou!")


def imprimeMDerrota(palavraSecreta):
    print("Voce perdeu!")
    print("a palavra secreta era {}".format(palavraSecreta))

def marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):
            letrasAcertadas[index] = letra
        index += 1

def pedeChute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def iniciaLetrasAcertadas(palavra):
    return ["_" for letra in palavra]

def imprimeAbertura():
    print("***************")
    print("bem vindo")
    print("***************")

def carregaPalavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta


if(__name__ == "__main__"):
    jogar()