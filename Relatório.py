import os
def relatório(Z):   # Definição relatório com o parâmetro Z
    #Pegará o arquivo Dados da turma para que faça a comparação com os dados dos outros arquivos.
    #O "Z" funciona como uma escolha, se for falso ele vai pegar o arquivo Dados dos professores, portanto será utilizada para gerar relatório dos professores.
    #Se "Z" for verdadeiro foi colocado para executar a ação de Dados dos alunos, portanto será utilizada para gerar relatório dos alunos.
    #Caso seja "None" vai ser utilizada na opção de gerar ata de exercício, a qual será utilizada os Dados dos professores e dos alunos.
    #Enfim pegou o arquivo Dados das disciplinas que funciona da mesma forma que turma, como um comparador para que filtre as informações.
    Turma = []
    Di = {}
    arquivo1 = open("Dados do sistema/Dados da turma.txt","r")
    if Z == False:
        Prof = []
        arquivo2 = open("Dados do sistema/Dados dos professores.txt","r")
    elif Z == True:
        Aluno = []
        arquivo2 = open("Dados do sistema/Dados dos alunos.txt","r")
    elif Z == None:
        Aluno = []
        Prof = []
        arquivo2 = open("Dados do sistema/Dados dos professores.txt","r")
        arquivo4 = open("Dados do sistema/Dados dos alunos.txt","r")
    arquivo3 = open("Dados do sistema/Dados das disciplinas.txt","r")
    #Adicionando todas informações dos arquivos na memória: Turma(referente à Turma), Di(referente à Disciplina), Prof(referente ao Professor), Aluno(referente ao aluno)
    for dados in arquivo1.readlines():
        dados = dados.split("*")
        Turma.append(dados)
    for dados in arquivo2.readlines():
        dados = dados.split("*")
        if Z == False or Z == None:
            Prof.append(dados)
        elif Z == True:
            Aluno.append(dados)
    for dados in arquivo3.readlines():
        dados = dados.split("*")
        Di[dados[1].strip("\n")] = dados[0]
    if Z == None:
        for dados in arquivo4.readlines():
            dados = dados.split("*")
            Aluno.append(dados)
        arquivo4.close()
    arquivo1.close()
    arquivo2.close()
    arquivo3.close()
    if Z == False:
        return Turma,Prof,Di
    elif Z == True:
        return Turma,Aluno,Di
    elif Z == None:
        return Turma,Prof,Di,Aluno


def Todas_turmas_Prof():
    #Para mostrar todas as turmas será utilizado  a memoria Turma, Prof e Di
    #Primeiramente chama-se a definição relatória e coloca como parâmetro False.
    #Logo apos passo por toda memória de Professores(Prof) e da-se um enumerate para mostrar a posição para o usuário e logo após pergunta em qual posição está
    #o dado que ele deseja gerar o relatório.
    try:
        Turmas,Professores,Di = relatório(False)
        print("{0:0>5}  {1:}".format("Número","Nome"))
        for posição,professor in enumerate(Professores):
            print("{0:0>5}   {1:}".format(posição+1,professor[0]))
        Professor_Número = int(input("Digite o Número do professor que desejar emiti um relatório: "))
        if  not str(Professor_Número).isdigit() or Professor_Número>len(Professores) or Professor_Número == 0 :
            input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
            os.system("cls")
            return Todas_turmas_Prof()
        print("\nProfessor: %s\n"%Professores[Professor_Número-1][0])
    #As memórias controlador serve para separar as informações que seráo manipuladas para formar o relatório relacionado ao professor.
    #O controlador1 vai guardar em um dicionário as informações do semestres que os professor tem no sistema e vai relacioná-lo com o codigo da turma.
    #O controlador2 vai guardar em um dicionário as informações do código da turma do professor e vai relacioná-lo com o codigo da disciplina.
    #Lembrando que o codigo da disciplia foi guardado em dicionário assim tem o código da disciplina relacionado com o nome.
    #Criou-se condições para que so adicione as informações aos controladores referente ao professor escolhido.
        controlador1 = {}
        controlador2 = {}
        for Turma in Turmas:
            if Turma[3] == Professores[Professor_Número-1][1] and Turma[2] in Di: #Turma[2] é o código da disciplina e ele confere se há no dicionário Di.
                if Turma[1] not in controlador1:
                    controlador1[Turma[1]] = [Turma[0]]
                elif Turma[0] not in controlador1[Turma[1]]:
                        controlador1[Turma[1]].append(Turma[0])
                if Turma[0] not in controlador2:
                    for codigo_disciplina in Di:
                        if codigo_disciplina  == Turma[2]:
                            controlador2[Turma[0]] = [Di[codigo_disciplina]]
                elif Di[Turma[2]] not in controlador2[Turma[0]]:
                    for codigo_disciplina  in Di:
                        if codigo_disciplina  == Turma[2]:
                            controlador2[Turma[0]].append(Di[codigo_disciplina])
    #Criação de um layout para o relatório
        for periodo in controlador1:    #Andado pelos semestre do professor.
            print("="*25)
            print("\tPeríodo: %s"%periodo)
            for posição in range(0,len(controlador1[periodo])):#Vai passar por cada codigo da turma
                print("\t\tTurma %s:"%controlador1[periodo][posição])   #Mostra nome da turma
                for codigo_turma in controlador2:   #Passando por cada codigo da turma
                    if codigo_turma == controlador1[periodo][posição]:  #Vendo se o codigo da turma da controlador2 tem algum dado relacionado com o controlador1
                    #Caso tenha ele executa a ação de mostrar o nome da disciplina.
                        Nome_disciplina = "\n\t\t\t".join(controlador2[codigo_turma])
                        print("\t\t\t%s"%Nome_disciplina)
        print("\n")
        return
    except ValueError:
        input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
        os.system("cls")
        return Todas_turmas_Prof()


def Turmas_por_semestre_Prof():
    #Código é semelhante a todas as turmas, o diferente é que pede-se o semestre e assim filtra por apenas pelo período colocado.
    try:
        os.system("cls")
        Turmas,Professores,Di = relatório(False)
        print("{0:0>5}  {1:}".format("Número","Nome"))
        for posição,professor in enumerate(Professores):
            print("{0:0>5}   {1:}".format(posição+1,professor[0]))
        Professor_Número = int(input("Digite o Número do professor que desejar emiti um relatório: "))
        if  not str(Professor_Número).isdigit() or Professor_Número>len(Professores) or Professor_Número == 0 :
            input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
            os.system("cls")
            return Turmas_por_semestre_Prof()
        controlador = []
        pede_Semestre = input("Escolha qual semestre que deseja ver: ")
        for Turma in Turmas:
            if Professores[Professor_Número-1][1] == Turma[3] and Turma[1] == pede_Semestre and Turma[0] not in controlador :
                controlador.append(Turma[0])
        if controlador == []:
            return print("O professor %s não tem turmas catalogadas no semestre %s."%(Professores[Professor_Número-1][0],pede_Semestre))
        print("Professor(a): %s"%Professores[Professor_Número-1][0])
        controlador1 = {}
        controlador2 = {}
        for Turma in Turmas:
            if Turma[3] == Professores[Professor_Número-1][1]:
                if Turma[1] not in controlador1 and Turma[1] == pede_Semestre:
                    controlador1[Turma[1]] = [Turma[0]]
                elif Turma[1] in controlador1 and Turma[0] not in controlador1[Turma[1]] and Turma[1] == pede_Semestre:
                        controlador1[Turma[1]].append(Turma[0])
                if Turma[0] not in controlador2 and Turma[1] == pede_Semestre:
                    for codigo_disciplina in Di:
                        if codigo_disciplina == Turma[2]:
                            controlador2[Turma[0]] = [Di[codigo_disciplina]]
                elif Turma[0] in controlador2 and Di[Turma[2]] not in controlador2[Turma[0]] and Turma[1] == pede_Semestre:
                    for codigo_disciplina in Di:
                        if codigo_disciplina == Turma[2]:
                            controlador2[Turma[0]].append(Di[codigo_disciplina])
        for periodo in controlador1:
            print("Período: %s"%pede_Semestre)
            for posição in range(0,len(controlador1[periodo])):
                print("\tTurma %s:"%controlador1[periodo][posição])
                for codigo_turma in controlador2:
                    if codigo_turma == controlador1[periodo][posição]:
                        Nome_disciplina = "\n\t\t".join(controlador2[codigo_turma])
                        print("\t\t%s"%Nome_disciplina)
    except ValueError:
        input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
        os.system("cls")
        return Turmas_por_semestre_Prof()

def Todas_turmas_alunos():
    #Mesma lógica que o dos professores, o diferente é que agora utiliza o parâmetro True que irá retornar a lista de Turma,Aluno e Di.
    try:
        Turmas,Alunos,Di = relatório(True)
        print("{0:0>5}  {1:}".format("Número","Nome"))
        for posição,Aluno in enumerate(Alunos):
            print("{0:0>5}   {1:}".format(posição+1,Aluno[0]))
        Pede_Número = int(input("Digite o Número do aluno que desejar emiti um relatório: "))
        if  not str(Pede_Número).isdigit() or Pede_Número>len(Alunos) or Pede_Número == 0 :
                input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
                os.system("cls")
                return Todas_turmas_alunos()
        Aluno = Alunos[Pede_Número-1][0]
        Cpf_Aluno = Alunos[Pede_Número-1][1]
        print("\nAluno: %s\n"%Aluno)
        controlador1 = {}
        controlador2 = {}
        for Turma in Turmas:
            if Turma[4] == Cpf_Aluno and Turma[2] in Di:
                if Turma[1] not in controlador1:
                        controlador1[Turma[1]] = [Turma[0]]
                elif Turma[0] not in controlador1[Turma[1]]:
                    controlador1[Turma[1]].append(Turma[0])
                if Turma[0] not in controlador2:
                    for codigo_disciplina in Di:
                        if codigo_disciplina == Turma[2]:
                            controlador2[Turma[0]] = [Di[codigo_disciplina]]
                elif Di[Turma[2]] not in controlador2[Turma[0]]:
                    for codigo_disciplina in Di:
                        if codigo_disciplina == Turma[2]:
                            controlador2[Turma[0]].append(Di[codigo_disciplina])
        for periodo in controlador1:
            print("\tPeríodo: %s"%periodo)
            for posição in range(0,len(controlador1[periodo])):
                print("\t\tTurma %s:"%controlador1[periodo][posição])
                for codigo_turma in controlador2:
                    if codigo_turma == controlador1[periodo][posição]:
                        Nome_disciplina = "\n\t\t\t".join(controlador2[codigo_turma])
                        print("\t\t\t%s"%Nome_disciplina)
        print("\n")
    except ValueError:
        input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
        os.system("cls")
        return Todas_turmas_alunos()


def Turmas_por_semestre_Aluno():
    #Utilizou o filtro de um único semestre
    try:
        Turmas,Alunos,Di = relatório(True)
        print("{0:0>5}  {1:}".format("Número","Nome"))
        for posição,Aluno in enumerate(Alunos):
            print("{0:0>5}   {1:}".format(posição+1,Aluno[0]))
        Pede_Número = int(input("Digite o Número do aluno que desejar emiti um relatório: "))
        if  not str(Pede_Número).isdigit() or Pede_Número>len(Alunos) or Pede_Número == 0 :
                input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
                os.system("cls")
                return Todas_turmas_alunos()
        controlador = []
        pede_Semestre = input("Escolha qual semestre que deseja ver: ")
        for Turma in Turmas:
            if Alunos[Pede_Número-1][1] == Turma[4] and Turma[1] == pede_Semestre and Turma[0] not in controlador :
                controlador.append(Turma[0])
        if controlador == []:
            return print("O Aluno %s não tem turmas catalogadas no semestre %s."%(Alunos[Pede_Número-1][0],pede_Semestre))
        Aluno = Alunos[Pede_Número-1][0]
        Cpf_Aluno = Alunos[Pede_Número-1][1]
        print("\nAluno: %s\n"%Aluno)
        controlador1 = {}
        controlador2 = {}
        for Turma in Turmas:
            if Turma[4] == Cpf_Aluno:
                if Turma[1] not in controlador1 and Turma[1] == pede_Semestre:
                        controlador1[Turma[1]] = [Turma[0]]
                elif Turma[1] in controlador1 and Turma[0] not in controlador1[Turma[1]] and Turma[1] == pede_Semestre:
                    controlador1[Turma[1]].append(Turma[0])
                if Turma[0] not in controlador2 and Turma[1] == pede_Semestre:
                    for codigo_disciplina in Di:
                        if codigo_disciplina == Turma[2]:
                            controlador2[Turma[0]] = [Di[codigo_disciplina]]
                elif Turma[0] in controlador2 and Di[Turma[2]] not in controlador2[Turma[0]] and Turma[1] == pede_Semestre:
                    for codigo_disciplina in Di:
                        if codigo_disciplina == Turma[2]:
                            controlador2[Turma[0]].append(Di[codigo_disciplina])
        for periodo in controlador1:
            print("\tPeríodo: %s"%periodo)
            for posição in range(0,len(controlador1[periodo])):
                print("\t\tTurma %s:"%controlador1[periodo][posição])
                for codigo_turma in controlador2:
                    if codigo_turma == controlador1[periodo][posição]:
                        Nome_disciplina = "\n\t\t\t".join(controlador2[codigo_turma])
                        print("\t\t\t%s"%Nome_disciplina)
        print("\n")
    except ValueError:
        input("Você digitou um caractere inválido, digite um número válido. (APERTE ENTER PARA CONTINUAR)")
        os.system("cls")
        return Todas_turmas_alunos()


def Ata_de_exercício():
    #A ata de exercício vai utilizar todas as memórias então foi criado uma memória para cada uma delas para guardar as informações necessária para cada uma delas
    #Pede o período e a turma a qual o usuário queira gerar a ata, assim irá filtar esses dados referente aos professores que tem os dados compatíveis(1)
    os.system("cls")
    Turmas,Professores,Disciplinas,Alunos = relatório(None)
    Nome_Professores = {}
    Nome_Alunos = {}
    periodos = []
    Turma = []
    for turma in Turmas:
        if turma[1] not in periodos:
            periodos.append(turma[1])
        if turma[0] not in Turma:
            Turma.append(turma[0])
    while True:
        os.system("cls")
        for periodo in periodos:
            print("__{}__".format(periodo))
        escolha_periodo = input("Escolha o periodo a qual deseja emite a ata de exercício. ")
        if escolha_periodo in periodos:
            break
        else:
            input("Periodo inválido, digite novamente. (ENTER PARA CONTINUAR")
    while True:
        os.system("cls")
        for turma_ in Turma:
            print("__{}__".format(turma_))
        escolha_turma = input("Escolha a turma a qual deseja emitir a ata de exercício." )
        if escolha_turma in Turma:
            os.system("cls")
            break
        else:
            input("Turma inválida, digite novamente. (ENTER PARA CONTINUAR")
    for turma in  Turmas:#(1)
        #Fez uma relação entre o cpf e o nome do professor, assim será pedido o cpf do professor para achar o nome dele
        for Professor in Professores:
            if Professor[1] not in Nome_Professores and Professor[1] == turma[3] and escolha_periodo == turma[1] and escolha_turma == turma[0]:
                Nome_Professores[Professor[1]] = Professor[0]
    if  len(Nome_Professores) == 0:
        return print("O periodo ou turma não tem dados relacionados no sistema.")
    while True:
        os.system("cls")
        #Pede para escolher o professor
        print("Professores : ")
        print("="*80)
        print("\t{0:13} {1:}".format("CPF","Nome"))
        for professor in Nome_Professores:
            print("\t{0:13} {1:}".format(professor,Nome_Professores[professor]))
        cpf_professor_desejada = input("Digite o CPF do professor que deseja emiti a ata de exercício. ")
        if cpf_professor_desejada not in Nome_Professores:
            input("Código inválido, digite novamente. (ENTER PARA CONTINUAR")
            continue
        else:
            input("Nome do professor escolhido : %s. (ENTER PARA CONTINUAR)"%Nome_Professores[cpf_professor_desejada])
            break
    while True:
        os.system("cls")
        #Pede o nome da disciplina do professor que queira gerar a ata.
        print("Disciplinas : ")
        Nome_disciplinas = {}
        print("="*80)
        print("\t{0:6} {1:}".format("Código","Nome"))
        for disciplina in Disciplinas:
            for turma in Turmas:
                if turma[2] == disciplina and turma[3] == cpf_professor_desejada and disciplina not in Nome_disciplinas:
                    Nome_disciplinas[disciplina] = Disciplinas[disciplina]
        for disciplina in Nome_disciplinas:
            print("\t{0:6} {1:}".format(disciplina,Nome_disciplinas[disciplina]))
        codigo_disciplina_desejada = input("Digite o código da disciplina que deseja emiti a ata de exercício. ")
        if codigo_disciplina_desejada not in Disciplinas:
            input("Código inválido, digite novamente. (ENTER PARA CONTINUAR")
            continue
        else:
            input("Nome da disciplina escolhida : %s. (ENTER PARA CONTINUAR)"%Disciplinas[codigo_disciplina_desejada])
            break
    #Assim filtra todos os alunos que tem todos os dados inseridos compatíveis com os dados inseridos: código da turma, periodo,cpf do professor e o codigo da disciplina
    for turma in Turmas:
        for aluno in Alunos:
            if aluno[1] not in Nome_Alunos and aluno[1] == turma[4] and escolha_periodo == turma[1] and escolha_turma == turma[0] and turma[3] == cpf_professor_desejada and turma[2] == codigo_disciplina_desejada:
                Nome_Alunos[aluno[1].strip("\n")] = aluno[0]
    #Essa memória de organizador é para deixar os nomes organizados colocando-os em uma lista, e organizando-os. (For necessário esse procedimento pois estava em um
#   dicionário
    Organizador_Dicionário_Alunos = []
    for aluno in Nome_Alunos:
        Organizador_Dicionário_Alunos.append([Nome_Alunos[aluno],aluno])
    Organizador_Dicionário_Alunos = sorted(Organizador_Dicionário_Alunos)
    os.system("cls")
    #Layout da ata de exercício:
    print("="*80)
    print("{0:20} {1:} {2:} {3:}".format("Código da disciplina","Período","Turma","Vagas"))
    print("{0:20} {1:7} {2:5} {3:4}".format(codigo_disciplina_desejada,escolha_periodo,escolha_turma,len(Nome_Alunos)))
    print("="*80)
    print("Nome da disciplina")
    print(Nome_disciplinas[codigo_disciplina_desejada])
    print("="*80)
    print("Professor(es)")
    print(Nome_Professores[cpf_professor_desejada])
    print("="*144)
    print("|{0:^3}|{1:^4}|{2:^11}|{3:^60}|{4:^60}|".format("ORD","NOTA","CPF","NOME DO(A) ALUNO(A)","ASSINATURA"))
    print("="*144)
    if len(Organizador_Dicionário_Alunos) == 0:
        print("|{:^142}|".format("Essa lista está sem alunos"))
    else:
        for posição,aluno in enumerate(Organizador_Dicionário_Alunos):
            print("|{0:>3}|{1:4}|{2:<11}|{3:<60}|{4:60}|".format(posição+1,"",aluno[1],aluno[0],""))
    print("="*144) 
        
    


