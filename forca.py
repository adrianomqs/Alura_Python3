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


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    for posicao, letra in enumerate(palavra_secreta):
        if(chute == letra):
            letras_acertadas[posicao] = letra
            

def imprime_mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
    
def imprime_mensagem_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    

def desenha_forca(erros):
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

        # pede um chute para o usuário
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    # imprime o resultado do jogo
    if(acertou):
        imprime_mensagem_ganhou()
    else:
        imprime_mensagem_perdeu(palavra_secreta)
      
    # imprime o fim do jogo
    imprime_fim()
    

# inicia o jogo se o programa for executado diretamente
if __name__ == '__main__':
    start()
