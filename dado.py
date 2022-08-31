import csv

lista = []

def adicionar_dados(i):
    #acessando o csv
    with open("dados.csv", "a+", newline="") as file: #"a+" serve para jogar para a 
        #ultima linha e o "newline=""" serve escrever na linha de baixo enves da mesma.
        escrever = csv.writer(file) #crio a variavel escrever
        escrever.writerow(i) #execulto a variavel escrever escrevendo por 
       

def ver_dados ():
    dados = []
    #acessando cvs
    with open ("dados.csv") as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
        # print(dados)
        return dados
    

def remover_dados (i):
   
    def adicionar_novalista(j):
        #acessando csv
        with open("dados.csv", "w", newline="") as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
        ver_dados()

    nova_lista = []
    empresa = i
    with open("dados.csv", "r") as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == empresa:
                    nova_lista.remove(linha)



    adicionar_novalista(nova_lista)


def pesquisar_dados(i):
    dados = []
    empresa = i
    print(i)

    #acessando csv
    with open ("dados.csv") as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == empresa:
                    dados.append(linha)
        
    return dados


