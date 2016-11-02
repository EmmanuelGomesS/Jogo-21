import random  #importa a biblioteca random
def teste(total1,total2):
    if (total1 == 21):
         print('O jogador 1 ganhou, fazendo os gloriosos 21 pontos =D...\n')
    elif (total2 == 21):
         print('O jogador 2 ganhou, fazendo os gloriosos 21 pontos =D...\n')
    elif (total1 <= 21 and total2 > 21):
         print('O jogador 2 tem um número maior de pontos do que é permitido...jogador 1 ganha.\n')
    elif (total1 > 21 and total2 <= 21):
         print('O jogador 1 tem um número maior de pontos do que é permitido...jogador 2 ganha.\n')
    elif (total1 == total2):
         print('Houve um empate...')
    elif (total2 > 21 and total1 < 21):
         print('O jogador 1 venceu por estar mais perto de 21.\n')
    elif (total1 > 21 and total2 < 21):
         print('O jogador 2 venceu por estar mais perto de 21.\n')
    elif (total1 < 21 and total1 > total2):
         print('O jogador 1 venceu por estar mais perto de 21.\n')
    elif (total2 < 21 and total1 < total2):
         print('O jogador 2 venceu por estar mais perto de 21.\n')


        
def instrucao (opjogo):
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINSTRUÇÔES:\nSão permitidos 2 jogadores.\nO jogo tem a duração de 7 partidas.\nOs jogadores terão através da soma dos valores das cartas pedidas por eles ao computadaor que atingir ou se aproximar da soma de 21 pontos.\nO jogador que ficar mais perto de 21 pontos será o vencedor da partida.\nSe o JOGADOR 1 ultrapassar a soma de 21 ponto, o JOGADOR 2 vence o jogo e vice-versa.\nNo caso de empate de 21 pontos para ambos jogadores o 1ºJogador vencerá a partida.\n\nCARTAS:\nÁS-OURO; ÁS-ESPADA; ÁS-COPA e ÁS-PAU;\n2-OURO; 2-ESPADA; 2-COPA e 2-PAU;\n3-OURO; 3-ESPADA; 3-COPA e 3-PAU;\n4-OURO; 4-ESPADA; 4-COPA e 4-PAU;\n5-OURO; 5-ESPADA; 5-COPA e 5-PAU;\n6-OURO; 6-ESPADA; 6-COPA e 6-PAU;\n7-OURO; 7-ESPADA; 7-COPA e 7-PAU;\n8-OURO; 8-ESPADA; 8-COPA e 8-PAU;\n9-OURO; 9-ESPADA; 9-COPA e 9-PAU;\n10-OURO; 10-ESPADA; 10-COPA e 10-PAU;\n(j)VALETE-OURO; (j)VALETE-ESPADA; (j)VALETE-COPA e (j)VALETE-PAU;\n(Q)DAMA-OURO; (Q)DAMA-ESPADA; (Q)DAMA-COPA e (Q)DAMA-PAU;\n(K)REI-OURO; (K)REI-ESPADA; (K)REI-COPA e (K)REI-PAU;\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


def jogo():#Definição da função
    Baralho=['ÁS-OURO','ÁS-ESPADA','ÁS-COPA','ÁS-PAU','2-OURO','2-ESPADA','2-COPA','2-PAU','3-OURO','3-ESPADA','3-COPA','3-PAU','4-OURO','4-ESPADA','4-COPA','4-PAU','5-OURO','5-ESPADA','5-COPA','5-PAU','6-OURO','6-ESPADA','6-COPA','6-PAU','7-OURO','7-ESPADA','7-COPA','7-PAU','8-OURO','8-ESPADA','8-COPA','8-PAU','9-OURO','9-ESPADA','9-COPA','9-PAU','10-OURO','10-ESPADA','10-COPA','10-PAU','(j)VALETE-OURO','(j)VALETE-ESPADA','(j)VALETE-COPA','(j)VALETE-PAU','(Q)DAMA-OURO','(Q)DAMA-ESPADA','(Q)DAMA-COPA','(Q)DAMA-PAU','(K)REI-OURO','(K)REI-ESPADA','(K)REI-COPA','(K)REI-PAU']#Lista baralho
    x=len(Baralho)
    sorteado=random.randint(0,x-1)
    y=Baralho[sorteado]
    print('Carta sorteada: ',y)#Imprime carta sorteada        
    #Testa a variável e retorna valor a ser somado no programa principal
    if((y=='ÁS-OURO')or(y=='ÁS-ESPADA')or(y=='ÁS-COPA')or(y=='ÁS-PAU')):
        return 1
    elif((y=='2-OURO')or(y=='2-ESPADA')or(y=='2-COPA')or(y=='2-PAU')):
        return 2
    elif((y=='3-OURO')or(y=='3-ESPADA')or(y=='3-COPA')or(y=='3-PAU')):
        return 3
    elif((y=='4-OURO')or(y=='4-ESPADA')or(y=='4-COPA')or(y=='4-PAU')):
        return 4
    elif((y=='5-OURO')or(y=='5-ESPADA')or(y=='5-COPA')or(y=='5-PAU')):
        return 5
    elif((y=='6-OURO')or(y=='6-ESPADA')or(y=='6-COPA')or(y=='6-PAU')):
        return 6
    elif((y=='7-OURO')or(y=='7-ESPADA')or(y=='7-COPA')or(y=='7-PAU')):
        return 7
    elif((y=='8-OURO')or(y=='8-ESPADA')or(y=='8-COPA')or(y=='8-PAU')):
        return 8
    elif((y=='9-OURO')or(y=='9-ESPADA')or(y=='9-COPA')or(y=='9-PAU')):
        return 9
    elif((y=='10-OURO')or(y=='10-ESPADA')or(y=='10-COPA')or(y=='10-PAU')or(y=='(j)VALETE-OURO')or(y=='(j)VALETE-ESPADA')or(y=='(j)VALETE-COPA')or(y=='(j)VALETE-PAU')or(y=='(Q)DAMA-OURO')or(y=='(Q)DAMA-ESPADA')or(y=='(Q)DAMA-COPA')or(y=='(Q)DAMA-PAU')or(y=='(K)REI-OURO')or(y=='(K)REI-ESPADA')or(y=='(K)REI-COPA')or(y=='(K)REI-PAU')):
        return 10

