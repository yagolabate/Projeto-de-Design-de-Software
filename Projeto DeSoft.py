# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk



class Projeto_Final:
    
    
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Projeto final")
        self.window.geometry('900x600+220+50')
        self.window.rowconfigure(0, minsize = 600)
        self.window.columnconfigure(0, minsize = 900)
        self.window.grid()
        
        self.objetivo_escolhido = 0
        
        # primeiro frame
        
        self.pagina1 = tk.Frame(self.window)
        self.pagina1.rowconfigure(0, minsize = 100)
        self.pagina1.rowconfigure(1, minsize = 100)
        self.pagina1.rowconfigure(2, minsize = 300)
        self.pagina1.rowconfigure(3, minsize = 50)
        self.pagina1.columnconfigure(0, minsize = 450)
        self.pagina1.columnconfigure(1, minsize = 450)
        self.pagina1.grid(row=0, column=0, sticky="nsew")
        
        self.Bem_vindo = tk.Label(self.pagina1)
        self.Bem_vindo.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.Bem_vindo.configure(text='Bem vindo ao ..', font = 50)
        
        self.objetivo = tk.Label(self.pagina1)
        self.objetivo.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.objetivo.configure(text='Escolha o seu objetivo:', font = 50)
        
        
        self.massa = Image.open('ganhar-massa.jpg').resize((320,250))
        self.load_massa = ImageTk.PhotoImage(self.massa)
        self.label = tk.Label(self.pagina1,image=self.load_massa)
        self.label.grid(row=2,column=0,sticky='nsew')    
        
        
        self.emagrecer = Image.open('emagrecer.jpg').resize((320,250))
        self.load_emagrecer = ImageTk.PhotoImage(self.emagrecer)
        self.label = tk.Label(self.pagina1,image=self.load_emagrecer)
        self.label.grid(row=2,column=1,sticky='nsew')  
        
        self.botao_massa = tk.Button(self.pagina1, width=35)
        self.botao_massa.grid(row=3,column=0,sticky='ns')
        self.botao_massa.configure(text='Ganhar Massa', font = 50)
        self.botao_massa.configure(command=self.clicar_GanharMassa)
        
        self.botao_emagrecer = tk.Button(self.pagina1, width=35)
        self.botao_emagrecer.grid(row=3,column=1,sticky='ns')
        self.botao_emagrecer.configure(text='Emagrecer', font = 50)
        self.botao_emagrecer.configure(command=self.clicar_Emagrecer)
        
        
        #segunda frame
        
        self.pagina2 = tk.Frame(self.window)
        self.pagina2.rowconfigure(0,minsize = 60)
        self.pagina2.rowconfigure(1,minsize = 70)
        self.pagina2.rowconfigure(2,minsize = 70)
        self.pagina2.rowconfigure(3,minsize = 70)
        self.pagina2.rowconfigure(4,minsize = 60) 
        self.pagina2.rowconfigure(5,minsize = 100)
        self.pagina2.rowconfigure(6,minsize = 100)     
        
        
        self.pagina2.columnconfigure(0,minsize = 100)
        self.pagina2.columnconfigure(1,minsize = 100)
        self.pagina2.columnconfigure(2,minsize = 100)
        self.pagina2.columnconfigure(3,minsize = 100)
        self.pagina2.columnconfigure(4,minsize = 100)
        self.pagina2.columnconfigure(5,minsize = 100)
        self.pagina2.grid(row=0, column=0, sticky="nsew")
        
        
        
        
        self.lgenero = tk.Label(self.pagina2)
        self.lgenero.grid(row=0, column = 0, sticky = 'nse')
        self.lgenero.configure(fg='black', text = "Gênero:")
        
        self.combo = ttk.Combobox(self.pagina2)
        self.combo.grid(row = 0, column = 1)
        
        
        self.combo['values'] = ['Masculino', 'Feminino']
        
        
        self.bpeso = tk.Entry(self.pagina2)
        self.bpeso.grid(row = 1, column = 1, sticky = 'ew')     
                
        
        self.lpeso = tk.Label(self.pagina2)
        self.lpeso.grid(row=1, column=0,sticky="nse")
        self.lpeso.configure(fg='black', text = 'Peso(Kg):')
        
        
        
        self.laltura = tk.Label(self.pagina2)
        self.laltura.grid(row=1, column=2, sticky = 'nse')
        self.laltura.configure(fg='black', text = 'Altura(cm):')
        
        self.baltura = tk.Entry(self.pagina2)
        self.baltura.grid(row=1, column=3, sticky='ew')       
        
        
        
        
        self.lidade = tk.Label(self.pagina2)
        self.lidade.grid(row=1, column=4, sticky = 'nse')
        self.lidade.configure(fg='black', text = 'Idade:')
        
        self.bidade = tk.Entry(self.pagina2)
        self.bidade.grid(row = 1, column = 5, sticky = 'ew' )
        
        
        
        self.lfrase = tk.Label(self.pagina2)
        self.lfrase.grid(row=2,column=2,columnspan=4, sticky='nsew')
        self.lfrase.configure(fg="black", text="Selecione seu nivel de atividade fisica:")
        
        
        self.mostrar1 = Image.open('sedentarismo.jpg').resize((150,100))
        self.plotar1 = ImageTk.PhotoImage(self.mostrar1)
        self.imagem1 = ttk.Button(self.pagina2,image = self.plotar1)
        self.imagem1.grid(row = 3, column = 0, sticky = 'nsew')
        
        
        self.mostrar2 = Image.open('levemente.jpg').resize((150,100))
        self.plotar2 = ImageTk.PhotoImage(self.mostrar2)
        self.imagem2 = ttk.Button(self.pagina2, image = self.plotar2)
        self.imagem2.grid(row = 3, column = 2, sticky = 'nsew')
        
        
        self.mostrar3 = Image.open('ativo.jpg').resize((150,100))
        self.plotar3 = ImageTk.PhotoImage(self.mostrar3)        
        self.imagem3 = ttk.Button(self.pagina2, image = self.plotar3)
        self.imagem3.grid(row = 3, column = 6, sticky = 'nsew')
        
        self.mostrar4 = Image.open('bastante ativo.jpg').resize((150,100))
        self.plotar4 = ImageTk.PhotoImage(self.mostrar4)
        self.imagem4 = ttk.Button(self.pagina2, image = self.plotar4)
        self.imagem4.grid(row = 5, column = 0, sticky = 'nsew')
        
        self.mostrar5 = Image.open('muito ativo.jpg').resize((150,100))
        self.plotar5 = ImageTk.PhotoImage(self.mostrar5)
        self.imagem5 = ttk.Button(self.pagina2, image = self.plotar5)
        self.imagem5.grid(row = 5, column =2, sticky = 'nsew')
    
        self.legenda1 = tk.Label(self.pagina2)
        self.legenda1.grid(row = 4, column = 0, sticky = 'nsew')
        self.legenda1.configure(fg = 'black', text = 'sedentário')
        
        self.legenda2 = tk.Label(self.pagina2)
        self.legenda2.grid(row = 4, column = 2, sticky = 'nsew')
        self.legenda2.configure(fg = 'black', text = 'levemente ativo')
        
        self.legenda3 = tk.Label(self.pagina2)
        self.legenda3.grid(row = 4, column = 6, sticky = 'nsew')
        self.legenda3.configure(fg = 'black', text = 'moderamente ativo')
        
        self.legenda4 = tk.Label(self.pagina2)
        self.legenda4.grid(row = 6, column = 0, sticky = 'nsew')
        self.legenda4.configure(fg = 'black', text = 'muito ativo')
        
        self.legenda5 = tk.Label(self.pagina2)
        self.legenda5.grid(row = 6, column = 2, sticky = 'nsew')
        self.legenda5.configure(fg = 'black', text = 'extremamente ativo')
        
        self.botao_voltar_pag1 = ttk.Button(self.pagina2,width=20)
        self.botao_voltar_pag1.grid(row=6,column=6,sticky='se')
        self.botao_voltar_pag1.configure(text="Voltar")
        self.botao_voltar_pag1.configure(command=self.pagina1.tkraise)
        
        
    
        

        
        #Chamando a primeira frame
        self.pagina1.tkraise() 
       
    def iniciar(self):
        self.window.mainloop()
        
    def clicar_GanharMassa(self):
        self.objetivo_escolhido = 1
        self.pagina2.tkraise()
        
    def clicar_Emagrecer(self):
        self.objetivo_escolhido = 2
        self.pagina2.tkraise()
        
        
        
        
    
        
app = Projeto_Final()
app.iniciar()