import random as rdn

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = rdn.randrange(1, 101)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina a dificuldade: "))
    print("")

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 8
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um número inteiro de 1 até 100: "))

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns!!! Você acertou!")
            print("")
            break
        else:
            if(maior):
                print("Você errou, seu chute foi maior que o número secreto")
                print("")
            elif(menor):
                print("Você errou, seu chute foi menor que o número secreto")
                print("")
        
            pontos = pontos - abs(numero_secreto - chute)

    print("Fim de jogo")
    print(f"O número secreto era {numero_secreto}")
    print(f"Sua pontuação foi de {pontos} pontos")

if(__name__ == "__main__"):
    jogar()