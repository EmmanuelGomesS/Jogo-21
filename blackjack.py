#Jogo BlackJack! 
import os,random,funcaoTeste#Importa biblioteca

#Variáveis
opjogo = 0
jogada = 0
totalj = 0
total1 = 0
total2 = 0

#Tela de inicio e menu de opções.
print('=*=*=*=*=*=*=*=*=*=*=*=0_0=*=*=*=*=*=*=*=*=*=*=*=')
print('            Bem Vindo ao BlackJack!\n')
print('Observação:\nO  jogo é feito para ser jogado por 2 jogadores.')
print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')    
print('\n---------MENU---------')
opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: \n')
while((opjogo!='1')and(opjogo!='2')and(opjogo!='3')):
    print('Opção invalida!\n')
    opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: ')
while(opjogo=='2'):
    funcaoTeste.instrucao(opjogo)
    opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: ')
    while((opjogo!='1')and(opjogo!='2')and(opjogo!='3')):
        print('Opção invalida!\n')
        opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: ')
#Vez do jogador número 1.
while(opjogo=='1'):
    
    for i in range(1,9):
        print(i,'ª partida')
        opjogo='S'
        os.system('clear')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nVocê tem que fazer 21 pontos ou chegar próximo\npara ganhar, porém sem estourar esse limite,\npodendo parar após cada jogada.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nJogador 1')
        totalj=0
        total1=0
        while(opjogo=='S'): #Laço que deixa as jogadas a critério do usuério.
            opjogo=input('Deseja fazer a jogada?[S]-Sim/[N]-Não \n')
            opjogo=str.upper(opjogo)
            while((opjogo!='S')and(opjogo!='N')):
                print('Opção inválida!')
                opjogo=input('Deseja fazer a jogada?[S]-Sim/[N]-Não \n')
                opjogo=str.upper(opjogo)
            if(opjogo=='N'):
                break
            #funcaoTeste.jogo()
            jogada=funcaoTeste.jogo()
            total1=(total1+jogada)
            if(total1>21):
                i=i+1
                print(i,'ª partida')
                print('Jogador 2 venceu.\n')
                break
            print('Você tirou {0} e até agora marcou {1} pontos.\n\n'.format(jogada,total1))
        if(total1>21):
            print('=*=*=*=*=*=*=*=*=*=*=*=0_0=*=*=*=*=*=*=*=*=*=*=*=')
            print('            Bem Vindo ao BlackJack!\n')
            print('Observação:\nO  jogo é feito para ser jogado por 2 jogadores.')
            print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')    
            print('\n---------MENU---------')
            opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: \n')
            while((opjogo!='1')and(opjogo!='2')and(opjogo!='3')):
                print('Opção invalida!\n')
                opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: ')
            while(opjogo=='2'):
                funcaoTeste.instrucao(opjogo)
                opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: ')
                while((opjogo!='1')and(opjogo!='2')and(opjogo!='3')):
                    print('Opção invalida!\n')
                    opjogo=input('Deseja iniciar o jogo?\n(1)Jogar\n(2)Instruções\n(3)Sair\n\nQual a sua escolha: ')
            break
        #Vez do jogador número 2.
        opjogo='S'
        os.system('clear')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nVocê tem que fazer 21 pontos ou chegar próximo\npara ganhar, porém sem estourar esse limite,\npodendo parar após cada jogada.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nJogador 2')
        print('Cuidado, pois o jogador 1 marcou {0} pontos\n'.format(total1))
        totalj=0
        total2 = 0
        while (opjogo=='S'):   #Laço que deixa as jogadas a critério do usuário.
            opjogo = input("Deseja fazer a jogada?[S]-Sim/[N]-Não \n")
            opjogo=str.upper(opjogo)
            while((opjogo!='S')and(opjogo!='N')):
                print('Opção inválida!')
                opjogo=input('Deseja fazer a jogada?[S]-Sim/[N]-Não \n')
                opjogo=str.upper(opjogo)
            if (opjogo=='N'):
                break
            #funcaoTeste.jogo()
            jogada=funcaoTeste.jogo()
            total2=(total2+jogada)
            if (total2 > 21):
                print('Jogador 1 venceu\n')
                break
            print('Você tirou {0} e até agora marcou {1} pontos.\n'.format(jogada,total2))
        print('O jogador 1 terminou com {0} pontos e o jogador 2 com {1} pontos, portanto...'.format(total1,total2))
        funcaoTeste.teste(total1,total2)
if(opjogo == '3'):
    exit()
