import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import *
import time
import os

class Tela:

    def __init__(self, master):


        
        cab = tk.Label(janela, text="Reposição WhatsApp")
        cab["font"] = ("Lucida", "30", "italic", "bold")
        
        cab.place(x=170, y=35)

        borracha = tk.PhotoImage(file="borracha.png")
        self.imgg = tk.Label(janela, image=borracha)
        self.imgg.borracha = borracha
        self.imgg.place(x=675, y=137)
        self.imgg.bind("<Button-1>", self.bor1)

        borracha2 = tk.PhotoImage(file="borracha.png")
        self.imgg2 = tk.Label(janela, image=borracha2)
        self.imgg2.borracha2 = borracha2
        self.imgg2.place(x=675, y=210)
        self.imgg2.bind("<Button-1>", self.bor2)

        borracha3 = tk.PhotoImage(file="borracha.png")
        self.imgg3 = tk.Label(janela, image=borracha3)
        self.imgg3.borracha3 = borracha3
        self.imgg3.place(x=675, y=270)
        self.imgg3.bind("<Button-1>", self.bor3)

        borracha4 = tk.PhotoImage(file="borracha.png")
        self.imgg4 = tk.Label(janela, image=borracha4)
        self.imgg4.borracha4 = borracha4
        self.imgg4.place(x=675, y=370)
        self.imgg4.bind("<Button-1>", self.bor4)

        borracha5 = tk.PhotoImage(file="borracha.png")
        self.imgg5 = tk.Label(janela, image=borracha5)
        self.imgg5.borracha5 = borracha5
        self.imgg5.place(x=675, y=447)
        self.imgg5.bind("<Button-1>", self.bor5)

        borracha6 = tk.PhotoImage(file="borracha.png")
        self.imgg6 = tk.Label(janela, image=borracha6)
        self.imgg6.borracha6 = borracha6
        self.imgg6.place(x=675, y=510)
        self.imgg6.bind("<Button-1>", self.bor6)



        self.nome = tk.Label(janela, text="Aluno:")
        self.nome["font"] = ("Helvetica", "16")
        self.nome.place(x=100, y=140)

        self.nomeE = tk.Entry(janela)
        self.nomeE["font"] = ("Helvetica", "16")
        self.nomeE.config(bg="#C0C0C0", foreground="#363636")
        self.nomeE.place(x=170, y=142, width=500)

        self.ctr = tk.Label(janela, text="CTR:")
        self.ctr["font"] = ("Helvetica", "16")
        self.ctr.place(x=110, y=210)

        self.ctrE = tk.Entry(janela)
        self.ctrE["font"] = ("Helvetica", "16")
        self.ctrE.config(bg="#C0C0C0", foreground="#363636")
        self.ctrE.place(x=170, y=212, width=100)

        self.turma = tk.Label(janela, text="Cód. Turma:")
        self.turma["font"] = ("Helvetica", "16")
        self.turma.place(x=360, y=210)

        self.turmaE = tk.Entry(janela)
        self.turmaE["font"] = ("Helvetica", "16")
        self.turmaE.config(bg="#C0C0C0", foreground="#363636")
        self.turmaE.place(x=490, y=212, width=180)

        self.prof = tk.Label(janela, text="Professor:")
        self.prof["font"] = ("Helvetica", "16")
        self.prof.place(x=60, y=270)

        professores=["Analice", "Eduardo", "Henrique", "João", "Kathlen", "Leonardo Alves", "Leonardo Mendes"]
        self.profE = ttk.Combobox(janela, values=professores)
        self.profE["font"] = ("Helvetica", "16")
        self.profE.place(x=170, y=272, width=180)

        self.curso = tk.Label(janela, text="Curso:")
        self.curso["font"] = ("Helvetica", "16")
        self.curso.place(x=415, y=270)

        cursos=["Hardware", "Informática", "Informática com Gestão Administrativa","Gestão Administrativa com Liderança", "Inglês"]
        self.cursoE = ttk.Combobox(janela, values=cursos)
        self.cursoE["font"] = ("Helvetica", "16")
        self.cursoE.place(x=490, y=272, width=180)
        
        self.modulo = tk.Label(janela, text="Módulo:")
        self.modulo["font"] = ("Helvetica", "16")
        self.modulo.place(x=70, y=370)

        self.moduloE = ttk.Combobox(janela, values="")
        self.moduloE["font"] = ("Helvetica", "16")
        self.moduloE.place(x=160, y=372, width=190)


        self.moduloE = tk.Entry(janela)
        self.moduloE["font"] = ("Helvetica", "16")
        self.moduloE.config(bg="#C0C0C0", foreground="#363636")
        self.moduloE.place(x=160, y=372, width=190)


        self.motivo = tk.Label(janela, text="Motivo:")
        self.motivo["font"] = ("Helvetica", "16")
        self.motivo.place(x=390, y=370)

        motivos=["Aluno(a) faltou", "Plantão de dúvidas"]
        self.motivoE = ttk.Combobox(janela, values=motivos)
        self.motivoE["font"] = ("Helvetica", "16")
        self.motivoE.place(x=470, y=372, width=200)

        self.data = tk.Label(janela, text="Aluno faltou em:")
        self.data["font"] = ("Helvetica", "16")
        self.data.place(x=10, y=450)

        self.dataF = DateEntry(janela, values=motivos, locale="pt_BR")
        self.dataF["font"] = ("Helvetica", "16")
        self.dataF.place(x=170, y=452, width=140)
        
        self.mais = tk.Label(janela, text="+")
        self.mais["font"] = ("Arial", "15")
        self.mais.config(bg="green", foreground="white")
        self.mais.place(x=312, y=452)
        self.mais.bind("<Button-1>", self.maiss)
        

        self.repor = tk.Label(janela, text="Data da reposição:")
        self.repor["font"] = ("Helvetica", "16")
        self.repor.place(x=340, y=450)

        self.dataR = DateEntry(janela, values=motivos, locale="pt_BR")
        self.dataR["font"] = ("Helvetica", "16")
        self.dataR.place(x=530, y=452, width=140)

        self.hor = tk.Label(janela, text="Horário:")
        self.hor["font"] = ("Helvetica", "16")
        self.hor.place(x=400, y=510)

        self.horE = tk.Entry(janela)
        self.horE["font"] = ("Helvetica", "16")
        self.horE.config(bg="#C0C0C0", foreground="#363636")
        self.horE.place(x=490, y=512, width=180)
        

        self.bt1 = tk.Button(janela, text="Gerar")
        self.bt1["font"] = ("Helvetica", "17")
        self.bt1.config(bg="#006400", foreground="white")
        self.bt1.place(x=440, y=610)
        self.bt1.bind("<Button-1>", self.gerar)

        self.bt1 = tk.Button(janela, text="Limpar")
        self.bt1["font"] = ("Helvetica", "17")
        self.bt1.config(bg="#8B0000", foreground="white")
        self.bt1.place(x=230, y=610)
        self.bt1.bind("<Button-1>", self.limpar)

        
    def maiss(self, event):

        motivos=["Aluno(a) faltou", "Plantão de dúvidas"]
        self.dataF2 = DateEntry(janela, values=motivos, locale="pt_BR")
        self.dataF2["font"] = ("Helvetica", "16")
        self.dataF2.place(x=170, y=490, width=140)
        

    def bor1(self, event):

        self.nomeE.delete(0, "end")
        

    def bor2(self, event):

        self.ctrE.delete(0, "end")

        self.turmaE.delete(0, "end")

    def bor3(self, event):

        self.profE.delete(0, "end")

        self.cursoE.delete(0, "end")

    def bor4(self, event):

        self.moduloE.delete(0, "end")

        self.motivoE.delete(0, "end")

    def bor5(self, event):

        self.dataF.delete(0, "end")

        self.dataR.delete(0, "end")

    def bor6(self, event):

        self.horE.delete(0, "end")

       


    def gerar(self, event):

        nome = self.nomeE.get()
        ctr = self.ctrE.get()
        turma = self.turmaE.get()
        modulo = self.moduloE.get()
        curso = self.cursoE.get()
        motivo = self.motivoE.get()
        data = self.dataR.get()
        falta = self.dataF.get()
        horario = self.horE.get()
        professor = self.profE.get()

        janela2 = tk.Tk()
        janela2.geometry("800x700+100+20")
        janela2.config(bg="white")
        janela2.title("Tirar Print")

        cab2 = tk.PhotoImage(master=janela2,file="cab2.png")
        self.imgg = tk.Label(janela2, image=cab2)
        self.imgg.cab2 = cab2
        self.imgg.place(x=215, y=5)

        self.lb = tk.Label(janela2, text= "PROFESSOR QUE MINISTRARÁ A REPOSIÇÃO: "+professor)
        self.lb["font"] = ("Arial black", "16")
        self.lb.config(bg="white")
        self.lb.place(x=50, y=180)

        self.lb2 = tk.Label(janela2, text= "ALUNO(A): "+nome)
        self.lb2["font"] = ("Arial black", "16")
        self.lb2.config(bg="white")
        self.lb2.place(x=50, y=230)

        self.lb3 = tk.Label(janela2, text= "CTR: "+ctr)
        self.lb3["font"] = ("Arial black", "16")
        self.lb3.config(bg="white")
        self.lb3.place(x=550, y=230)

        self.lb4 = tk.Label(janela2, text= "DATA: "+data)
        self.lb4["font"] = ("Arial black", "16")
        self.lb4.config(bg="white")
        self.lb4.place(x=50, y=290)

        self.lb5 = tk.Label(janela2, text= "das  "+horario)
        self.lb5["font"] = ("Arial black", "16")
        self.lb5.config(bg="white")
        self.lb5.place(x=270, y=290)

        self.lb6 = tk.Label(janela2, text= "DADOS DO CURSO:")
        self.lb6["font"] = ("Arial black", "16")
        self.lb6.config(bg="white")
        self.lb6.place(x=50, y=390)

        self.lb7 = tk.Label(janela2, text= "Curso: "+curso)
        self.lb7["font"] = ("Times new roman", "20")
        self.lb7.config(bg="white")
        self.lb7.place(x=150, y=440)

        self.lb8 = tk.Label(janela2, text= "Turma: "+turma)
        self.lb8["font"] = ("Times new roman", "20")
        self.lb8.config(bg="white")
        self.lb8.place(x=150, y=480)

        self.lb9 = tk.Label(janela2, text= "Módulo: "+modulo)
        self.lb9["font"] = ("Times new roman", "20")
        self.lb9.config(bg="white")
        self.lb9.place(x=150, y=520)

        self.lb10 = tk.Label(janela2, text= "Motivo da reposição:  "+motivo)
        self.lb10["font"] = ("Arial black", "18")
        self.lb10.config(bg="white", foreground="darkred")
        self.lb10.place(x=50, y=580)


        self.lb11 = tk.Label(janela2, text= "em  "+falta)
        self.lb11["font"] = ("Arial black", "18")
        self.lb11.config(bg="white", foreground="darkred")
        self.lb11.place(x=565, y=580)

        janela2.resizable(width=False, height=False)
        

    
        
        
        
        
        janela2.mainloop()

    def limpar(self, event):

        self.nomeE.delete(0, "end")
        self.ctrE.delete(0, "end")
        self.turmaE.delete(0, "end")
        self.moduloE.delete(0, "end")
        self.cursoE.delete(0, "end")
        self.motivoE.delete(0, "end")
        self.dataR.delete(0, "end")
        self.horE.delete(0, "end")
        self.profE.delete(0, "end")
        self.dataF.delete(0, "end")
    

janela = tk.Tk()
Tela(janela)
janela.title("Reposição de aula")
janela.geometry("750x700+100+10")
janela.resizable(width=False, height=False)
janela.mainloop()
