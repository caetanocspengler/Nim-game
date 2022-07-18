def saudacoes():
    print("#############################################")
    print("#          SEJA BEM-VINDO AO NIM!!!         #")
    print("#############################################")
    print()
    print("Jogo desenvolvido por: Caetano Spengler e Leandro Dias")
    print()
    print("Regras do jogo: ")
    print("1ª -  Escolha um número IMPAR maior que 5 e menos que 40")
    print("2ª - Cada jogador poderá retirar um valor entre 1 e 4 ")
    print("3ª - Perderá o jogo o jogador que retirar o último palito na fila")

def retira_palito():
    global valorFinal   
    valorFinal = fila_palitos
    if retirada >= 1 and retirada <= 4:
        valorFinal = fila_palitos - retirada

    else:
        print("Digite um valor válido!!")
        

def verifica_ganhador():
    global vencedor
    vencedor = ''
    if valorFinal <= 1 or valorFinal == 1:
        print("Jogador "+nome+" ganhou. ")
        vencedor = nome
        documenta_resultado()
        quit()
    
    elif valorFinal <= 1 or valorFinal == 1 :
         print("Jogador "+openente+" ganhou. ")
         vencedor = oponente
    else:
        retira_palito()

def documenta_resultado():
    arquivo = open("dados.txt", "a")
    arquivo.write("\nJogador 1: "+nome+"\nJogador 2: "+oponente+"\nVencedor: "+vencedor)
    arquivo.write("\n----------\n")

import random 

saudacoes()
while True: 
    jogador = input("Escolha contra quem você deseja jogar: \n (1)Colega \n (2)Computador(bot) \n Digite apenas o número: ")

    if jogador == '1':
            nome = input("Digite seu nome: ")
            oponente = input("Digite o nome do colega que irá jogar contra você: ")
            break

    elif jogador == '2':
        nome = input("Digite seu nome: ")
        openente = 'Friday.bot'
        break

    else:
        print("Digite um valor válido! ")

while True:
    fila_palitos = int(input("Digite um número IMPAR de palitos maior ou igual a CINCO(5) ou menor que QUARENTA(40): "))
    if fila_palitos % 2 == 0 or fila_palitos < 5 or fila_palitos > 40:
        print("Digite um valor válido! ")
        continue

    else:
        print("Quantidade de Palitos:"+fila_palitos*'|')
        break

while True:

    retirada = int(input("Jogador "+nome+" quantidade de palitos que deseja retirar entre em 1 e 4: "))

    if jogador == '1':
            retira_palito()
            fila_palitos = valorFinal
            print(valorFinal * '|')
            verifica_ganhador()
        
            retirada = int(input("Jogador "+oponente+" quantidade de palitos que deseja retirar entre em 1 e 4: "))
            retira_palito()
            fila_palitos = valorFinal
            print(valorFinal * '|')
            verifica_ganhador()

    else: 
        retira_palito()
        fila_palitos = valorFinal
        print(valorFinal * '|')
        verifica_ganhador()
        retirada = random.randint(1,4)
        print("O jogador "+openente+" está jogando e retirou "+str(retirada)+" da fila")
        retira_palito()
        fila_palitos = valorFinal
        print(valorFinal * '|')
        verifica_ganhador()
