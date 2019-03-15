# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:35:34 2019

@author: Cristiano Teixeira
"""

from tkinter import *

window = Tk()
window.title("Jogo da Velha")
window.geometry('240x240')
tabela=[" "," "," ",
        " "," "," ",
        " "," "," ",]
j=["X"]
vez=["Jogador 1"]
vencedor=["empate"]

def click1():
    if (tabela[0]==" "):
        del tabela[0]
        tabela.insert(0, j[0])
        bt1.configure(text= tabela[0])
        alterna()
def click2():
    if (tabela[1]==" "):
        del tabela[1]
        tabela.insert(1, j[0])
        bt2.configure(text= tabela[1])
        alterna()
def click3():
    if (tabela[2]==" "):
        del tabela[2]
        tabela.insert(2, j[0])
        bt3.configure(text= tabela[2])
        alterna()
def click4():
    if (tabela[3]==" "):
        del tabela[3]
        tabela.insert(3, j[0])
        bt4.configure(text= tabela[3])
        alterna()
        
def click5():
    if (tabela[4]==" "):
        del tabela[4]
        tabela.insert(4, j[0])
        bt5.configure(text= tabela[4])
        alterna()
def click6():
    if (tabela[5]==" "):
        del tabela[5]
        tabela.insert(5,j[0])
        bt6.configure(text= tabela[5])
        alterna()
def click7():
    if (tabela[6]==" "):
        del tabela[6]
        tabela.insert(6,j[0])
        bt7.configure(text= tabela[6])
        alterna()
def click8():
    if (tabela[7]==" "):
        del tabela[7]
        tabela.insert(7,j[0])
        bt8.configure(text= tabela[7])
        alterna()
def click9():
   if (tabela[8]==" "):
        del tabela[8]
        tabela.insert(8,j[0])
        bt9.configure(text= tabela[8])
        alterna()

def alterna():
    if (j[0]=="X"):
        del j[0]
        j.insert(0,"O")
        del vez[0]
        vez.insert(0,"Jogador 2")
    else:
        del j[0]
        j.insert(0,"X")
        del vez[0]
        vez.insert(0,"Jogador 1")
    label1.configure(text="Vez "+vez[0])
    verifica()
        

def verifica():
    
    '''verifica a primeira linha'''
    if(tabela[0]==tabela[1] and tabela[1]==tabela[2] and tabela[2]!=" "):
        if(tabela[0]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[0]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    '''verifica a segunda linha''' 
    if(tabela[3]==tabela[4] and tabela[4]==tabela[5] and tabela[5]!=" "):
        if(tabela[3]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[3]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    '''verifica a terceira linha'''
    if(tabela[6]==tabela[7] and tabela[7]==tabela[8] and tabela[8]!=" "):
        if(tabela[6]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[6]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    
    '''verifica a primeira coluna'''
    if(tabela[0]==tabela[3] and tabela[3]==tabela[6] and tabela[6]!=" "):
        if(tabela[0]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[0]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    '''verifica a segunda coluna''' 
    if(tabela[1]==tabela[4] and tabela[4]==tabela[7] and tabela[7]!=" "):
        if(tabela[1]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[1]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    '''verifica a terceira coluna'''
    if(tabela[2]==tabela[5] and tabela[5]==tabela[8] and tabela[8]!=" "):
        if(tabela[2]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[2]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    '''verifica a diagonal superior esquerda'''
    if(tabela[0]==tabela[4] and tabela[4]==tabela[8] and tabela[8]!=" "):
        if(tabela[0]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[0]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    '''verifica a diagonal superior esquerda'''
    if(tabela[2]==tabela[4] and tabela[4]==tabela[6] and tabela[6]!=" "):
        if(tabela[2]=="X"):
            del vencedor[0]
            vencedor.insert(0, "Jogador 1 com X")
            fimdejogo()
        else:
            if (tabela[2]=="O"):
                del vencedor[0]
                vencedor.insert(0, "Jogador 2 com O")
                fimdejogo()
    if(tabela[0]!=" " and tabela[2]!=" " and tabela[3]!=" "and tabela[4]!=" " and tabela[5]!=" " and tabela[6]!=" " and tabela[7]!=" " and tabela[8]!=" "):
        fimdejogo()
        
def fimdejogo():
    
    messagebox.showinfo('Fim de Jogo: ', 'O Vencedor é: '+ vencedor[0])

label1=Label(window, text="Vez "+vez[0])
label1.grid(column=0, row=0)    
bt1 = Button(window, text=" 1 ", width=10, height=4, command=click1)
bt1.grid(column=0, row=1)
bt2 = Button(window, text="  2 ", width=10, height=4, command=click2)
bt2.grid(column=1, row=1)
bt3 = Button(window, text=" 3 ", width=10, height=4,command=click3)
bt3.grid(column=2, row=1)
bt4 = Button(window, text="  4 ", width=10, height=4,command=click4)
bt4.grid(column=0, row=2)
bt5 = Button(window, text=" 5 ", width=10, height=4,command=click5)
bt5.grid(column=1, row=2)
bt6 = Button(window, text="  6 ", width=10, height=4,command=click6)
bt6.grid(column=2, row=2)
bt7 = Button(window, text=" 7 ", width=10, height=4,command=click7)
bt7.grid(column=0, row=3)
bt8 = Button(window, text="  8 ", width=10, height=4,command=click8)
bt8.grid(column=1, row=3)
bt9 = Button(window, text=" 9 ", width=10, height=4,command=click9)
bt9.grid(column=2, row=3)


window.mainloop()
