# coding=UTF-8
from tkinter import*
from tkinter import messagebox
import random


#============================================================================
#
#       FUNcoES AUXILIARES
#
#============================================================================

def criarbotoes():
#>>>>Funcao que cria a interface e é usada para resetar o jogo

    global b,jogada
    jogada = 1
    blank = PhotoImage(file = "./res/blank.png")
    o = PhotoImage(file="./res/o.png")
    b.append(Button(f,text="        ",command = lambda:cliquenojogo(b[0])))
    blank = PhotoImage(file="./res/blank.png")
    b[0].config(image=blank)
    b[0].image = blank
    b[0].grid()
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[1])))
    b[1].grid(row = 0,column=1,padx=1,pady=1)
    b[1].config(image=blank)
    b[1].image = blank
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[2])))
    b[2].config(image=blank)
    b[2].image = blank
    b[2].grid(row = 0,column=2,padx=1,pady=1) 
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[3])))
    b[3].config(image=blank)
    b[3].image = blank
    b[3].grid(row = 1,column=0,padx=1,pady=1)
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[4])))
    b[4].config(image=blank)
    b[4].image = blank
    b[4].grid(row = 1,column=1,padx=1,pady=1)
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[5])))
    b[5].config(image=blank)
    b[5].image = blank
    b[5].grid(row = 1,column=2,padx=1,pady=1)
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[6])))
    b[6].config(image=blank)
    b[6].image = blank
    b[6].grid(row = 2,column=0,padx=1,pady=1)
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[7])))
    b[7].config(image=blank)
    b[7].image = blank
    b[7].grid(row = 2,column=1,padx=1,pady=1)
    b.append(Button(f,text="       ",command = lambda:cliquenojogo(b[8])))
    b[8].config(image=blank)
    b[8].image = blank
    b[8].grid(row = 2,column=2,padx=1,pady=1)
    for i in range(0,9):
        b[i].config(text = "       ",state = NORMAL,relief = RAISED)

def teste(t):
#>>> Funcao que testa se ou a maquina ou o jogador ganharam a partida.

    global b,vit, vitorias,derr,derrotas,dificuldade,jogada
    vitoria = False
    if b[0]['text']== t and b[3]['text']== t and b[6]['text'] == t : vitoria = True 
    elif b[1]['text']== t and b[4]['text']== t and b[7]['text'] == t : vitoria = True 
    elif b[2]['text']== t and b[5]['text']== t and b[8]['text'] == t : vitoria = True 
    elif b[0]['text']== t and b[1]['text']== t and b[2]['text'] == t : vitoria = True
    elif b[3]['text']== t and b[4]['text']== t and b[5]['text'] == t : vitoria = True
    elif b[6]['text']== t and b[7]['text']== t and b[8]['text'] == t : vitoria = True
    elif b[0]['text']== t and b[4]['text']== t and b[8]['text'] == t : vitoria = True
    elif b[2]['text']== t and b[4]['text']== t and b[6]['text'] == t : vitoria = True
    if (vitoria == True and t == "   X   "):
            vit = vit+1
            vitorias.set(vit)
            if dificuldade == "player":
                player = "Jogador 1"
            else: player = "Você"
            print(player + " ganhou o jogo Parabens!")
            print(b[0]['text']+"|"+b[1]['text']+"|"+b[2]['text']+"\n"+b[3]['text']+"|"+b[4]['text']+"|"+b[5]['text']+"\n"+b[6]['text']+"|"+b[7]['text']+"|"+b[8]['text'])
            reset = messagebox.askyesno("Jogo da Velha",player +" ganhou, deseja reiniciar o jogo?")
            if reset == True:
                criarbotoes()
                return
            else: jan.destroy()
    elif (vitoria == True and t == "   O   "):
            if dificuldade == "player":
                player = "Jogador 2 ganhou o jogo Parabens"
            else: player = "Você PERDEU"
            print(player)
            derr = derr +1
            derrotas.set(derr)
            print(b[0]['text']+"|"+b[1]['text']+"|"+b[2]['text']+"\n"+b[3]['text']+"|"+b[4]['text']+"|"+b[5]['text']+"\n"+b[6]['text']+"|"+b[7]['text']+"|"+b[8]['text'])
            reset = messagebox.askyesno("Jogo da Velha",player + ", deseja reiniciar o jogo?")
            if reset == True:               
                criarbotoes()
                return
            else: jan.destroy()
    elif velha():
            return
    else:
        return vitoria

def velha():
#>>>Funcao que auxilia a funcao teste em caso ocorra velha.

    global emp,empates
    j = 0
    for i in range(0,9):
        if b[i]['state'] == 'disabled':
            j = j+1
    if j == 9:
        print("O jogo acabou! \n Deu Velha!")
        emp = emp +1
        empates.set(emp)
        reset = messagebox.askyesno("Jogo da Velha","DEU VELHA, deseja reiniciar o jogo?")
        if reset == True:
            criarbotoes()
            return True
        else: jan.destroy()
    return False
                
def testarpossibilidade(play):
#>>>Funcao que estabelece a possibilidade de utilizacao do botao pelo computador

    global jogada
    if b[play]['state'] == 'normal':
        o = PhotoImage(file="./res/o.png")
        b[play].config(image = o,text = "   O   ",state = DISABLED,relief = FLAT)
        b[play].image = o
        jogada = jogada +1
        teste("   O   ")
        return True
    else: return False

#===============================================================================
#
#    JOGADAS DO COMPUTADOR
#
#===============================================================================

def jogadadocomputadordificil():
#
#    Computador joga para ganhar o maximo possivel,
#          checando as jogadas do jogador
# e caso seja uma jogada conhecida,utiliza o turno bloqueando-a.
#
    
    global b
    vezesjogadas = 0
    j = 0
    play = 123
    for i in range(0,9):
        if b[i]['text'] == "   X   ":
            vezesjogadas += 1
        
    #Checa primeiro lance do Jogador
    if b[4]['text']== "   X   " and vezesjogadas == 1:
        x = [0,2,6,8]
        r = random.sample(x,k=len(x))
        if testarpossibilidade(r[0]):
            print("Hmm entao você vai comecar pelo meio...")
            return
    for i in [1,3,5,7]:
        if b[i]['text'] == "   X   " and vezesjogadas == 1:
            if i == 1 :x = [0,2,4,7]
            if i == 3 :x = [0,4,5,6]
            if i == 5 :x = [2,3,4,8]
            if i == 7 :x = [6,8,4,1]
            r = random.sample(x,k=len(x))
            if testarpossibilidade(r[0]):
                print("Hmm entao você vai comecar pela lateral...")
                return
    for i in [0,2,6,8]:
        if b[i]['text'] == "   X   " and vezesjogadas == 1:
            if testarpossibilidade(4):
                print("Hmm entao você vai comecar pelas quinas...")
                return
    if ((b[0]['text'] == "   X   " and b[8]['text'] == "   X   ")== True or (b[2]['text'] == "   X   " and b[6]['text'] == "   X   ") == True)and (vezesjogadas == 2):
        x = [1,3,5,7]
        r = random.sample(x,k=len(x))
        if testarpossibilidade(r[0]):
            print("É uma cilada!")
            return
    #Verifica se existe possibilidade de Ganhar
        
    for i in range(0,9,3):
        if b[i+1]['text']== "   O   " and b[i+2]['text']== "   O   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")

                return
            break
    for i in range(1,9,3):
        if b[i-1]['text']== "   O   " and b[i+1]['text']== "   O   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")

                return
            break
    for i in range(2,9,3):
        if b[i-1]['text']== "   O   " and b[i-2]['text']== "   O   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")

                return
            break
    for i in range(0,3):
        if b[i+3]['text']== "   O   " and b[i+6]['text']== "   O   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")

                return
            break
    for i in range(3,6):
        if b[i-3]['text']== "   O   " and b[i+3]['text']== "   O   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")

                return
            break
    for i in range(6,9):
        if b[i-3]['text']== "   O   " and b[i-6]['text']== "   O   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")

                return
            break
        
    if b[2]['text']== "   O   " and b[4]['text']== "   O   ":
        play = 6
        if testarpossibilidade(play) == True:
            teste("   O   ")

            return
    elif b[2]['text']== "   O   " and b[6]['text']== "   O   ":
        play = 4
        if testarpossibilidade(play) == True:
            teste("   O   ")

            return
    elif b[4]['text']== "   O   " and b[6]['text']== "   O   ":
        play = 2
        if testarpossibilidade(play) == True:
            teste("   O   ")

            return
    elif b[0]['text']== "   O   " and b[4]['text']== "   O   ":
        play = 8
        if testarpossibilidade(play) == True:
            teste("   O   ")

            return
    elif b[0]['text']== "   O   " and b[8]['text']== "   O   ":
        play = 4
        if testarpossibilidade(play) == True:
            teste("   O   ")

            return
    elif b[4]['text']== "   O   " and b[8]['text']== "   O   ":
        play = 0
        if testarpossibilidade(play) == True:
            teste("   O   ")

            return
    #Se nao existe possibilidade de ganhar ele joga pra nao perder
    if play == 123 or testarpossibilidade(play) == False:    
        print("Boa Jogada, mas nao posso deixar você vencer!")    
        jogadadocomputadormedio()
        

def jogadadocomputadormedio():
    #
    #      Computador Joga para evitar perder
    #
    
    global b
    play = 123
    #Primeiro testa se tem perigo
    r = random.sample(range(10),10)

    for i in range(0,9,3):
        if b[i+1]['text']== "   X   " and b[i+2]['text']== "   X   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")
                return
            break
    for i in range(1,9,3):
        if b[i-1]['text']== "   X   " and b[i+1]['text']== "   X   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")
                return
            break
    for i in range(2,9,3):
        if b[i-1]['text']== "   X   " and b[i-2]['text']== "   X   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")
                return
            break
    for i in range(0,3):
        if b[i+3]['text']== "   X   " and b[i+6]['text']== "   X   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")
                return
            break
    for i in range(3,6):
        if b[i-3]['text']== "   X   " and b[i+3]['text']== "   X   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")
                return
            break
    for i in range(6,9):
        if b[i-3]['text']== "   X   " and b[i-6]['text']== "   X   ":
            play = i
            if testarpossibilidade(play) == True:
                teste("   O   ")
                return
            break
        
    if b[2]['text']== "   X   " and b[4]['text']== "   X   ":
        play = 6
        if testarpossibilidade(play) == True:
            teste("   O   ")
            return
    elif b[2]['text']== "   X   " and b[6]['text']== "   X   ":
        play = 4
        if testarpossibilidade(play) == True:
            teste("   O   ")
            return
    elif b[4]['text']== "   X   " and b[6]['text']== "   X   ":
        play = 2
        if testarpossibilidade(play) == True:
            teste("   O   ")
            return
    elif b[0]['text']== "   X   " and b[4]['text']== "   X   ":
        play = 8
        if testarpossibilidade(play) == True:
            teste("   O   ")
            return
    elif b[0]['text']== "   X   " and b[8]['text']== "   X   ":
        play = 4
        if testarpossibilidade(play) == True:
            teste("   O   ")
            return
    elif b[4]['text']== "   X   " and b[8]['text']== "   X   ":
        play = 0
        if testarpossibilidade(play) == True:
            teste("   O   ")
            return
    # joga aleatoriamente caso nao se enquadre em perigo
    
    if play == 123 or testarpossibilidade(play) == False:
        jogadadocomputador()


def jogadadocomputador():
    #
    #   Computador joga de maneira aleatoria   
    #

    i=0
    for i in range(0,10):
        r = random.randint(0,8)
        if testarpossibilidade(r):
            break
    
#============================================================================
#        
#           FUNcoES DOS BOToES DA INTERFACE   
#
#============================================================================    
def cliquenojogo(b):
    
    global x , o, jogada ,dificuldade
    if jogada%2 == 0:
        print(str(jogada))
        o = PhotoImage(file="./res/o.png")
        b.config(text = "   O   ",image= o,state = DISABLED,relief = FLAT)
        b.image = o
        teste("   O   ")
        jogada = jogada+1
    else:
        x = PhotoImage(file="./res/x.png")
        b.config(text = "   X   ",image= x,state = DISABLED,relief = FLAT)
        b.image = x
        jogada = jogada+1
    if teste("   X   ") == False:
        if dificuldade == "facil":
            jogadadocomputador()
        elif dificuldade == "medio":
            jogadadocomputadormedio()
        elif dificuldade == "dificil":
            jogadadocomputadordificil()
            
        elif dificuldade == "player":
            return
        else:
            messagebox.showwarning("Aviso", "Selecione uma dificuldade!")
            criarbotoes()
            jogada = 1
            
def facil():
    global dificuldade,l1,l2,derr,vit,emp
    l1.config(text = 'Vitorias:')
    l2.config(text = 'Derrotas:')
    derr = 0
    emp = 0
    vit = 0
    empates.set(emp)
    vitorias.set(vit)
    derrotas.set(derr)
    dificuldade = "facil"
    
def medio():
    global dificuldade,l1,l2,derr,vit,emp
    l1.config(text = 'Vitorias:')
    l2.config(text = 'Derrotas:')
    derr = 0
    emp = 0
    vit = 0
    empates.set(emp)
    vitorias.set(vit)
    derrotas.set(derr)
    dificuldade = "medio"

def dificil():
    global dificuldade,l1,l2,derr,vit,emp
    l1.config(text = 'Vitorias:')
    l2.config(text = 'Derrotas:')
    derr = 0
    emp = 0
    vit = 0
    empates.set(emp)
    vitorias.set(vit)
    derrotas.set(derr)
    dificuldade = "dificil"

def player():
    global dificuldade,l1,l2,derr,vit,emp
    l1.config(text = 'Vitorias Jogador 1:')
    l2.config(text = 'Vitorias Jogador 2:')
    derr = 0
    emp = 0
    vit = 0
    empates.set(emp)
    vitorias.set(vit)
    derrotas.set(derr)
    dificuldade = "player"        

b = []
dificuldade = ""
vit = 0
derr = 0
emp = 0
jogada = 1



#======================
# MENU DE DIFICULDADES
#======================
jan = Tk()
jan.title("Jogo da Velha")

vitorias = StringVar()
vitorias.set(vit)

derrotas = StringVar()
derrotas.set(derr)

empates = StringVar()
empates.set(emp)

menubar = Menu(jan)
difmenu = Menu(menubar, tearoff=0)
difmenu.add_radiobutton(label="Fácil",command=facil)
difmenu.add_radiobutton(label="Médio",command=medio)
difmenu.add_radiobutton(label="Difícil", command=dificil)
difmenu.add_separator()
difmenu.add_radiobutton(label="Player(Beta)", command=player)
difmenu.add_separator()
difmenu.add_command(label="Sair", command=lambda:jan.destroy())
menubar.add_cascade(label="Dificuldade", menu=difmenu)

#====================
# JANELA PRINCIPAL
#====================

titulo = Label(jan,text = "Jogo da Velha",width =10, bg="#6495ED", font = ("Old English Text MT","30","bold"),fg="white" ,relief= GROOVE)
titulo.pack(fill= X,padx=10,pady=5)
f = Frame(jan)

f.pack()
f2= Frame(jan)

f2.pack(side = TOP)
f3= Frame(jan)
f3.pack()
jan.config(menu=menubar)
l1=Label(f2,text="Vitorias: ")
l1.grid(column = 0,row = 0, stick = E)
valvit = Label(f2, textvariable = vitorias)
valvit.grid(column = 1,row = 0,stick = W)
Label(f2,text="Empates: ").grid(column = 2,row = 0,stick = E)
valemp = Label(f2, textvariable = empates)
valemp.grid(column = 3,row = 0,stick = W)
l2=Label(f2,text="Derrotas: ")
l2.grid(column = 4,row = 0,stick= E)
valderr = Label(f2, textvariable = derrotas)
valderr.grid(column = 5,row = 0,stick = W)
criarbotoes()
d = Button(f3)
res = PhotoImage(file="./res/restart.png")
d.config(image=res,command = criarbotoes)
d.image = res
d.grid(padx=10,pady=10)
pcbtn = Button(f3)
pc = PhotoImage(file="./res/pc.png")
pcbtn.config(image=pc,command = jogadadocomputador)
pcbtn.image = pc
pcbtn.grid(padx=10,pady=10,column = 1,row = 0)

Label(jan, text = "versao 1.0.0",relief= RIDGE,anchor = E).pack(side = BOTTOM,fill = X)
jan.mainloop()



#b = tk.Button(root,command = clica)
#imagem = PhotoImage(file = "  .png")
#b.config(image = imagem)
#b.pack()
#root.mainloop()
