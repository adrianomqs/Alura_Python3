import adivinhacao
import forca


def start():
    print("")
    print("*********************************")
    print("Bem vindo á Central de jogos!")
    print("*********************************")

    while True:
        jogo = int(input('Escolha seu jogo. [1] Adivinhação ou [2] Forca?: '))

        if jogo == 1:
            # Adivinhação
            adivinhacao.start()
        elif jogo == 2:
            # Forca
            forca.start()
        else:
            # Não encontrado
            print( 'Jogo não encontrado!')


if __name__ == '__main__':
    start()