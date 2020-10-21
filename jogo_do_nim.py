#JOGO DO NIM
import time
import random 


def começa():
    
    print("\nOlá bem vindo ao Jogo do Nim!")
    resposta = input("\nVocê já conhece as regras?\nDigite '1' para sim e '2' para não: ")
    regras(resposta)
    modos()
    while (True):
        jogar_novamente()
    
    
def modos():
    global escolhido
    escolhido = adversario()
    modo_jogo(escolhido)
    
    
def jogar_novamente():
    while True:
        try:
            resposta = int(input("Digite 1 para: Jogar novamente\nDigite 2 para: voltar ao menu inicial. "))
            if resposta == 1:
                print("Você decidiu jogar novamente")
                modos()
            elif resposta == 2:
                print("Okay! Vamos voltar ao menu inicial")
                começa()
            while resposta != 1 and resposta != 2: 
                resposta = int(input("Ah não! :( Resposta invalida, tente novamente!\nDigite 1 para: Jogar novamente\nDigite 2 para: voltar ao menu inicial. "))
            break    
        except ValueError:
            print("Parece que você esqueceu de digitar... Tente novamente.")
             
    
   

def quem_começa():
    global jogador_um
    global jogador_dois
    global player1_começa
    jogador_um = input("Digite o nome do jogador 1: ")
    while jogador_um =="":
        print("O nome e algo importante para o jogo. Pense em um bem criativo!")
        jogador_um = input("Digite o nome do jogador 1: ")
    jogador_dois = input("Digite o nome do jogador 2: ")

    while jogador_dois =="":
        print("O nome e algo importante para o jogo. Pense em um bem criativo!")
        jogador_dois = input("Digite o nome do jogador 2: ")

    print("Vamos decidir quem começa com par ou impar.")
    while True:
        try:
            par_impar = int(input(f"{jogador_um} escolha '1' para impar ou  '2' para par: \n"))
            if par_impar == 1:
                print(f"{jogador_um} escolheu 'impar',{jogador_dois} ficou com 'par'")
                escolheu_par = 0
            elif par_impar == 2:
                print(f"{jogador_um} escolheu 'par',{jogador_dois} ficou com 'impar'")
                escolheu_par = 1
            while par_impar != 1 and par_impar !=2:
                par_impar = int(input(f"Algo não deu certo, {jogador_um}! Vamos tentar novamente!\nEscolha '1' para impar ou  '2' para par: \n"))
            break
        except ValueError:
            print("Ooops, parece que você não digitou nada! Tente novamente")
         
    
    while True:
        try:
            num_p1 = int(input(f"{jogador_um} digite um número, agora {jogador_dois} deve fechar os olhos. Não vale espiar!!\nNúmero: "))
            break
        except ValueError:
            print("Ooops, parece que você não digitou nada! Tente novamente")
             
    while True:   
        try:
            num_p2 = int(input(f"{jogador_dois} agora é sua vez de digitar um número!\nNúmero:"))
            break
        except ValueError:
            print("Ooops, parece que você não digitou nada! Tente novamente")
             
        
    resultado = int((num_p1 + num_p2)%2)
    if resultado != 0 :
        if escolheu_par == 0:
            print(f"{jogador_um} venceu!")
            player1_começa = 1
        elif escolheu_par == 1:
            print(f"{jogador_dois} venceu!")
            player1_começa = 0
    elif resultado == 0:
        if escolheu_par == 1:
            print(f"{jogador_um} venceu!")
            player1_começa = 1
        elif escolheu_par == 0:
            print(f"{jogador_dois} venceu!")
            player1_começa = 0
    if  escolhido == 1:
        partida_pvp()
    return player1_começa
#Função que inicia o modo indicado pelo jogador, '1' para partida isolado '2' para campeonato    
def modo_jogo(escolhido):
     
    while True:
        try:
            opção  = int(input("Escolha:\n1 - para jogar uma partida isolada:\n2 - para jogar um campeonato:\nResposta: "))
            if  opção == 1:
                print("Você escolheu partida isolada!\n")
                time.sleep(1)
                if escolhido == 1:
                   
                    quem_começa()
                elif escolhido ==0:
                    partida_atual = 1
                    partida(partida_atual)
            elif  opção == 2:
                print("Você escolheu campeonato!\n")
                time.sleep(1)
                if escolhido == 0:
                    campeonato()
                elif escolhido == 1:
                    campeonato_pvp()
            while  opção != 1 and  opção != 2:
                opção  = int(input("Vish algo de errado não está certo!\nEscolha:\n1 - para jogar uma partida isolada:\n2 - para jogar um campeonato:\nResposta: "))
            break
        except ValueError:
            print("Ooops, parece que você não digitou! Digite nov1amente por favor.")
 
    
    while  opção != 1 and opção != 2:
        print("Valor invalido, por favor digite novamente")
        opção  = int(input("1 - para jogar uma partida isolada:\n2 - para jogar um campeonato:\n"))         

#função que retorna o modo de jogo "1" para PVP e "2" para P vs PC e chama a função 'modo_jogo()'
def adversario():
    while True:
        try:
            adversario = int(input("Qual modo você deseja jogar? \n 1- Jogador Vs Jogador \n 2- Jogador Vs Maquina. \nModo: "))
            time.sleep(1)
            if adversario  == 1:
                print("Você escolheu Jogador Vs Jogador!")       
                pvp = 1
                return pvp
            elif adversario  == 2:
                print("Você escolheu Jogador Vs Maquina. Boa Sorte!\n")
                pvp = 0
                return pvp 
            while adversario !=1 and adversario !=2:
                 adversario = int(input("Opção invalida amigo!\nQual modo você deseja jogar? \n 1- Jogador Vs Jogador \n 2- Jogador Vs Maquina. \nModo: "))

            break
        except ValueError:
            print("Oooops! Você não digitou nada, por favor digite novamente.")
    while adversario != 1 and adversario != 2:
        print("Oooops! Você não digitou nada, por favor digite novamente.")
        adversario = int(input("Qual modo você deseja jogar? \n 1- Jogador Vs Jogador \n 2- Jogador Vs Maquina \n "))    

    
#Função que explica as regras ao jogador se necessario e chama a função "adversario".
def regras(r):    
    while r != '1' and r != '2':
        r =input("Opa,opção invalida!\nDigite:1 para REGRAS OU 2-para JOGAR:")
    if r == '1' :
        print("Então vamos começar!\n")
        time.sleep(1)
    elif r == '2':
        print("Okay, irei te explicar como funciona!\n")
        print("O jogo do Nim é uma brincadeira muito antiga onde duas pessoas ou mais colocam determinado número de peças em uma mesa e escolhem quantas peças podem ser retiradas, vence quem retirar a ultima peça;\n")
   
def seleciona_dificuldade(dificuldade):
    if dificuldade == 4:
        print("Você selecionou o modo Impossivel. Vish..!")
        return dificuldade
    elif  dificuldade == 1:
        print("Você selecionou o modo fácil. Se divirta!")
        return dificuldade
    elif dificuldade == 2:
        print("Você selecionou o modo médio. Vamos lá!")  
        return dificuldade
    elif dificuldade == 3:
        print("Você selecionou o modo difícil. Boa sorte!") 
        return dificuldade
    
    else:
        print("Opção invalida, por favor digite novamente.\n")    
def jogada_Escolhida_Pc(dificuldade):
    sorte = 0
    if dificuldade == 1 :
        sorte = 4 
    elif dificuldade == 2 :
        sorte = 3
    elif dificuldade == 3 :
        sorte = 2
    elif dificuldade == 4 :
        sorteio_jogada = 2
        return sorteio_jogada #No modo impossível o computador sempre escolhe a jogada certa

    sorteio_jogada = random.randint(0,sorte) # A variavel sorte são as chances que o computador tem de fazer a jogada certa, quanto maior menor a chance
    return sorteio_jogada
    
def jogada_aleatoria_pc(m):
    peças_removidas_pc = random.randint(1,m)
    return peças_removidas_pc

     
def par_impar ():
    while True:
        try:
            par_impar = int(input("\nPara decidir quem começa iremos fazer um par ou ímpar.  \nEscolha:\n1 para impar & 2 para par.\nResposta: "))
            while par_impar != 1 and par_impar !=2:
                print("Ooops! Você digitou algo errado por favor tente novamente!")
                par_impar = int(input("Para decidir quem começa iremos fazer um par ou ímpar.  \n Escolha: 1 para impar\n2 para par.\n Resposta: "))
            if par_impar == 1:
                print("Você escolheu impar!\n")
                escolheu_par = 0 #Variavel de referencia para saber se usuario escolheu par ou não. 0 = não
                return escolheu_par
            elif par_impar == 2:
                print("Você escolheu par!\n") 
                escolheu_par = 1               
                return escolheu_par 
        except ValueError:
            print("Ooops! Você digitou algo muito errado por favor tente novamente!")
        
        
    
def deu_par_impar(soma,par):
    venceu = 0
    if (soma) % 2 != 0:
        print("Deu ímpar!")
        if par == 0:
            print("\nVocê venceu, comece!\n")
            venceu = 1
          
        elif par == 1:
            print("Você perdeu o computador começa!")
             
    elif(soma) % 2 == 0:
        print("Deu par!")
        if par == 1:
            print("\nVocê venceu, comece!\n")
            venceu = 1
        elif par == 0:
            print("Você perdeu, computador começa!")
    return venceu
        
def partida(partida_atual):
    win = 0
    time.sleep(1)
     
    if partida_atual == 1:
        print("Escolha a dificuldade: ")
        time.sleep(1)
        global dificuldade
        dificuldade = int(input("1 / Fácil \n2 / Médio \n3 / Díficil \n4 / Impossível\nDigite:"))
        time.sleep(1)
        dificuldade =  seleciona_dificuldade(dificuldade)
    
    while True:
        try:
            pecas_mesa  = int(input("\nTeremos quantas peças na mesa?\nResposta: "))
            while pecas_mesa <=0:
                pecas_mesa  = int(input("Número de peças invailido, lembrando que deve ser > 0!\nQuantas peças?\nResposta:"))  
            break
        except ValueError:
            print("Ooops! Você não digitou algo algum, por favor tente novamente!")
            
    
              
    while True:
        try:
           limite_peca = int(input("Limite de peças por jogada?\nResposta: "))
           while limite_peca <= 0 and limite_peca <= pecas_mesa:
               limite_peca = int(input(f"Valor invalido!Dica: O limite de peças tem que ser menor que o número de peças na mesa({pecas_mesa}" 
               +"\nLimite de peças por jogada?\nResposta: "))
           break
        except ValueError:
            print("Ooops! Você não digitou algo algum, por favor tente novamente!")
    
    time.sleep(1)
    
    if (par_impar()) == 1:
        escolheu_par = 1
    else:
        escolheu_par = 0
    while True:
        try:
            num_jogador = int(input("Escolha um número de 0 a 10: "))
            while num_jogador >10 and num_jogador < 0:
                num_jogador = int(input("O número tem que estar entre 0 e 10 (incluindo)!\nEscolha outro número: "))
            break
        except ValueError:
            print("Vish, parece que você não digitou nada.\nVamos tentar de novo. ")

   
    num_pc = random.randint(0,10)
    time.sleep(1.5)
    print(f"\nO PC escolheu o número: {num_pc}.\n")
    
    soma = num_jogador + num_pc
    
    venceu = deu_par_impar(soma,escolheu_par) 
    if venceu == 1: #verifica se o jogador venceu par ou impar
        
        peças_removidas_uso = usuario_escolhe_jogada(pecas_mesa,limite_peca)
        print(f"Você retirou {peças_removidas_uso} peça(s)")
        pecas_mesa =  pecas_mesa - peças_removidas_uso
        print(f"Agora resta(m){pecas_mesa} peça(s)\n")
        time.sleep(1)
        if pecas_mesa == 0:
            win +=2
            print("***Você venceu!***\n")
            return (win)


        a,b = 1,0
    elif venceu == 0:
        jogada = jogada_Escolhida_Pc(dificuldade) 

        jogada_correta = 2
        if jogada == jogada_correta :
            peças_removidas_pc = computador_escolhe_jogada(pecas_mesa,limite_peca)
        elif jogada != jogada_correta :
            peças_removidas_pc = jogada_aleatoria_pc(limite_peca)
        pecas_mesa =  pecas_mesa - peças_removidas_pc
        time.sleep(1)
        print(f"O computador retirou {peças_removidas_pc} peça(s)")
        print(f"Agora resta(m){pecas_mesa} peça(s)\n")
        time.sleep(1)
        if pecas_mesa == 0:
            print("***O computador venceu!***")
            win +=1        
            return (win)

        a,b=0,1
        
      
    while pecas_mesa > 0:
        if a == 1:
            jogada = jogada_Escolhida_Pc(dificuldade)
            
            jogada_correta = 2
            if jogada == jogada_correta :
                peças_removidas_pc = computador_escolhe_jogada( pecas_mesa,limite_peca)
            elif jogada != jogada_correta :
                peças_removidas_pc = jogada_aleatoria_pc(limite_peca)    
            pecas_mesa =   pecas_mesa - peças_removidas_pc
            time.sleep(1)
            print(f"O computador retirou {peças_removidas_pc} peça(s)")
            print(f"Agora resta(m){pecas_mesa} peça(s)\n")
            time.sleep(1)
            if pecas_mesa == 0:
                win +=1
                print("***O computador venceu!***")
                return (win)
                
            a,b=0,1
                    
        elif b == 1:
            peças_removidas_uso = usuario_escolhe_jogada(pecas_mesa,limite_peca)
            print(f"Você retirou {peças_removidas_uso} peça(s)")
            pecas_mesa = pecas_mesa- peças_removidas_uso
            print(f"Agora resta(m){pecas_mesa} peça(s)\n")
            if  pecas_mesa == 0:
                print("***Você venceu!***\n")
                win +=2
                 
                return (win)
            a,b = 1,0
     
                 
def campeonato():
    pontosUser = 0
    pontosPc = 0
    global partida_atual
    partida_atual = 1
    for i  in range(1,4):
        print(f"**** Rodada {i} ****\n")
        vencedor = partida(partida_atual) 
        if vencedor == 1:
            pontosPc +=1
        elif vencedor == 2:
            pontosUser +=1
        
        i += i
        partida_atual +=1

    print(f"**** Final do campeonato! ****")
    trofeu = "\U0001F3C6"
    medalhaPrata ="\U0001F948"
    if pontosPc > pontosUser:
        emoji_pc = trofeu
        emoji_user = medalhaPrata
    elif pontosUser > pontosPc:
        emoji_user = trofeu
        emoji_pc = medalhaPrata

    
    print(f"Placar:{emoji_user} Você {pontosUser} X {pontosPc} Computador{emoji_pc}\n")
    
    return (pontosUser, pontosPc)

def campeonato_pvp():
    pontosP1 = 0
    pontosP2 = 0
   
    for i  in range(1,4):
        if i == 1:
            quem_começa()
        print(f"**** Rodada {i} ****\n")
       
        if partida_pvp() == 1:            
            pontosP1 +=1
        else:
            pontosP2 +=1
        i += i
    print(f"**** Final do campeonato! ****")
    if pontosP1 > pontosP2:
        emoji_P1 = "\U0001F3C6"
        emoji_P2 = "\U0001F948"
    elif pontosP2 > pontosP1:
        emoji_P1 = "\U0001F3C6"
        emoji_P2 = "\U0001F948"
    print(f"Placar:{emoji_P1} {jogador_um} {pontosP1} X {pontosP2} {jogador_dois} {emoji_P2}  ")
    return (pontosP1, pontosP2)

def computador_escolhe_jogada(n,m):
    time.sleep(1)
    peças_removidas_pc = 1 
    for k in range (1,m+1):
        peças_removidas_pc = k
        if ((n - peças_removidas_pc) % (m+1) == 0 ):
            return peças_removidas_pc
            
    if(n-peças_removidas_pc %(m+1) !=0):
        peças_removidas_pc = m 
    return peças_removidas_pc
   
def usuario_escolhe_jogada(n,m):
    while True:
        try:
            time.sleep(1)
            peças_a_remover_usu= int(input("Quantas peças você vai tirar?\nResposta: " ))
            time.sleep(1)
            while  peças_a_remover_usu  > m or  peças_a_remover_usu > n or peças_a_remover_usu <=0 :
                if peças_a_remover_usu > m:
                    print(f"Valor maior que o limite de peças por jogada: {m}.Tente de novo.")
                elif peças_a_remover_usu > n:
                    print(f"Só restam{n} peças na mesa.Tente novamente.")
                elif peças_a_remover_usu <= 0:
                    print(f"O valor mínimo para retirar de peças é 1.Tente novamente.")
                peças_a_remover_usu= int(input("Quantas peças você vai tirar?\nResposta: " ))
            break
        
            
        except:
            print("Ooops! Parece que você não digitou nada, tente novamente.")
             
    
    return peças_a_remover_usu 

def jogador_um_joga(n,m):
    while True:
        try:
            time.sleep(1)
            peças_a_remover = int(input(f"Quantas peças você vai tirar {jogador_um}: \n" ))
            time.sleep(1)
            while  peças_a_remover  > m or  peças_a_remover > n or peças_a_remover <=0 :
                if peças_a_remover > m:
                    print(f"Valor maior que o limite de peças por jogada: {m}.Tente de novo.")
                elif peças_a_remover > n:
                    print(f"Só restam{n} peças na mesa.Tente novamente.")
                elif peças_a_remover <= 0:
                    print(f"O valor mínimo para retirar de peças é 1.Tente novamente.")
                peças_a_remover = int(input(f"Quantas peças você vai tirar {jogador_um}: \n"))
            break
            
        except:
            print("Ooops! Parece que você não digitou nada, tente novamente.")
    
    return peças_a_remover
def jogador_dois_joga(n,m):
    while True:
        try:
            peças_a_remover= int(input(f"Quantas peças você vai tirar {jogador_dois}: \n" ))
            while  peças_a_remover  > m or  peças_a_remover > n or peças_a_remover <=0 :
                if peças_a_remover > m:
                    print(f"Valor maior que o limite de peças por jogada: {m}.Tente de novo.")
                elif peças_a_remover > n:
                    print(f"Só restam{n} peças na mesa.Tente novamente.")
                elif peças_a_remover <= 0:
                    print(f"O valor mínimo para retirar de peças é 1.Tente novamente.")
                peças_a_remover = int(input("Quantas peças você vai tirar?\nResposta: " ))
            break
        except ValueError:
            print("Ooops! Parece que você não digitou nada, tente novamente.")
    
            
    return peças_a_remover 

def partida_pvp():
    while True:
        try:
            n  = int(input("Quantas peças na mesa?\nResposta: "))
            while n <= 0:
                print("O número de peças deve ser maior que zero.Tente novamente.")
                n  = int(input("Quantas peças na mesa?\nResposta: "))
            break
        except ValueError:
            print("Oops! Número invalido! Por favor digite novamente.")
            
    while True:
        try:
            m = int(input("Limite de peças a serem retiradas por jogada: "))
            while m >= n:
                print(f"O limite de peças deve menor que o número de peças na mesa: {n}")
            time.sleep(1)
            break
        except ValueError:
            print("Oops! Número invalido! Por favor digite novamente.")     
    
    if player1_começa == 1:
            
            print(f"{jogador_um} começa!\n")
            peças_removidas  = jogador_um_joga(n,m)
            print(f"{jogador_um} retirou {peças_removidas} peça(s)")
            n =  n- peças_removidas
            print(f"Agora resta(m) {n} peça(s)\n")
            if n == 0:
                print(f"Fim do jogo! {jogador_um} venceu!\n")
                return int(1)
            a,b = 0,1     
    else:
            print(f"{jogador_dois} começa!\n")         
            peças_removidas = jogador_dois_joga(n,m)
            print(f"{jogador_dois} retirou {peças_removidas} peça(s)")
            n =  n- peças_removidas
            print(f"Agora resta(m){n}peça(s)\n")
            if n == 0:
                print(f"Fim do jogo! {jogador_dois} venceu!\n")
                return int(2)
            a,b=1,0
    while n > 0:
        if a == 1:        
            peças_removidas = jogador_um_joga(n,m)
            print(f"O {jogador_um} retirou {peças_removidas} peça(s)\n")
            n =  n- peças_removidas
            print(f"Agora resta(m) {n} peça(s)\n")
            if n == 0:
                print(f"Fim do jogo! {jogador_um} venceu!\n")
                return int(1)
            a,b = 0,1     
        elif b == 1:
            peças_removidas = jogador_dois_joga(n,m)
            print(f"{jogador_um} retirou: {peças_removidas} peça(s)\n")
            n = n - peças_removidas 
            print(f"Agora resta(m) {n} peça(s)\n")
            if n == 0:
                print(f"Fim do jogo! {jogador_dois} venceu!\n")
                return int(2)
            a,b=1,0   


    
começa()       
