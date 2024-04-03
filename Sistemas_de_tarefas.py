import os
tarefas=[]
nome=[]
c=""

def add(nome):
    nome=str(input("Qual o nome da atividade a ser adicionada:\n"))
    tarefas.append(nome)
def m(nome):
    e()
    nome=str(input("Informe qual o nome da atividade que deve ser marcada\n")) 
    nome=("X",nome[0])
    print(nome)
def e():
    for item in tarefas:
        print(item)
def r(nome):
    print("Aqui segue a lsita de atividades:\n--------------------------------------------------------------------------------------------------")
    e()
    nome=str(input("\nInforme o nome da atividade que deseja excluir:"))
    for i in range(len(tarefas)):
        if(tarefas[i]==nome):
            tarefas.remove(nome)  
            tarefas.pop(nome)
            print(tarefas)
def l(tarefas):
    o=(input("Se desejar mesmo limpar a lsita de tarefas presione a tecla (Enter) "))
    if (o==""):
        for linha in tarefas:
            for i in range(len(linha)):
                linha[i]=0
        e()
while (c==""):
 opc=int(input("Informe qual ação deseja fazer:\n----------------------------------------------------\n1 - Incluir tarefa\n2 - Marcar como feita\n3 - Remover tarefa\n4 - Esvaziar lista\n5 - Visualizar lista\n"))        
 match opc:
     case 1:
        add(nome)
        c=str(input("\nSe deseja continuar presione (Enter)"))
     case 2:
        m(nome)
        c=str(input("\nSe deseja continuar presione (Enter)"))
     case 3:
        r(nome)
        c=str(input("\nSe deseja continuar presione (Enter)"))
     case 4:
        l(tarefas)   
        c=str(input("\nSe deseja continuar presione (Enter)")) 
     case 5:
       e()
       c=str(input("\nSe deseja continuar presione (Enter)"))