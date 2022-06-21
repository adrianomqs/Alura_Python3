import random


def start():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # inicialização das variáveis
    numero_secreto = random.randrange(1, 101)  # randomicos de 1 á 100
    pontuacao = 1000

    # Seleção de level
    level = int(input("Selecione o nivel de dificuldade [1= facil, 2= médio, 3= difícil]: "))
    if level == 1:
        max_tentativas = 30
        print(f'Você selecinou level fácil, você tem {max_tentativas} tentativas.')
    elif level == 2:
        max_tentativas = 15
        print(f'Você selecinou level médio, você tem {max_tentativas} tentativas.')
    elif level == 3:
        max_tentativas = 5
        print(f'Você selecinou level difícil, você tem {max_tentativas} tentativas.')

    print(f'Sua pontuação inicial é {pontuacao} pontos.')

    # Teste de chutes do usuario
    for rodada in range(1, max_tentativas + 1):
        # print('rodada ', rodada, ' de ', max_tentativas)
        # print('rodada {} de {}'.format(rodada, max_tentativas))
        print(f'rodada {rodada} de {max_tentativas}')

        chute_str = input("Digite o seu número: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns! Você acertou!")
            break
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
            elif menor:
                print("O seu chute foi menor do que o número secreto!")
            pontuacao -= level * (abs(chute - numero_secreto))
            print(f'Sua nova pontuação é: {pontuacao} pontos')
        print('')

    # fim de jogo
    print('')
    print('#################################')
    print(f'O numero secreto era: {numero_secreto}')
    if rodada < max_tentativas:
        print(f'Parabens! voce acertou usando {rodada} tentativas.')
    else:
        print(f'voce usou todas as {rodada} tentativas e não acertou.')
    print(f'Sua pontuação final é: {pontuacao} pontos')
    print('Fim do jogo!')
    print('#################################')


if __name__ == '__main__':
    start()
