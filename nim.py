def saudacoes():
    print("#############################################")
    print("#          SEJA BEM-VINDO AO NIM!!!         #")
    print("#############################################")
    print()
    print("Jogo desenvolvido por: Caetano Spengler e Leandro Dias")
    print()
    print("Regras do jogo: ")
    print("1ª - Escolha um número IMPAR maior que 5 e menos que 40")
    print("2ª - Cada jogador poderá retirar um valor entre 1 e 4 ")
    print("3ª - Perderá o jogo o jogador que retirar o último palito na fila")

def retirada_valida(retirada,fila_palitos,is_bot):
    if retirada >= 1 and retirada <= 4 and retirada <= fila_palitos:
        return True
    
    else:
        if not is_bot:
            print("Digite um valor válido")
        return False

def perdeu(fila_palitos):
    return fila_palitos == 0

def documenta_resultado(jogador1,jogador2,vencedor):
    arquivo = open("dados.txt", "a")
    arquivo.write("\nJogador 1: "+jogador1+"\nJogador 2: "+jogador2+"\nVencedor: "+vencedor)
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
        oponente = 'Friday.bot'
        break

    else:
        print("Digite um valor válido! ")

while True:
    fila_palitos = int(input("Digite um número IMPAR de palitos maior ou igual a CINCO(5) ou menor que QUARENTA(40): "))
    if fila_palitos % 2 == 0 or fila_palitos < 5 or fila_palitos > 40:
        print("Digite um valor válido! ")

    else:
        print("Quantidade de Palitos:"+fila_palitos*'|')
        break

while True:

    if jogador == '1':
        numero_valido = False
        while not numero_valido:
            retirada = int(input("Jogador "+nome+" quantidade de palitos que deseja retirar entre em 1 e 4: "))
            numero_valido = retirada_valida(retirada, fila_palitos,False)
            
        fila_palitos = fila_palitos - retirada
        print("Quantidade de Palitos:"+fila_palitos*'|')
        
        if perdeu(fila_palitos):
            ganhador = oponente
            break
        else:
            numero_valido = False
            while not numero_valido:
                retirada = int(input("Jogador "+oponente+" quantidade de palitos que deseja retirar entre em 1 e 4: "))
                numero_valido = retirada_valida(retirada, fila_palitos,False)
                
            fila_palitos = fila_palitos - retirada
            print("Quantidade de Palitos:"+fila_palitos*'|')
            if perdeu(fila_palitos):  
                ganhador = nome
                break

    else: 
        
        retirada = random.randint(1,4)

        numero_valido = False
        while not numero_valido:
            retirada = int(input("Jogador "+nome+" quantidade de palitos que deseja retirar entre em 1 e 4: "))
            numero_valido = retirada_valida(retirada, fila_palitos,False)
            
        fila_palitos = fila_palitos - retirada
        print("Quantidade de Palitos:"+fila_palitos*'|')
        
        if perdeu(fila_palitos):
            ganhador = oponente
            break

        else:
            numero_valido = False
            while not numero_valido:
                retirada = random.randint(1,4)
                numero_valido = retirada_valida(retirada, fila_palitos,True)

            print("O jogador "+oponente+" está jogando e retirou "+str(retirada)+" da fila")
            fila_palitos = fila_palitos - retirada
            print("Quantidade de Palitos:"+fila_palitos*'|')
            
            if perdeu(fila_palitos):
                ganhador = nome
                break

print(ganhador+" GANHOU!")
documenta_resultado(nome,oponente,ganhador)
