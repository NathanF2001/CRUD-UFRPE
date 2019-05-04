import Perguntas
#Importando a biblioteca Perguntas do próprio diretório  
def Novo(n):
#Definição de Novos dados, com o parametro "n".
    file,Dados_novos = opções(n,True)
    #Executado a função opções,como o parâmetro "n" e o valor booleano True. Os dados da função opções são guardados na variável "file" e "Dados_novos" .
    arquivo = open(file,"r+")
    #O file funciona como um nome do arquivo(Para entender qual é o arquivo vá para definição de opções). Assim abriu-se o arquivo com o modo "r"(leitura).
    for dados_arquivo in arquivo.readlines():
    #Utilizou o for para ler cada linha do arquivo. Este bloco serve para ver se os dados escritos já estão no sistema
        if dados_arquivo != '':
        #Condição para que caso a linha não tenha nada, não execute a operação. Pois se executasse, ocorreria IndexError.
            if file != "Dados do sistema/Dados da turma.txt":
            #O motivo dessa condição se dá do fato de que o arquivo "Turma" se comporta diferente dos demais arquivo, assim tendo que criar essa condição
                dados_arquivo = dados_arquivo.split("*")
                #Transformando a linha do arquivo em uma lista.
                dados_arquivo[1] = dados_arquivo[1].strip("\n")
                #Tirando a quebra linha que pode haver no segundo elemento no caso de "Aluno" e "Disciplina".
                if dados_arquivo[1] == Dados_novos[1]:
                #Condição para ver se o dados novo já estão no sistema
                    return print("Dados já cadastrado no sistema")
            else:
            #Condição do caso do arquivo "Turma".
                Dados_novos = "*".join(Dados_novos)
                #Os "Dados_novos" é retornado como uma lista, assim executa o join para transformá-lo em string.
                dados_arquivo = dados_arquivo.strip("\n")
                #Retira a quebra linha.
                if Dados_novos == dados_arquivo:
                #Compara o Dados novo com os dados que tem no arquivo e caso for Verdadeiro ele 
                    return print("Dados já cadastrado no sistema")
                    # retorna a mensagem, pois o dado ja está no sistema.
                else:
                #Executa o else
                    Dados_novos = Dados_novos.split("*")
                    #Transforma o Dados novos em lista, para não dá um erro absurdo.
                    continue
    Dados_novos = "*".join(Dados_novos)
    #Transforma Dados novos em string. Percebe-se que no caso de Turma eu transformei a string em lista e logo agora
    #transformei de novo em string. O motivo disso é sobre o erro absurdo que dá. Se nao transformasse Dados_novos em lista ele iria para essa linha como uma
    #string, assim iria da join numa string e daria uma string inadequada à situação.
    arquivo.write("%s\n"%Dados_novos)
    #Escreve os dados no arquivo
    arquivo.close()
    #Fecha o arquivo
    organizar(n)
    #Executa a função organiza(n), com o parâmetro n.
    return print("Dados adicionados ao sistema")


def retirar(Z):
#Definição de retirar(Z), com parâmetro Z
    try:    
        memória = []
        #Criou-se uma memória para guarda as linhas do arquivo
        y = consultar(Z)
        #Utilizou a função consultar(Z), com parâmetro Z.
        if y == 0 :
        #Isso é caso a função consultar retorne 0, que no caso significa que o arquivo está vazio.
            return print("Não é possível retirar dados.")
        nome_arquivo = opções(Z,False)
        #Executa a função opções, com parâmetro Z e False. Com o parâmetro False ele retorna apenas um valor
        arquivo = open(nome_arquivo,"r")
        #Abri o arquivo para leitura.
        for dados_linha in arquivo.readlines():
            #Passa-se por cada linha do arquivo e
            memória.append(dados_linha)
            #Adiciona-o à memória.
        arquivo.close()
        #Fecha o arquivo
        numero_dado_retirar = int(input("Em qual posição está o dado que deseja tirar? "))
        #Posição do dado a retirar. A lógica dele é que na consulta eu enumerei
        #o valor de cada linha do arquivo e imprimir. Sabendo o posição onde está
        #o arquivo posso manipula-lo sem precisar pedi alguma informação da própria lista.
        #So foi um método prático de capturar informação do arquivo.
        if numero_dado_retirar > len(memória) or numero_dado_retirar<= 0:
        #Condição a qual mostra se a variável numero_dado_retirar for maior que a memória ou menor
        #ou igual a 0 ele não execute, pois se executasse daria erro de posição errada ou IndexError.
            return print("Número inválido.")
        dado_retirar = memória[numero_dado_retirar-1].split("*")
        #Buscou o dado da memória a qual será retirado.
        confirmar = confirmação(Z,dado_retirar)
        #Executa a função confirmação, com os parâmetro Z e dado_retirar
        if confirmar == "S":
        #Caso o valor a retornar for "S"
            del memória[numero_dado_retirar-1]
            #Deleta o dado.
            arquivo = open(nome_arquivo,"w")
            #Abri o arquivo como "w", assim apagando tudo que está no arquivo e adicionando os novos dados que está na memória.
            for a in memória:
            #For para passa em cada posição de memória
                arquivo.write(a)
                #Escreve no arquivo
            arquivo.close()
            #Fecha o arquivo
            return print("Dados retirado do sistema.")
        elif confirmar == "N":
        #Caso o valor a retornar for "N"
            return print("Voltando ao sistema.")
    except ValueError:
        return print("Escreva um valor válido")
    

def consultar(Z):
#Definição consultar(Z), com parâmetro Z
    Memória = []
    #Criou-se uma memória para guarda as linhas do arquivo
    if Z == "P":
        #Parâmetro Z ter valor de "P".
        arquivo = open("Dados do sistema/Dados dos professores.txt","r")
        #Abri o arquivo Dados dos professores.
        for dados_linha in arquivo.readlines():
            #Passa a cada linha do arquivo
            dados_linha = dados_linha.strip("\n").split("*")
            #Na string da linha do arquivo é retirada a quebra de linha e logo após é transformado em Lista.
            Memória.append(dados_linha)
            #Adiciona a lista na memória
        arquivo.close()
        #Fecha o arquivo
        if Memória == []:
        #Condição caso a memória esteja vazia
            print("Essa categoria está vazia")
            return 0
            #Retornando "0" auxilia na função retirar(Z).
        print("{0:10} {1:13} {2:20} {3:60}".format("Número","CPF","Departamento","Nome"))
        #Posição de cada item na lista que será gerada.
        for posição,Dados in enumerate(Memória):
            print("{0:0>5}      {1:13} {2:20} {3:60}".format(str(posição+1),Dados[1],Dados[2],Dados[0]))
            #Os valores de cada item organizados para lista.
    elif Z == "D":
    #Parâmetro Z ter valor de "D".
        arquivo = open("Dados do sistema/Dados das disciplinas.txt","r")
        for dados_linha in arquivo.readlines():
            #Passa a cada linha do arquivo
            dados_linha = dados_linha.strip("\n").split("*")
            #Na string da linha do arquivo é retirada a quebra de linha e logo após é transformado em Lista.
            Memória.append(dados_linha)
            #Adiciona a lista na memória
        arquivo.close()
        #Fecha o arquivo
        if Memória == []:
            #Condição caso a memória esteja vazia
            print("Essa categoria está vazia")
            return 0
            #Retornando "0" auxilia na função retirar.
        print("{0:10} {1:13} {2:60}".format("Número","Código","Nome"))
        #Posição de cada item na lista que será gerada.
        for posição,Dados in enumerate(Memória):
            print("{0:0>5}      {1:13} {2:60}".format(str(posição+1),Dados[1],Dados[0]))
            #Os valores de cada item organizados para lista.
    elif Z == "A":
    #Parâmetro Z ter valor de "A".
        arquivo = open("Dados do sistema/Dados dos alunos.txt","r")
        for dados_linha in arquivo.readlines():
        #Passa a cada linha do arquivo
            dados_linha = dados_linha.strip("\n").split("*")
            #Na string da linha do arquivo é retirada a quebra de linha e logo após é transformado em Lista.
            Memória.append(dados_linha)
            #Adiciona a lista na memória
        arquivo.close()
        #Fecha o arquivo
        if Memória == []:
            #Condição caso a memória esteja vazia
            print("Essa categoria está vazia")
            return 0
        #Retornando "0" auxilia na função retirar.
        print("{0:10} {1:13} {2:60}".format("Número","CPF","Nome"))
        #Posição de cada item na lista que será gerada.
        for posição,Dados in enumerate(Memória):
            print("{0:0>5}      {1:13} {2:60}".format(str(posição+1),Dados[1],Dados[0]))
            #Os valores de cada item organizados para lista.
    elif Z == "T":
        #Parâmetro Z ter valor de "T".
        arquivo = open("Dados do sistema/Dados da turma.txt","r")
        for dados_linha in arquivo.readlines():
        #Passa a cada linha do arquivo
            dados_linha = dados_linha.strip("\n").split("*")
            #Na string da linha do arquivo é retirada a quebra de linha e logo após é transformado em Lista.
            Memória.append(dados_linha)
            #Adiciona a lista na memória
        arquivo.close()
        #Fecha o arquivo
        if Memória == []:
        #Condição caso a memória esteja vazia
            print("Essa categoria está vazia")
            return 0
            #Retornando "0" auxilia na função retirar.
        print("{0:10} {1:20} {2:10} {3:25} {4:20} {5:20}".format("Número","Código da turma","Período","Código da disciplina","CPF do professor","CPF do aluno"))
        #Posição de cada item na lista que será gerada.
        for posição,Dados in enumerate(Memória):
            print("{0:0>5}      {1:20} {2:10} {3:25} {4:20} {5:20}".format(str(posição+1),Dados[0],Dados[1],Dados[2],Dados[3],Dados[4]))
            #Os valores de cada item organizados para lista.
    return 1
    #Retornando "1" auxilia na função retirar(Z).
    

def alterar(Z):
#Definição alterar(Z), com parâmetro Z.
    try:
        Memória = []
        #Criou-se uma memória para guarda as linhas do arquivo.
        consultar(Z)
        #Executa a função consultar(Z).
        escolha = int(input("Escolha em qual número está o dado que queira alterar: "))
        #Posição do dado a retirar.
        file,Dados_Novos = opções(Z,True)
        #Executado a função opções,como o parâmetro "Z" e o valor booleano True. Os dados da função opções são guardados na variável "file" e "Dados_novos" .
        arquivo = open(file,"r") #Abri o arquivo
        for dados_arquivo in arquivo.readlines():
        #Passa-se por cada linha do arquivo .
            dados_arquivo = dados_arquivo.split("*")
            #Transforma a lista em string
            Memória.append(dados_arquivo)
            #Adiciona à memória
        if escolha > len(Memória) or escolha< 0:
        #Condição caso a variável "escolha" não seja adequada.
            return print("Número inválido.")
        arquivo.close()
        #fecha arquivo
        dado_alterar = Memória[escolha-1]
        #guarda a posição do dado a qual vai alterar.
        Y = "*".join(Dados_Novos)
        #Pegou a lista Dados_Novos e transformou em uma string guardada na variável Y.
        for dados in Memória:
        #Passa por toda memória
            dados = "*".join(dados)
            #Transforma a lista dados em string.
            dados = dados.strip("\n")
            #Retira a quebra linha
            if Y == dados:
            #Condição se os dois forem iguais não alterar
                return print("Os dados digitados já estão no sistema.")
        print("Escreva a sua alteração.(Escreva nada se não quiser alterar)")
        confirmar = confirmação(Z,dado_alterar)
        #Função confirmação, com parâmetros "Z" e dado_alterar.
        if confirmar == "S":
        #Condição se a variável confirmar for "S".
            for posição,b in enumerate(Memória[escolha-1]):
            #Enumerate foi utilizado pois so vai ser utilizado a posição da lista dentro da memória.
                if Dados_Novos[posição] != '':
                #Condição se o dado é diferente que string vazia.
                    Memória[escolha-1][posição] = Dados_Novos[posição]
                    #Alteração do dado
            arquivo = open(file,"w")
            #Abri o arquivo para escreve os dados da memória atualizado
            for dados in Memória:
            #Passa por casa elemento da memória
                dados = "*".join(dados)
                #Transforma em string
                arquivo.write(dados)
                #Escreve no arquivo
            arquivo.close()
            #fecha o arquivo
            return print("Dados trocados.")
        elif confirmar == "N":
        #Condição se a variável confirmar for "N"
            arquivo.close()
            return print("Retornando ao sistema.")
    except ValueError:
        return print("Escreva um valor válido")


def organizar(n):
#Definição organizar(n), com parâmetro n
    Organizar = []
    #Organizar funciona como a memória que será organizada
    file = opções(n,False)
    #Função opções e executada, com parâmetro n e False, assim so irá retornar um valor: o nome do arquivo.
    arquivo = open(file,"r")
    #Abri o arquivo
    for dados_arquivo in arquivo.readlines():
    #Passando por cada linha do arquivo
        dados_arquivo = dados_arquivo.strip("\n").split("*")
        #tira a quebra linha e transforma em lista
        Organizar.append(dados_arquivo)
        #Adiciona à memória Organizar
    arquivo.close()
    Organizar = sorted(Organizar)
    #Utiliza o sorted, que funciona como organizador de toda lista. Assim todas lista estará organizada.
    arquivo = open(file,"w")
    for dados in Organizar:
        dados = "*".join(dados)
        arquivo.write("%s\n"%dados)
    #Vou nem comenta de novo... Cansei.
    arquivo.close()
    return 
    

def opções(Z,alterar):
#Definição opções com os parâmetro Z e alterar
    if Z == "P":
    #Condição se Z tive valor de "P"
        x = "Dados do sistema/Dados dos professores.txt"
        #Guarda dados professores à variável x
        if alterar == True:
            y = Perguntas.Dados_professores()
            return (x,y)
    elif Z == "D":
    #Condição se Z tive valor de "D"
        x = "Dados do sistema/Dados das disciplinas.txt"
        #Guarda dados da disciplina à variável x
        if alterar == True:
            y = Perguntas.Dados_disciplinas()
            return (x,y)
    elif Z == "A":
    #Condição se Z tive valor de "A"
        x = "Dados do sistema/Dados dos alunos.txt"
        #Guarda dados dos alunos à variável x
        if alterar == True:
            y = Perguntas.Dados_alunos()
            return (x,y)
    elif Z == "T":
    #Condição se Z tive valor de "T"
        x = "Dados do sistema/Dados da turma.txt"
        #Guarda dados da turma à variável x
        if alterar == True:
            y = Perguntas.Dados_turma()
            return (x,y)
    #O alterar True executa a opções de perguntar novos dados e guarda-os na variável y
    return x

def confirmação(Z,L):
#Definição confirmação(Z,L), com parâmetros Z e L
    if Z == "P":
        conf = input("""Tem certeza que deseja executar esta ação nos seguintes dados:
        Nome do Professor: %s
        CPF do Professor: %s
        Departamento do Professor: %s
        Digite S para SIM/ N para NÃO
        """%(L[0],L[1],L[2]))
        #pergunta para confirma se o usuária queira executar a ação
        return conf
    elif Z == "D":
        conf = input("""Tem certeza que deseja executar esta ação nos seguintes dados:
        Nome da disciplina: %s
        Código da disciplina: %s
        Digite S para SIM/ N para NÃO
        """%(L[0],L[1]))
        #pergunta para confirma se o usuária queira executar a ação
        return conf
    elif Z == "A":
        conf = input("""Tem certeza que deseja executar esta ação nos seguintes dados:
        Nome do aluno: %s
        CPF do aluno: %s
        Digite S para SIM/ N para NÃO
        """%(L[0],L[1]))
        #pergunta para confirma se o usuária queira executar a ação
        return conf
    elif Z == "T":
        conf = input("""Tem certeza que deseja executar esta ação nos seguintes dados:
        Código da turma: %s
        Período: %s
        Código da disciplina: %s
        CPF do professor: %s
        CPF do aluno: %s
        Digite S para SIM/ N para NÃO
        """%(L[0],L[1],L[2],L[3],L[4]))
        #pergunta para confirma se o usuária queira executar a ação
        return conf



        
        
        
    
        
