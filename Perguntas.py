#As repetições são utilizadas para caso o usuário coloque informações inadequadas ao sistema.
#Fazendo com que ela seja repetida até que as informações seja adequada ao que pede ao sistema.
def Dados_professores():    #Definição de Dados do professor
    while True:             #Repetição 
        print("Nome do Professor: ",end= "")
        nome_professor = input()    #Variável para guardar a informação do Nome do Professor
        print("CPF do Professor: ",end= "")
        CPF = input()               #Variável para guardar a informação do CPF do Professor
        print("Departamento do Professor: ",end= "")
        departamento = input()      #Variável para guardar a informação do Departamento do Professor
        np = nome_professor.replace(" ","")     #A variável "np" serve para que seja retirado os espaços da variável.
        d = departamento.replace(" ","")        #A variável "d" serve para que seja retirado os espaços da variável.
        if (np.isalpha()or not np == '') and (CPF.isdigit()or not CPF == '') and (d.isalpha() or not d == ''):  #Verificando se os dados estão de acordo como sistema requere.
            Lista = [nome_professor,CPF,departamento]   #Adiciona todos os dados a uma lista
            return Lista                                # Retornando a lista
        else:                                           #O else serve como condição a qual as informações inseridas não foram adequadas ao que o sistema requere.
            print("Dados inseridos estão incorretos, digite novamente: ")
        
    
def Dados_disciplinas():        #Definição de Dados da disciplina
    while True:                 #Repetição
        print("Nome da disciplina: ",end= "")
        nome_disciplina = input()   #Variável para guardar a informação do Nome da disciplina
        print("Código da disciplina: ",end= "")
        codigo_disciplina = input() #Variável para guardar a informação do Código da disciplina
        nd = nome_disciplina.replace(" ",'')    #A variável "nd" serve para que seja retirado os espaços da variável.
        if (nd.isalpha()or not nd == '' ) and (codigo_disciplina.isdigit() or not codigo_disciplina==''):
            #Verificando se os dados estão de acordo como sistema requere.
            Lista = [nome_disciplina,codigo_disciplina]         #Adiciona todos os dados a uma lista
            return Lista                                    # Retornando a lista
        else:                                               #O else serve como condição a qual as informações inseridas não foram adequadas ao que o sistema requere.
            print("Dados inseridos estão incorretos, digite novamente: ")
            
    
def Dados_alunos():             #Definição de Dados do aluno
    while True:                 #Repetição
        print("Nome do Aluno: ",end= "")
        nome_aluno = input()    #Variável para guardar a informação do Nome do aluno
        print("CPF do aluno: ",end= "")
        cpf_aluno = input()     #Variável para guardar a informação do Cpf do aluno
        na = nome_aluno.replace(" ","")     #A variável "na" serve para que seja retirado os espaços da variável.
        if (na.isalpha() or not na == '') and (cpf_aluno.isdigit() or not cpf_aluno == ''):     #Verificando se os dados estão de acordo como sistema requere.
            Lista = [nome_aluno,cpf_aluno]      #Adiciona todos os dados a uma lista
            return Lista                        # Retornando a lista
        else:                                   #O else serve como condição a qual as informações inseridas não foram adequadas ao que o sistema requere.
            print("Dados inseridos estão incorretos, digite novamente: ")
    
    
def Dados_turma():              #Definição de Dados da Turma
    while True:                 #Repetição
        print("Código da turma: ",end= "")
        codigo_turma = input()  #Variável para guardar a informação do codigo da turma
        print("Período: ",end = "")
        periodo = input()       #Variável para guardar a informação do período
        print("Código da disciplina: ",end = "")
        codigo_disciplina = input()     #Variável para guardar a informação do código da disciplina
        print("CPF do professor: ",end= "")
        cpf_professor = input()         #Variável para guardar a informação do CPF do professor
        print("CPF do aluno: ",end= "")
        cpf_aluno = input()             #Variável para guardar a informação do CPF do aluno
        p = periodo.replace(".","")     #A variável "p" serve para que seja retirado o ponto da variável período.
        #Verificando se os dados estão de acordo como sistema requere:
        if (codigo_turma.isalnum() or not codigo_turma == '') and (p.isdigit() or not p == '') and (codigo_disciplina.isdigit()or not codigo_disciplina == '') and (cpf_professor.isdigit or not cpf_professor == '') and (cpf_aluno.isdigit()or notcpf_aluno == ''):
            Lista = [codigo_turma,periodo,codigo_disciplina,cpf_professor,cpf_aluno]    #Adiciona todos os dados a uma lista
            return Lista            # Retornando a lista
        else:                       #O else serve como condição a qual as informações inseridas não foram adequadas ao que o sistema requere.
            print("Dados inseridos estão incorretos, digite novamente: ")

