


from tkinter import ttk
from tkinter.tix import Tree
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from dado import *
from dado import adicionar_dados
from dado import remover_dados
from dado import pesquisar_dados



#cores ---------------------------

cinzaescuro = "#1C1C1C" #cinza escuro
cinzaclaro ="#A9A9A9" 
azul = "#1E90FF"
azulescuro = "#0000FF"
branco = "#F0F8FF"
azulclaro = "#87CEFA"
preto ="#1C1C1C"
pretoclaro = "#4F4F4F"
#criando janela

janela  = Tk()
janela.title("☎📞")
# janela.geometry("560x560")

janela.configure(background=azulescuro)
janela.resizable(width=FALSE, height=FALSE) # / Caso ative esse código a janela não poderá ter tamanho alterado

Style = Style(janela)
Style.theme_use("clam")


#Separando a janela em partes distintas
frame_cima = Frame(janela, width=560, height=40, bg=preto)
frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

frame_baixo = Frame(janela, width=560, height=200, bg=azulescuro)
frame_baixo.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW )

frame_tabela = Frame(width=560, height=305,  bg=azulescuro)
frame_tabela.grid(row=2, column=0, padx=0, pady=15, sticky=NSEW )

#Colocando nome no frame de cima

cima_nome = Label(frame_cima, text="Agenda Contec", anchor=NE, font=("cambria 20 bold "), bg=preto, fg=branco)
cima_nome.place(x=175, y=-8)

cima_assinatura = Label(frame_cima, text="Cread_by_Jhow",anchor=NE, font=("arial 7"), bg=preto, fg=branco )
#anchor=NE torna o o texto movel por x e y
cima_assinatura.place(x=320, y=25)

global tree

def mostrar_dados ():
    global tree
    #creando a tabela com scrollbars
    list_header = ['Empresa','Resp', 'Tel', 'Zap', 'E-mail']
    dados = ver_dados ()
        

    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(
        frame_tabela, orient="vertical", command=tree.yview)

    #Hoeizontal scrollbar
    hsb = ttk.Scrollbar(
        frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0, row=1, sticky="ew")

    # hd=["nw","nw","nw","nw","nw"]
    # h=[120,50,80,120,200]
    # n=0

    #Tree cabeçalho
    tree.heading(0, text="Empresa", anchor=NW)
    tree.heading(1, text="Resp", anchor=NW)
    tree.heading(2, text="Tel", anchor=NW)
    tree.heading(3, text="Zap", anchor=NW)
    tree.heading(4, text="E-mail", anchor=NW)

    #Tree corpo
    tree.column(0, width=100,anchor="nw")
    tree.column(1, width=100,anchor="nw")
    tree.column(2, width=100,anchor="nw")
    tree.column(3, width=100,anchor="nw")
    tree.column(0, width=180,anchor="nw")

    for item in dados:
        tree.insert("", "end", values=item)

mostrar_dados ()

#função adicionar

def inserir ():

    empresa = pre_empresa.get()
    socio =pre_socio.get()
    tel =pre_tel.get()
    zap =pre_zap.get()
    email =pre_email.get()
    
    dado = [empresa, socio, tel, zap, email]

    if empresa == "" or tel == "":
        messagebox.showwarning("Jhow avisa!", "Os dados empresa e tel são obrigatorios qualquer dúvida ver com o Jhow!")

    else:
        adicionar_dados(dado)
        messagebox.showinfo("Jhow avisa!", "Os dados foram cadastrados com sucesso! ")

        pre_empresa.delete(0, "end")
        pre_socio.delete(0, "end")
        pre_tel.delete(0, "end")
        pre_zap.delete(0, "end")
        pre_email.delete(0, "end")

        mostrar_dados()


#Deletar dado
def remover ():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        empresa = str(tree_lista[0])

        remover_dados(empresa)

        messagebox.showinfo("Jhow avisa", "Os dados foram deletados com sucesso!")

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar_dados()

    except:
        messagebox.showwarning("Jhow avisa", "Por favor selecione uma informação na tabela!")

#procurar
def procurar():
    empresa = e_buscar.get()
    dados = pesquisar_dados(empresa)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert("", "end", values=item)

    e_buscar.delete(0,"end")



#configurando frame de baixo

l_empresa = Label(frame_baixo, text="Empresa:", anchor=NW, font=("Ivy 10 bold"), bg=azulescuro, fg=branco)
l_empresa.place(x=10, y=20)
pre_empresa = Entry(frame_baixo, width=25, justify="left", font=("", 10), highlightthickness=1)
#justify é de onde começo a escrever da direita ou da esquerda.
pre_empresa.place(x=100, y=20)

l_socio = Label(frame_baixo, text="Responsável:", anchor=NW, font=("Ivy 10 bold"), bg=azulescuro, fg=branco)
l_socio.place(x=10, y=60)
pre_socio = Entry(frame_baixo, width=25, justify="left", font=("", 10), highlightthickness=1)
pre_socio.place(x=100, y=60)

l_tel = Label(frame_baixo, text="Telefone:", anchor=NW, font=("Ivy 10 bold"), bg=azulescuro, fg=branco)
l_tel.place(x=10, y=100)
pre_tel = Entry(frame_baixo, width=25, justify="left", font=("", 10), highlightthickness=1)
pre_tel.place(x=100, y=100)

l_zap = Label(frame_baixo, text="Whatsapp:", anchor=NW, font=("Ivy 10 bold"), bg=azulescuro, fg=branco)
l_zap.place(x=300, y=20)
pre_zap = Entry(frame_baixo, width=25, justify="left", font=("", 10), highlightthickness=1)
pre_zap.place(x=400, y=20)

l_email = Label(frame_baixo, text="E-mail:", anchor=NW, font=("Ivy 10 bold"), bg=azulescuro, fg=branco)
l_email.place(x=300, y=60)
pre_email = Entry(frame_baixo, width=25, justify="left", font=("", 10), highlightthickness=1)
pre_email.place(x=400, y=60)

l_buscar = Button(frame_baixo,width=8,command=procurar, text="Buscar", font=("Ivy 8 bold"), bg=branco, fg=preto, relief=RAISED, overrelief=RIDGE)
l_buscar.place(x=300, y=100)

e_buscar = Entry(frame_baixo, width=25, justify="left", font=("",10), highlightthickness=1)
e_buscar.place(x=400, y=100)

l_cadastrar = Button(frame_baixo,width=10,command=inserir, text="Cadastrar", font=("Ivy 8 bold"), bg=branco, fg=preto, relief=RAISED, overrelief=RIDGE)
l_cadastrar.place(x=150, y=150)

l_deletar = Button(frame_baixo,width=10,command=remover, text="Deletar", font=("Ivy 8 bold"), bg=branco, fg=preto, relief=RAISED, overrelief=RIDGE)
l_deletar.place(x=470, y=150)

l_dados = Button(frame_baixo,width=20,command=mostrar_dados, text="Mostrar dados", font=("Ivy 8 bold"), bg=branco, fg=preto, relief=RAISED, overrelief=RIDGE)
l_dados.place(x=280, y=150)

# l_editar = Button(frame_baixo,width=30, text="Editar", font=("Ivy 8 bold"), bg=branco, fg=preto, relief=RAISED, overrelief=RIDGE)
# l_editar.place(x=300, y=180)

janela.mainloop()

