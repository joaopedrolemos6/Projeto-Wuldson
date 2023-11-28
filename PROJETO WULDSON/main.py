#%%
from tkinter import *
from tkinter import ttk
import math

# Tamanho
janela = Tk()
janela.title("IMC")
janela.geometry("500x300")
janela.configure(bg='white')

# Orientação
txt_orientacao = Label(janela, text="Descubra seu IMC agora!!(índice de massa corporal)", font=('Arial 15'))
txt_orientacao.grid(column=1, row=1,)

txt_orientacao2 = Label(janela, text="Digite as informações a seguir...", pady=15, font=('Arial 10'))
txt_orientacao2.grid(column=1, row=2,)

# Pergunta altura
txt_orientacao3 = Label(janela, text="Qual sua altura?")
txt_orientacao3.grid(column=1, row=7, padx=0)
e_altura = Entry(janela)
e_altura.grid(row=8, column=1,)

# Pergunta peso
txt_orientacao4 = Label(janela, text="Qual seu peso?")
txt_orientacao4.grid(row=9, column=1)
e_peso = Entry(janela)
e_peso.grid(column=1, row=10)

#-----------------FORMULA CALCULAR-----

def calcular():
    try:
        peso = float(e_peso.get())
        altura = float(e_altura.get())
        resultado = peso / (altura ** 2)

        if resultado < 18.5:
            print("Abaixo do Peso Ideal")
        elif resultado >= 18.5 and resultado < 25:
            print("Peso Ideal")
        elif resultado >= 25 and resultado < 30:
            print("Acima do Peso Ideal ")
        else:
            print("Obesidade")
    except ValueError:
        print("Digite apenas números")

botao = Button(janela, text="calcular IMC", background='yellow', command=calcular)
botao.place(x=330, y=120)

janela.mainloop()
# %%
