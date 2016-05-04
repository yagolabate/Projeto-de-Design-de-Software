# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

import ToolTip as ttp



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
        
        self.botao_massa = ttk.Button(self.pagina1, width=35)
        self.botao_massa.grid(row=3,column=0,sticky='ns')
        self.botao_massa.configure(text='Ganhar Massa')
        self.botao_massa.configure(command=self.clicar_GanharMassa)
        
        self.botao_emagrecer = ttk.Button(self.pagina1, width=35)
        self.botao_emagrecer.grid(row=3,column=1,sticky='ns')
        self.botao_emagrecer.configure(text='Emagrecer')
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
        self.lfrase.grid(row=2,column=2,columnspan=3, sticky='nsew')
        self.lfrase.configure(fg="black", text="Selecione seu nivel de atividade fisica:")
        
        
        self.mostrar1 = Image.open('sedentarismo.jpg').resize((150,100))
        self.plotar1 = ImageTk.PhotoImage(self.mostrar1)
        self.imagem1 = ttk.Button(self.pagina2,image = self.plotar1)
        self.imagem1.grid(row = 3, column = 1, sticky = 'nsew')
        
        
        self.mostrar2 = Image.open('levemente.jpg').resize((150,100))
        self.plotar2 = ImageTk.PhotoImage(self.mostrar2)
        self.imagem2 = ttk.Button(self.pagina2, image = self.plotar2)
        self.imagem2.grid(row = 3, column = 3, sticky = 'nsew')
        
        
        self.mostrar3 = Image.open('ativo.jpg').resize((150,100))
        self.plotar3 = ImageTk.PhotoImage(self.mostrar3)        
        self.imagem3 = ttk.Button(self.pagina2, image = self.plotar3)
        self.imagem3.grid(row = 3, column = 5, sticky = 'nsew')
        
        self.mostrar4 = Image.open('bastante ativo.jpg').resize((150,100))
        self.plotar4 = ImageTk.PhotoImage(self.mostrar4)
        self.imagem4 = ttk.Button(self.pagina2, image = self.plotar4)
        self.imagem4.grid(row = 5, column = 1, sticky = 'nsew')
        
        self.mostrar5 = Image.open('muito ativo.jpg').resize((150,100))
        self.plotar5 = ImageTk.PhotoImage(self.mostrar5)
        self.imagem5 = ttk.Button(self.pagina2, image = self.plotar5)
        self.imagem5.grid(row = 5, column =3, sticky = 'nsew')
    
        self.legenda1 = tk.Label(self.pagina2)
        self.legenda1.grid(row = 4, column = 1, sticky = '')
        self.legenda1.configure(fg = 'black', text = 'sedentário')
        ttp.CreateToolTip(self.legenda1, 'Pouco ou nenhum exercício diário.')
                       
        
        self.legenda2 = tk.Label(self.pagina2)
        self.legenda2.grid(row = 4, column = 3, sticky = '')
        self.legenda2.configure(fg = 'black', text = 'levemente ativo')
        ttp.CreateToolTip(self.legenda2, 'Exercício leve/1 a 3 dias por semana.')
        
        self.legenda3 = tk.Label(self.pagina2)
        self.legenda3.grid(row = 4, column = 5, sticky = '')
        self.legenda3.configure(fg = 'black', text = 'moderamente ativo')
        ttp.CreateToolTip(self.legenda3, 'Exercício moderado/3 a 5 dias por semana')
        
        self.legenda4 = tk.Label(self.pagina2)
        self.legenda4.grid(row = 6, column = 1, sticky = 'nsew')
        self.legenda4.configure(fg = 'black', text = 'muito ativo')
        ttp.CreateToolTip(self.legenda4, 'Exercício intenso/ 6 a 7 dias na semana')        
        
        self.legenda5 = tk.Label(self.pagina2)
        self.legenda5.grid(row = 6, column = 3, sticky = 'nsew')
        self.legenda5.configure(fg = 'black', text = 'extremamente ativo')
        ttp.CreateToolTip(self.legenda5, 'Exercício intenso todos os dias da semana ou com treinos bi-diários')
        
        self.botao_voltar_pag1 = ttk.Button(self.pagina2,width=20)
        self.botao_voltar_pag1.grid(row=6,column=5,sticky='se')
        self.botao_voltar_pag1.configure(text="Voltar")
        self.botao_voltar_pag1.configure(command=self.pagina1.tkraise)
        
        
        #terceira frame
        
        self.pagina3 = tk.Frame(self.window)
        
        self.pagina3.rowconfigure(0, minsize = 75)
        self.pagina3.rowconfigure(1, minsize = 75)
        self.pagina3.rowconfigure(2, minsize = 75)
        self.pagina3.rowconfigure(3, minsize = 75)
        self.pagina3.rowconfigure(4, minsize = 75)
        self.pagina3.rowconfigure(5, minsize = 75)
        self.pagina3.rowconfigure(6, minsize = 150)
        self.pagina3.columnconfigure(0, minsize = 150)
        self.pagina3.columnconfigure(1, minsize = 150)
        self.pagina3.columnconfigure(2, minsize = 150)
        self.pagina3.columnconfigure(3, minsize = 150)
        self.pagina3.columnconfigure(4, minsize = 150)
        self.pagina3.columnconfigure(5, minsize = 150)
        
        
        self.frase_1 = ttk.Label(self.pagina3)
        self.frase_1.grid(row = 0, column = 0, sticky = 'nsw')
        self.frase_1.configure(text = "Quantidades a serem consumidas:")
        
        self.carboidrato = ttk.Label(self.pagina3)
        self.carboidrato.grid(row = 1, column = 0, sticky = 'nse')
        self.carboidrato.configure(text = "Carboidratos:")
        
        self.total_carbo = ttk.Label(self.pagina3)
        self.total_carbo.grid(row = 1, column = 1, sticky = 'nswe')
        self.total_carbo.configure(text= self.CalculaCarbo())
        
        self.proteina = ttk.Label(self.pagina3)
        self.proteina.grid(row = 1, column = 2, sticky = 'nse')
        self.proteina.configure(text = "Proteínas:")
        
        self.total_proteina = ttk.Label(self.pagina3)
        self.total_proteina.grid(row = 1, column = 3, sticky = 'nswe')
        self.total_proteina.configure(text= self.CalculaProteina())
        
        self.gordura = ttk.Label(self.pagina3)
        self.gordura.grid(row = 1, column = 4, sticky = 'nse')
        self.gordura.configure(text = "Gorduras:")
        
        self.total_gordura = ttk.Label(self.pagina3)
        self.total_gordura.grid(row = 1, column = 5, sticky = 'nswe')
        self.total_gordura.configure(text= self.CalculaGordura())
        
        self.frase_2 = ttk.Label(self.pagina3)
        self.frase_2.grid(row = 2, column = 0, sticky = 'nsw')
        self.frase_2.configure(text = "Quantidades já consumidas:")
        
        self.carboidrato_2 = ttk.Label(self.pagina3)
        self.carboidrato_2.grid(row = 3, column = 0, sticky = 'nse')
        self.carboidrato_2.configure(text = "Carboidratos:")
        
        self.consumo_carbo = ttk.Label(self.pagina3)
        self.consumo_carbo.grid(row = 3, column = 1, sticky = 'nswe')
        self.consumo_carbo.configure(text= self.ConsumoCarbo())
        
        self.proteina_2 = ttk.Label(self.pagina3)
        self.proteina_2.grid(row = 3, column = 2, sticky = 'nse')
        self.proteina_2.configure(text = "Proteínas:")
        
        self.consumo_proteina = ttk.Label(self.pagina3)
        self.consumo_proteina.grid(row = 3, column = 3, sticky = 'nswe')
        self.consumo_proteina.configure(text= self.ConsumoProteina())
        
        self.gordura_2 = ttk.Label(self.pagina3)
        self.gordura_2.grid(row = 3, column = 4, sticky = 'nse')
        self.gordura_2.configure(text = "Gorduras:")
        
        self.consumo_gordura = ttk.Label(self.pagina3)
        self.consumo_gordura.grid(row = 3, column = 5, sticky = 'nswe')
        self.consumo_gordura.configure(text= self.ConsumoGordura())
        
        self.frase_3 = ttk.Label(self.pagina3)
        self.frase_3.grid(row = 4, column = 0, sticky = 'nsw')
        self.frase_3.configure(text = "Alimentos consumidos:")
        
        self.ad_alimento = ttk.Label(self.pagina3)
        self.ad_alimento.grid(row = 5, column = 0, columnspan = 1, sticky = 'nswe')
        self.ad_alimento.configure(text = "Adicione um alimento:")
        
        self.entry_ad = ttk.Entry(self.pagina3)
        self.entry_ad.grid(row = 5, column = 1)
        
        self.quan_alimento = ttk.Label(self.pagina3)
        self.quan_alimento.grid(row = 5, column = 3, columnspan = 1, sticky = 'nswe')
        self.quan_alimento.configure(text = "Quantidade do alimento(g):")
        
        self.entry_quan = ttk.Entry(self.pagina3)
        self.entry_quan.grid(row = 5, column = 4)
        
        self.alimentos_ad = ttk.Scrollbar(self.pagina3, orient = 'vertical')
        self.alimentos_ad.grid(row = 6, column = 0, columnspan = 5, sticky = 'nswe')
        
    
        
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
        
    def CalculaCarbo(self):
        return 0
        
    def CalculaProteina(self):
        return 0
        
    def CalculaGordura(self):
        return 0
        
    def ConsumoCarbo(self):
        return 0
        
    def ConsumoProteina(self):
        return 0
        
    def ConsumoGordura(self):
        return 0
        

        
        
    
        
app = Projeto_Final()
app.iniciar()