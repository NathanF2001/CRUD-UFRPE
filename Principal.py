import Comandos,Relatório,os #foi importado as bibliotecas criadas para o programa: Relatório e Comando. E o "os" que é para executar o parâmetro system
while True:                 #cria-se uma repetição para que sempre execute o que vem a seguir:
    os.system("cls")        #Utilizou-se o parametro os.system, no cmd.
    print("="*80)
    print(""""Bem-vindo ao Sistema de Controle Acadêmico
    Escolha qual área deseja entrar:
    Dados de professores: Digite "P"
    Dados da disciplinas: Digite "D"    
    Dados de alunos: Digite "A" 
    Dados de Turmas: Digite "T"
    Gerar Relátorio: Digite "G"
    Digite "Sair" para finalizar do programa""")            #Imprimu-se o menu para que o usuário escolha em qual Setor do programa ele irá entrar.
    print("-"*80)
    escolha = input()                                       #Utilizou a variável "escolha" para guarda o valor referente ao menu
    escolha = escolha.upper()                               #Transforma-se a variável "escolha para maiúscula, caso o usuário digite minúscula
    os.system("cls")
    if escolha == "SAIR":                                   #Condição, caso o usuário queira finalizar o programa
        break                                               #Parar a repetição
    print("="*80)
    if escolha != "G" and escolha != "P" and escolha != "D"and escolha != "A"and escolha != "T" and escolha != "SAIR": # condição para que o usuário digite apenas 
        input("Área inválida, digite um número referente ao menu. (ENTER PARA CONTINUAR)")                             # caracteres que estão no sistema.
    else:
        if escolha == "G":                      #condição para ir para as configurações de Relatório
            while True:                         #Repetição para ocorrer a operação até ocorrer um "break".
                os.system("cls")
                print("""Digite:
                1 - Gerar relatório de todas as turmas em relação com professor.
                2 - Gerar relatório das matérias por semestre em relação professor.
                3 - Gerar relatório de todas as turmas em relação com o aluno.
                4 - Gerar relatório das matérias por semestre em relação ao aluno.
                5 - Gerar Ata de exercício.
                0 - Volta ao menu""")           #Menu do setor relatório.
                escolha2 = input()              #Variável "escolha2" como o valor referente ao menu do relatório
                if escolha2 == "0":             #Condição "0"
                    break                       #Finalizar a repetição
                elif escolha2 == "1":           #Condição "1"
                    Relatório.Todas_turmas_Prof()   #Executando a definição "Todas_turmas_Prof()" na biblioteca Relatório
                elif escolha2 == "2":                       #condição "2"
                    Relatório.Turmas_por_semestre_Prof()    #Executando a definição "Turmas_por_semestre_Prof()" na biblioteca Relatório
                elif escolha2 == "3":                       #condição "3"
                    Relatório.Todas_turmas_alunos()     #Executando a definição "Todas_turmas_alunos()" na biblioteca Relatório
                elif escolha2 == "4":                       #condição "4"
                    Relatório.Turmas_por_semestre_Aluno()   #Executando a definição "Turmas_por_semestre_Aluno()" na biblioteca Relatório
                elif escolha2 == "5":                       #condição "5"
                    Relatório.Ata_de_exercício()    #Executando a definição "Ata_de_exercício()" na biblioteca Relatório
                else:                                       #Caso o valor da variável "escolha2" não esteja no menu é executado esse else
                    print("="*80)
                    print("Digite um número válido")
                    print("="*80)
                    input("Aperte enter para continuar")
                    os.system("cls")
                    continue
                input("Aperte enter para continuar")
                os.system("cls")
                break
                
        else:                                       #Condição para ir para as configurações referente a "Professores","Disciplinas","Alunos","Turmas".
            while True:                             #Repetição para ocorrer a operação até ocorrer um "break".
                #Há apenas um menu para esse  4 setores porque o programa está otimizado/generalizado.
                print("""Digite:
                1 - Para adicionar novos dados
                2 - Para atualizar dados
                3 - Para apagar dados
                4 - Para consultar dados""")
                print("""Se deseja parar de executar o processo Digite "0" """) #Menu do setor.
                print("="*80)
                escolha2 = input()
                if escolha2 == "1":     #Condição "1"
                    Comandos.Novo(escolha)  #Executando a definição "Novo(escolha)" na biblioteca Comandos.
                elif escolha2 == "2":   #Condição "2"
                    Comandos.alterar(escolha)   #Executando a definição "alterar(escolha)" na biblioteca Comandos.
                elif escolha2 == "3":   #Condição "3"
                    Comandos.retirar(escolha)   #Executando a definição "retirar(escolha)" na biblioteca Comandos.
                elif escolha2 == "4":   #Condição "4"
                    y = Comandos.consultar(escolha) #Executando a definição "consultar(escolha)" na biblioteca Comandos.
                elif escolha2 == "0":   #Condição "0"
                    os.system("cls")
                    break
                else:                   ##Caso o valor da variável "escolha2" não esteja no menu é executado esse else.
                    print("="*80)
                    print("Digite um número válido")
                    print("="*80)
                    print(input("Aperte enter para continuar"))
                    os.system("cls")
                    continue
                print("="*80)
                print(input("Aperte enter para continuar"))
                os.system("cls")
    
        

      
