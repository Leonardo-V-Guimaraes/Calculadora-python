# Importando tkinter
from re import A
from tkinter import *
from tkinter import ttk

# cores

cor1 = "#1E1F1E" # Preto
cor2 = "#FEFFFF" # Branco
cor3 = "#38576B" # Azul escuro
cor4 = "#ECEFF1" # Cinza
cor5 = "#FFAB40" # Laranja

janela =Tk() # Importe do ttk
janela.title("Calculador") # para nomear a janela
janela.geometry("235x310") #Ajuste de tamanho de tela largura / altura
janela.config(bg=cor1) # Alterando o bg da calc.

# Criando os Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3) # Cria o frame do display + bg = cor do fundo
frame_tela.grid(row=0, column=0) # Metodo para dividir em linhas a tela

frame_teclado = Frame(janela, width=235, height=268) # Cria o frame do teclado 
frame_teclado.grid(row=1, column=0) # Metodo para dividir em linhas - Neste caso apenas 2. 1 para o tela e outro para o teclado


# Variavel todos valores
todos_valores = '' # Qualquer alteração que fizer em todos_valores sera mantido, sendo apenas sobrescrito
                   # como exemplo '12+99999*' ##ele vai salvar na variavel e ser executado dentro do resultado = eval

# criando label
valor_texto = StringVar() # Valor da tela. StringVar vai receber o valor da string e enviar para o textvariable

# Criando funções
def entrada_valores(event):

    global todos_valores # Definida como global para que possa ser acessada por todas as funções

    todos_valores = todos_valores + str(event) # Str transforma o valor event em string

    # passando valor par tela
    valor_texto.set(todos_valores)

# Funcão para calcular
def calcular():
    global todos_valores # Definida como global para que possa ser acessada por todas as funções
    resultado = eval(todos_valores) # Eval realiza as operações matematicas  

    valor_texto.set(str(resultado)) # O valor resultado já tem uma saida STR, mas para garantir está sendo setado novamente 

# Funcão limpar tela
def limpar_tela():
    global todos_valores # Definida como global para que possa ser acessada por todas as funções
    todos_valores="" #Limpa os valores inseridos
    valor_texto.set("") #Limpa a tela da calculadora

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=5, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
                                #textvariable é uma variavel que permite que os seus valores sejam alterados dinamicamente - padx distancia entre o ultimo numero até o canto - anchor orientação do texto ( este caso para esquerda) - justify funciona como o anchor
app_label.place(x=0, y=0)

# Criando os botões #

# 1 sequencia #
b_1 = Button(frame_teclado, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
# Cria botão - onde vai ser - text = Texto de exibição - width/height = tamanho e largura - bg = cor de fundo - font = Selecionar fonte - relief = Estilo da fonte - overrelief = adiciona qual sera o estilo que ira apresentar quando passar com o mouse
b_1.place(x=0, y=0) # Faz o set de onde o botão deve estar se baseando nos eixos X(horizontal) e Z(vertical)

b_2 = Button(frame_teclado, command = lambda: entrada_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_2.place(x=118, y=0)
# Botão laranja
b_3 = Button(frame_teclado, command = lambda: entrada_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # fg cor do conteudo interno
b_3.place(x=177, y=0)

# 2 sequencia # ( 4 botões )
b_4 = Button(frame_teclado, command = lambda: entrada_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_4.place(x=0, y=52)
b_5 = Button(frame_teclado, command = lambda: entrada_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_5.place(x=59, y=52)
b_6 = Button(frame_teclado, command = lambda: entrada_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_6.place(x=118, y=52)
# Botão laranja
b_7 = Button(frame_teclado, command = lambda: entrada_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # fg cor do conteudo interno
b_7.place(x=177, y=52)

# 3 sequencia # ( 4 botões )
b_8 = Button(frame_teclado, command = lambda: entrada_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_8.place(x=0, y=104)
b_9 = Button(frame_teclado, command = lambda: entrada_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_9.place(x=59, y=104)
b_10 = Button(frame_teclado, command = lambda: entrada_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_10.place(x=118, y=104)
# Botão laranja
b_11 = Button(frame_teclado, command = lambda: entrada_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # fg cor do conteudo interno
b_11.place(x=177, y=104)

# 4 sequencia # ( 4 botões )
b_12 = Button(frame_teclado, command = lambda: entrada_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_12.place(x=0, y=156)
b_13 = Button(frame_teclado, command = lambda: entrada_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_13.place(x=59, y=156)
b_14 = Button(frame_teclado, command = lambda: entrada_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_14.place(x=118, y=156)
# Botão laranja
b_15 = Button(frame_teclado, command = lambda: entrada_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # fg cor do conteudo interno
b_15.place(x=177, y=156)

# 5 sequencia #
b_16 = Button(frame_teclado, command = lambda: entrada_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_teclado, command = lambda: entrada_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_17.place(x=118, y=208)
# Botão laranja
b_18 = Button(frame_teclado, command =calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # fg cor do conteudo interno
b_18.place(x=177, y=208)


janela.mainloop()