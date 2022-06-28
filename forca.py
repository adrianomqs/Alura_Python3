import random


def imprime_cabecalho():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")
    print("")
    
    
def imprime_fim():
    print("")
    print('#################################')
    print('Fim do jogo!')
    print('#################################')
    
    
def inicializa_letras_acertadas(palavras):
    letras_acertadas = ["_" for letra in palavras]
    return letras_acertadas


def carregar_palavra():
    palavras = []
    
    with open('palavras.txt') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta


def start():
    
    enforcou = False
    acertou = False
    erros = 0
    
    # imprime o cabeçalho do jogo
    imprime_cabecalho()
    
    # carrega a palavra secreta
    palavra_secreta = carregar_palavra()
    
    # inicializa o campo de letras acertadas
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    # loop do jogo
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")
      
    # imprime o fim do jogo
    imprime_fim()
    

# inicia o jogo se o programa for executado diretamente
if __name__ == '__main__':
    start()
