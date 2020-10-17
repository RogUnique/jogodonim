            #JOGO DO NIM
import time
import random 


def começa():
    print("Olá bem vindo ao Jogo do Nim!")
    resposta = input("Você já conhece as regras?\nDigite '1' para sim e '2' para não:")
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
            break
        except ValueError:
            print("Parece que você esqueceu de digitar... Tente novamente.")
             
    if resposta == 1:
        print("Você decidiu jogar novamente")
        modos()
    elif resposta == 2:
        print("Okay! Vamos voltar ao menu inicial")
        começa()    

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
            break
        except ValueError:
            print("Ooops, parece que você não digitou nada! Tente novamente")
         
    if par_impar == 1:
        print(f"{jogador_um} escolheu 'impar',{jogador_dois} ficou com 'par'")
        escolheu_par = 0
    elif par_impar == 2:
        print(f"{jogador_um} escolheu 'par',{jogador_dois} ficou com 'impar'")
        escolheu_par = 1
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
    #op = opção
    while True:
        try:
            op  = int(input("Escolha:\n1 - para jogar uma partida isolada:\n2 - para jogar um campeonato:\nResposta: "))
            break
        except ValueError:
            print("Ooops, parece que você não digitou! Digite novamente por favor.")
 
    if op == 1:
        print("Você escolheu partida isolada!\n")
        if escolhido == 1:
            quem_começa()
        elif escolhido ==0:
            partida()
    elif op == 2:
        print("Você escolheu campeonato!\n") 
        if escolhido == 0:
            campeonato()
        elif escolhido == 1:
            campeonato_pvp()
    while op != 1 and op != 2:
        print("Valor invalido, por favor digite novamente")
        op  = int(input("1 - para jogar uma partida isolada:\n2 - para jogar um campeonato:\n"))         

#função que retorna o modo de jogo "1" para PVP e "2" para P vs PC e chama a função 'modo_jogo()'
def adversario():
    while True:
        try:
            adversario = int(input("Qual modo você deseja jogar? \n 1- Jogador Vs Jogador \n 2- Jogador Vs Maquina. \nModo: "))
            break
        except ValueError:
            print("Oooops! Você não digitou nada, por favor digite novamente.")
    while adversario != 1 and adversario != 2:
        print("Oooops! Você não digitou nada, por favor digite novamente.")
        adversario = int(input("Qual modo você deseja jogar? \n 1- Jogador Vs Jogador \n 2- Jogador Vs Maquina \n "))    

    if adversario  == 1:
        print("Você escolheu Jogador Vs Jogador!")       
        pvp = 1
        return pvp
    elif adversario  == 2:
        print("Você escolheu Jogador Vs Maquina. Boa Sorte!\n")
        pvp = 0
        return pvp 
            
#Função que explica as regras ao jogador se necessario e chama a função "adversario".
def regras(r):    
    while r != '1' and r != '2':
        r =input("Opa,opção invalida!\nDigite:1 para REGRAS OU 2-para JOGAR:")
    if r == '1' :
        print("Então vamos começar\n")         
    elif r == '2':
        print("Okay, irei te explicar como funciona!\n")
        print("O jogo do Nim é uma brincadeira muito antiga onde duas pessoas ou mais colocam determinado número de peças em uma mesa e escolhem quantas peças podem ser retiradas, vence quem retirar a ultima peça;\n")
   
def seleciona_dificuldade(dificuldade): #copiado
    if  dificuldade == 1:
        print("Você selecionou o modo fácil. Se divirta!")
        return dificuldade
    elif dificuldade == 2:
        print("Você selecionou o modo médio. Vamos lá!")  
        return dificuldade
    elif dificuldade == 3:
        print("Você selecionou o modo difícil. Boa sorte!") 
        return dificuldade
    elif dificuldade == 4:
        print("Você selecionou o modo Impossivel. Vish..!") 
    else:
        print("Opção invalida, por favor digite novamente.\n")    
def jogada_Escolhida_Pc(dificuldade):
    sorte = 0
    if dificuldade == 1 :
        sorte = 5 
    elif dificuldade == 2 :
        sorte = 3
    elif dificuldade == 3 :
        sorte = 1 
    num = random.randint(1,sorte) # A variavel sorte são as chances que o computador tem de fazer a jogada certa, quanto maior menor a chance
    return num
    
def jogada_aleatoria_pc(m):
    peças_removidas_pc = random.randint(1,m)
    return peças_removidas_pc

def jogada_pc(jogada,n,m): #Função com objetivo de chamar a jogada do PC e informar quantas peças foram retiradas
    jogada_correta = 2
    if jogada == jogada_correta :
        peças_removidas_pc = computador_escolhe_jogada(n,m)
    elif jogada != jogada_correta :
        peças_removidas_pc = jogada_aleatoria_pc(m)    
    n =  n- peças_removidas_pc
    time.sleep(1)
    print(f"O computador retirou {peças_removidas_pc} peça(s)")
    print(f"Agora resta(m){n} peça(s)\n")
    if n == 0:
        print("Fim do jogo! Computador venceu!\n")
        return int(1)
     
def jogada_usuario (n,m): #Função com objetivo de chamar a jogada do usuario e informar quantas peças foram retiradas
    peças_removidas_uso = usuario_escolhe_jogada(n,m)
    print(f"Você retirou {peças_removidas_uso} peça(s)")
    n =  n- peças_removidas_uso
    print(f"Agora resta(m){n} peça(s)\n")
    if n == 0:
        print("Fim do jogo! Você venceu!\n")
        return int(1)
     
def par_impar ():
    while True:
        try:
            par_impar = int(input("Para decidir quem começa iremos fazer um par ou ímpar.  \nEscolha:\n1 para impar & 2 para par.\nResposta: "))
             
        except ValueError:
            print("Ooops! Você digitou algo muito errado por favor tente novamente!")
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
    
def deu_par_impar(soma,par):
    venceu = 0
    if (soma) % 2 != 0:
        print("Deu ímpar!")
        if par == 0:
            print("Você venceu o par ou ímpar e irá começar o jogo! ")
            venceu = 1
          
        elif par == 1:
            print("Você perdeu o computador começa!")
             
    elif(soma) % 2 == 0:
        print("Deu par!")
        if par == 1:
            print("Você venceu, comece!")
            venceu = 1
        elif par == 0:
            print("Você perdeu, computador começa!")
    return venceu
        
def partida():
    print("Escolha a dificuldade: ")
    dificuldade = int(input("1 / Fácil \n2 / Médio \n3 / Díficil \n4 / Impossível\nDigite:"))
    dificuldade =  seleciona_dificuldade(dificuldade)
    while True:
        try:
            pecas_mesa  = int(input("Teremos quantas peças na mesa?\nResposta: "))
            break
        except ValueError:
            print("Ooops! Você não digitou algo algum, por favor tente novamente!")
            
    while pecas_mesa <= 0:
        pecas_mesa  = int(input("Valor invalido! Por favor digite novamente \n Quantas peças? "))        

    limite_peca = int(input("Limite de peças por jogada?"))

    while limite_peca <= 0:
        limite_peca = int(input("Valor invalido!Por favor digite novamente \n Limite de peças por jogada? "))
    
    if (par_impar()) == 1:
        escolheu_par = 1
    else:
        escolheu_par = 0


    num_jogador = int(input("Agora escolha um número: "))
    num_pc = random.randrange(1,101)
    time.sleep(2)
    print(f"O PC escolheu o número: {num_pc}.")
    
    soma = num_jogador + num_pc
    
    venceu = deu_par_impar(soma,escolheu_par) 
    if venceu == 1: #verifica se o jogador venceu
        
        peças_removidas_uso = usuario_escolhe_jogada(pecas_mesa,limite_peca)
        print(f"Você retirou {peças_removidas_uso} peça(s)")
        pecas_mesa =  pecas_mesa - peças_removidas_uso
        print(f"Agora resta(limite_peca){pecas_mesa} peça(s)\n")
        if pecas_mesa == 0:
            print("Fim do jogo! Você venceu!\n")
            return int(1)


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
        if pecas_mesa == 0:
            print("Fim do jogo! Computador venceu!\n")
            return int(1)

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
            if pecas_mesa == 0:
                print("Fim do jogo! Computador venceu!\n")
                return int(1) 
                
            a,b=0,1
                    
        elif b == 1:
            peças_removidas_uso = usuario_escolhe_jogada(pecas_mesa,limite_peca)
            print(f"Você retirou {peças_removidas_uso} peça(s)")
            pecas_mesa = pecas_mesa- peças_removidas_uso
            print(f"Agora resta(m){pecas_mesa} peça(s)\n")
            if  pecas_mesa == 0:
                print("Fim do jogo! Você venceu!\n")
                return int(1)
            a,b = 1,0
                 
def campeonato():
    pontosUser = 0
    pontosPc = 0
    for i  in range(1,4):
        print(f"**** Rodada {i} ****\n")
        if partida()==1:
            pontosPc +=1
        elif partida() == 2:
            pontosUser +=1
        i += i
    print(f"**** Final do campeonato! ****")
    print(f"Placar: Você {pontosUser} X {pontosPc} Computador ")
    return (pontosUser, pontosPc)

def campeonato_pvp():
    pontosP1 = 0
    pontosP2 = 0
   
    for i  in range(1,4):
        if i == 1:
            quem_começa()
        print(f"**** Rodada {i} ****\n")
       
        if partida_pvp() ==1:            
            pontosP1 +=1
        else:
            pontosP2 +=1
        i += i
    print(f"**** Final do campeonato! ****")
    print(f"Placar: {jogador_um} {pontosP1} X {pontosP2} {jogador_dois}  ")
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
            peças_a_remover_usu= int(input("Quantas peças você vai tirar?\n" ))
            break
        
        except:
            print("Ooops! Parece que você não digitou nada, tente novamente.")
             
    while  peças_a_remover_usu  > m or peças_a_remover_usu <=0 :
        print("Oops! Jogada inválida! Tente de novo.\n")
        peças_a_remover_usu = int(input("Quantas peças você vai tirar? \n"))
    return peças_a_remover_usu 

def jogador_um_joga(n,m):
    while True:
        try:
            peças_a_remover= int(input(f"Quantas peças você vai tirar {jogador_um}: \n" ))
            break
        except:
            print("Ooops! Parece que você não digitou nada, tente novamente.")
    while  peças_a_remover  > m or  peças_a_remover > n or peças_a_remover <=0 :
        print("Oops! Jogada inválida! Tente de novo.\n")
        peças_a_remover = int(input(f"Quantas peças você vai tirar {jogador_um}: \n"))
    return peças_a_remover
def jogador_dois_joga(n,m):
    while True:
        try:
            peças_a_remover= int(input(f"Quantas peças você vai tirar {jogador_dois}: \n" ))
            break
        except ValueError:
            print("Ooops! Parece que você não digitou nada, tente novamente.")
            
        
    while  peças_a_remover  > m or  peças_a_remover > n or peças_a_remover <=0 :
        print("Oops! Jogada inválida! Tente de novo.\n")
        peças_a_remover = int(input(f"Quantas peças você vai tirar {jogador_dois}: \n"))
    return peças_a_remover 

def partida_pvp():
    while True:
        try:
            n  = int(input("Peças na mesa: "))
            break
        except ValueError:
            print("Oops! Número invalido! Por favor digite novamente.")
            

    while n <= 0:
        n  = int(input("Valor invalido! Por favor digite novamente \n Quantas peças: "))        

    while True:
        try:
            m = int(input("Limite de peças por jogada: "))
            break
        except ValueError:
            print("Oops! Número invalido! Por favor digite novamente.")
            
    while m <= 0:
        m = int(input("Valor invalido!Por favor digite novamente \n Limite de peças por jogada: "))        
    
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


  



 

