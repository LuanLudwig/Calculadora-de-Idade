from tkinter import *
from tkinter import ttk
# importando tkvcalendar
from tkcalendar import Calendar, DateEntry
# importanto Date util
from dateutil.relativedelta import relativedelta
#importanto Date time
from datetime import date

# criando Jenela
janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry('310x400')

# cores
cor1 = "#3b3b3b" #cinza escuro
cor2 = "#473406" #laranja escuro
cor3 = "#ffffff" #branco

# criando Frames
frameCima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frameCima.grid(row=0, column=0)
frameBaixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cor2)
frameBaixo.grid(row=1, column=0)


# criando função para criar idade
def calcular():
    inicial = cal_1.get()
    termino = cal_2.get()

    
    
    # separando os valores das Datas, escaneando variaveis e separando valor para cada variavel.
    mesInicial, diaInicial, anoInicial = [int(f) for f in inicial.split('/')]
    data_inicial = date(anoInicial, mesInicial, diaInicial)

    mesTermino, diaTermino, anoTermino = [int(f) for f in termino.split('/')]
    data_nascimento = date(anoTermino, mesTermino, diaTermino)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    lappIdade['text'] = anos
    lappMesesIdade['text'] = meses
    lappDiasIdade['text'] = dias
    

# criando labels para o frame de cima

lCalculadora = Label(frameCima, text="CALCULADORA", width=25, height=1, padx=3, relief=FLAT, anchor=CENTER, font=('Monofur 15 bold'), bg=cor1, fg=cor3)
lCalculadora.place(x=0, y=30)

lCalculadora = Label(frameCima, text="DE IDADE", width=11, height=1, padx=0, relief=FLAT, anchor=CENTER, font=('Arial 35 bold'), bg=cor1, fg=cor3)
lCalculadora.place(x=0, y=70)

# criando labels para o frame de baixo
ldataInicial = Label(frameBaixo, text="Data Incial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Monofur 11 '), bg=cor2, fg=cor3)
ldataInicial.place(x=50, y=30)

cal_1 = DateEntry(frameBaixo, width=13, bg='darkblue', borderwidth=2, date_pattern='dd/mm/y', y=2023)
cal_1.place(x=170, y=30)

ldataNascimento = Label(frameBaixo, text="Data Nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Monofur 11 '), bg=cor2, fg=cor3)
ldataNascimento.place(x=50, y=60)

cal_2 = DateEntry(frameBaixo, width=13, bg='darkblue', borderwidth=2, date_pattern='dd/mm/y', y=2023)
cal_2.place(x=170, y=60)

lappIdade = Label(frameBaixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Monofur 25 bold '), bg=cor2, fg=cor3)
lappIdade.place(x=50, y=120)
lappAnos = Label(frameBaixo, text="Anos", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Monofur 11 bold '), bg=cor2, fg=cor3)
lappAnos.place(x=50, y=160)

lappMesesIdade = Label(frameBaixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Monofur 25 bold '), bg=cor2, fg=cor3)
lappMesesIdade.place(x=140, y=120)
lappMeses = Label(frameBaixo, text="Meses", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Monofur 11 bold '), bg=cor2, fg=cor3)
lappMeses.place(x=140, y=160)

lappDiasIdade = Label(frameBaixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Monofur 25 bold '), bg=cor2, fg=cor3)
lappDiasIdade.place(x=220, y=120)
lappDias = Label(frameBaixo, text="Dias", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Monofur 11 bold '), bg=cor2, fg=cor3)
lappDias.place(x=220, y=160)


# Criando Botões
bCalcular = Button(frameBaixo, command=calcular, text="Calcular", width=17, height=0, relief=RAISED, overrelief=RIDGE, font=('Monofur 15 bold '), bg=cor2, fg=cor3)
bCalcular.place(x=50, y=200)

janela.mainloop()