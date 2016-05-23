# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import comidas
import pickle

import ToolTip as ttp
#from firebase import firebase
#firebase = firebase.FirebaseApplication('https://projeto-de-desoft.firebaseio.com/')

class Projeto_Final:
    
    
    def __init__(self):
        
                
        self.window = tk.Tk()
        
        self.window.protocol("WM_DELETE_WINDOW", self.terminar)
        
        self.window.title("Projeto final")
        self.window.geometry('900x600+220+50')
        self.window.rowconfigure(0, minsize = 600)
        self.window.columnconfigure(0, minsize = 900)
        self.window.grid()
        
        
        self.objetivo_escolhido = tk.StringVar()
        self.peso = tk.StringVar()
        self.altura = tk.StringVar()
        self.idade = tk.StringVar()        
        self.cc = tk.StringVar()
        self.cg = tk.StringVar()
        self.cp = tk.StringVar()
        self.alimento = tk.StringVar()
        self.quantidade = tk.StringVar()
        self.carbo_consumidos = tk.StringVar()
        self.prot_consumidos = tk.StringVar()
        self.gordura_consumidos = tk.StringVar()
        self.c = tk.StringVar()
        self.p = tk.StringVar()
        self.g = tk.StringVar()
        
        arquivo = open("projeto.pickle", "rb")
        self.dici = pickle.load(arquivo)
        
        self.inicio = self.dici['iniciar']
        
        self.variavel_carbo_consumido = 0
        self.variavel_carbo_consumido += self.dici['carboidratos consumidas']
        self.variavel_prot_consumido = 0
        self.variavel_prot_consumido += self.dici['proteina consumidos']
        self.variavel_gord_consumido = 0  
        self.variavel_gord_consumido += self.dici['gordura consumidos']
        
        self.ultimo_alimento_carbo = tk.StringVar()
        self.ultimo_alimento_prot = tk.StringVar()
        self.ultimo_alimento_gord = tk.StringVar()


        self.genero = tk.StringVar()

        self.combo_value = tk.StringVar()
        
        self.window.iconbitmap(self, default='ganhar-massa.ico')
        
        self.comidas = comidas.ler_dicionario_comidas()

        self.categorias_comida = [c for c in self.comidas]
        self.categorias_comida.sort()
        self.categoria_comida_inicial = self.categorias_comida[0]
        
        self.comidas_na_categoria = [c for c in self.comidas[self.categoria_comida_inicial]]
        self.comida_inicial = self.comidas_na_categoria[0]    
        

        
        self.lista_alimentos_consumidos = []
        
        #cadastro de usuario
        
        
        
        self.pagina0 = tk.Frame(self.window)
        self.pagina0.rowconfigure(0, minsize = 250)
        self.pagina0.rowconfigure(1, minsize = 50)
        self.pagina0.rowconfigure(2, minsize = 50)
        self.pagina0.rowconfigure(3, minsize = 200)
        self.pagina0.rowconfigure(4, minsize = 50)
        self.pagina0.columnconfigure(0 ,minsize = 400)
        self.pagina0.columnconfigure(1, minsize = 500)
        self.pagina0.grid(row=0,column=0, sticky="nsew")
        self.pagina0.configure(background = 'light blue')
        
        self.ltitulo = ttk.Label(self.pagina0)
        self.ltitulo.grid(row = 0, columnspan = 2, sticky = '')
        self.ltitulo.configure(text = 'Bem vindo ao nosso programa:', font = 100, background = 'light blue')
        
        self.llogin = ttk.Label(self.pagina0)
        self.llogin.grid(row = 1, column = 0, sticky = 'e')
        self.llogin.configure(text = "Login:", background = 'light blue')
        
        self.blogin = ttk.Entry(self.pagina0)
        self.blogin.grid(row = 1, column = 1, sticky = 'w')
        
        self.lsenha = ttk.Label(self.pagina0)
        self.lsenha.grid(row = 2, column = 0, sticky = 'e')
        self.lsenha.configure(text = "Senha:", background = 'light blue')
        
        self.bsenha = ttk.Entry(self.pagina0)
        self.bsenha.grid(row = 2, column = 1, sticky = 'w')
        
        self.bseguinte = ttk.Button(self.pagina0)
        self.bseguinte.grid(row = 4, column = 1, sticky = 'e')
        self.bseguinte.configure(text = "Seguinte", )
        self.bseguinte.configure(command = self.clicar_seguinte)
        
        self.ir_pagina_3 = tk.Button(self.pagina0)
        self.ir_pagina_3.grid(row=4,column=0,sticky="nsew")
        self.ir_pagina_3.configure(text="PAGINA 3")
        self.ir_pagina_3.configure(command=self.irpagina3)
        
        
        
        
        
        
        
        # primeiro frame
        
        
        self.pagina1 = tk.Frame(self.window)
        self.pagina1.rowconfigure(0, minsize = 100)
        self.pagina1.rowconfigure(1, minsize = 100)
        self.pagina1.rowconfigure(2, minsize = 300)
        self.pagina1.rowconfigure(3, minsize = 50)
        self.pagina1.columnconfigure(0, minsize = 450)
        self.pagina1.columnconfigure(1, minsize = 450)
        self.pagina1.grid(row=0, column=0, sticky="nsew")
        self.pagina1.configure(background = 'light blue')
        
        
        
        
        self.objetivo = tk.Label(self.pagina1)
        self.objetivo.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.objetivo.configure(text='Escolha o seu objetivo:', font = 50, background = 'light blue')
        
        
        self.massa = Image.open('ganhar-massa.jpg').resize((320,250))
        self.load_massa = ImageTk.PhotoImage(self.massa)
        self.label = tk.Label(self.pagina1,image=self.load_massa)
        self.label.grid(row=2,column=0,sticky='nsew')  
        self.label.configure(background = 'light blue')
        
        
        self.emagrecer = Image.open('emagrecer.jpg').resize((320,250))
        self.load_emagrecer = ImageTk.PhotoImage(self.emagrecer)
        self.label = tk.Label(self.pagina1,image=self.load_emagrecer)
        self.label.grid(row=2,column=1,sticky='nsew')  
        self.label.configure(background = 'light blue')
        
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
        self.pagina2.configure(background = 'light blue')
        
        
        self.lgenero = tk.Label(self.pagina2)
        self.lgenero.grid(row=0, column = 0, sticky = 'nse')
        self.lgenero.configure(fg='black', text = "Gênero:", background = 'light blue')
        
        self.combo = ttk.Combobox(self.pagina2, textvariable = self.combo_value)
        self.combo.grid(row = 0, column = 1)
        self.combo['values'] = ['Masculino', 'Feminino']       
        
        self.bpeso = tk.Entry(self.pagina2, textvariable = self.peso)
        self.bpeso.grid(row = 1, column = 1, sticky = 'ew')     
                
        self.lpeso = tk.Label(self.pagina2)
        self.lpeso.grid(row=1, column=0,sticky="nse")
        self.lpeso.configure(fg='black', text = 'Peso(Kg):', background = 'light blue')
        
        
        self.laltura = tk.Label(self.pagina2)
        self.laltura.grid(row=1, column=2, sticky = 'nse')
        self.laltura.configure(fg='black', text = 'Altura(cm):', background = 'light blue')
        
        self.baltura = tk.Entry(self.pagina2, textvariable = self.altura)
        self.baltura.grid(row=1, column=3, sticky='ew')       
        
        
        self.lidade = tk.Label(self.pagina2)
        self.lidade.grid(row=1, column=4, sticky = 'nse')
        self.lidade.configure(fg='black', text = 'Idade:', background = 'light blue')
        
        self.bidade = tk.Entry(self.pagina2, textvariable = self.idade)
        self.bidade.grid(row = 1, column = 5, sticky = 'ew' )
        
        
        self.lfrase = tk.Label(self.pagina2)
        self.lfrase.grid(row=2,column=2,columnspan=3, sticky='nsew')
        self.lfrase.configure(fg="black", text="Selecione seu nivel de atividade fisica:", background = 'light blue')
        
        
        self.mostrar1 = Image.open('sedentarismo.jpg').resize((150,100))
        self.plotar1 = ImageTk.PhotoImage(self.mostrar1)
        self.imagem1 = ttk.Button(self.pagina2,image = self.plotar1)
        self.imagem1.grid(row = 3, column = 1, sticky = 'nsew')
        self.imagem1.configure(command=self.clicar_sedentario)
                
        self.mostrar2 = Image.open('levemente.jpg').resize((150,100))
        self.plotar2 = ImageTk.PhotoImage(self.mostrar2)
        self.imagem2 = ttk.Button(self.pagina2, image = self.plotar2)
        self.imagem2.grid(row = 3, column = 3, sticky = 'nsew')
        self.imagem2.configure(command=self.clicar_levemente)
               
        self.mostrar3 = Image.open('ativo.jpg').resize((150,100))
        self.plotar3 = ImageTk.PhotoImage(self.mostrar3)        
        self.imagem3 = ttk.Button(self.pagina2, image = self.plotar3)
        self.imagem3.grid(row = 3, column = 5, sticky = 'nsew')
        self.imagem3.configure(command=self.clicar_moderamente)
                
        self.mostrar4 = Image.open('bastante ativo.jpg').resize((150,100))
        self.plotar4 = ImageTk.PhotoImage(self.mostrar4)
        self.imagem4 = ttk.Button(self.pagina2, image = self.plotar4)
        self.imagem4.grid(row = 5, column = 1, sticky = 'nsew')
        self.imagem4.configure(command=self.clicar_muito)
                
        self.mostrar5 = Image.open('muito ativo.jpg').resize((150,100))
        self.plotar5 = ImageTk.PhotoImage(self.mostrar5)
        self.imagem5 = ttk.Button(self.pagina2, image = self.plotar5)
        self.imagem5.grid(row = 5, column =3, sticky = 'nsew')
        self.imagem5.configure(command=self.clicar_extremamente)
    
    
        self.legenda1 = tk.Label(self.pagina2)
        self.legenda1.grid(row = 4, column = 1, sticky = '')
        self.legenda1.configure(fg = 'black', text = 'sedentário', background = 'light blue')
        ttp.CreateToolTip(self.legenda1, 'Pouco ou nenhum exercício diário.')
                       
        self.legenda2 = tk.Label(self.pagina2)
        self.legenda2.grid(row = 4, column = 3, sticky = '')
        self.legenda2.configure(fg = 'black', text = 'levemente ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda2, 'Exercício leve/1 a 3 dias por semana.')
        
        self.legenda3 = tk.Label(self.pagina2)
        self.legenda3.grid(row = 4, column = 5, sticky = '')
        self.legenda3.configure(fg = 'black', text = 'moderadamente ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda3, 'Exercício moderado/3 a 5 dias por semana')
        
        self.legenda4 = tk.Label(self.pagina2)
        self.legenda4.grid(row = 6, column = 1, sticky = 'nsew')
        self.legenda4.configure(fg = 'black', text = 'muito ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda4, 'Exercício intenso/ 6 a 7 dias na semana')        
        
        self.legenda5 = tk.Label(self.pagina2)
        self.legenda5.grid(row = 6, column = 3, sticky = 'nsew')
        self.legenda5.configure(fg = 'black', text = 'extremamente ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda5, 'Exercício intenso todos os dias da semana ou com treinos bi-diários')

        
        self.botao_voltar_pag1 = ttk.Button(self.pagina2, width=20)
        self.botao_voltar_pag1.grid(row=6,column=5,sticky='se')
        self.botao_voltar_pag1.configure(text="Voltar")
        self.botao_voltar_pag1.configure(command=self.pagina1.tkraise)
        
        
        #terceira frame
        
        self.pagina3 = tk.Frame(self.window)
        
        self.pagina3.rowconfigure(0, minsize = 35)
        self.pagina3.rowconfigure(1, minsize = 35)
        self.pagina3.rowconfigure(2, minsize = 35)
        self.pagina3.rowconfigure(3, minsize = 35)
        self.pagina3.rowconfigure(4, minsize = 35)
        self.pagina3.rowconfigure(5, minsize = 75)
        self.pagina3.rowconfigure(6, minsize = 75)
        self.pagina3.rowconfigure(7, minsize = 75)
        self.pagina3.rowconfigure(8, minsize = 75)
        self.pagina3.columnconfigure(0, minsize = 150)
        self.pagina3.columnconfigure(1, minsize = 150)
        self.pagina3.columnconfigure(2, minsize = 150)
        self.pagina3.columnconfigure(3, minsize = 150)
        self.pagina3.columnconfigure(4, minsize = 150)
        self.pagina3.columnconfigure(5, minsize = 150)
        self.pagina3.grid(row=0, column=0, sticky="nsew")
        self.pagina3.configure(background = 'light blue')
        
        
        
        self.frase_1 = ttk.Label(self.pagina3)
        self.frase_1.grid(row = 0, column = 0, sticky = 'nsew')
        self.frase_1.configure(text = "Quantidades a serem consumidas:", font ="ComicSansMS 14")
        self.frase_1.configure(background = 'light blue')
        
        self.carboidrato = ttk.Label(self.pagina3)
        self.carboidrato.grid(row = 1, column = 0, sticky = 'nsew')
        self.carboidrato.configure(textvariable = self.cc)
        self.carboidrato.configure(background = 'light blue')
        
        self.proteina = ttk.Label(self.pagina3)
        self.proteina.grid(row = 1, column = 1, sticky = 'nsew')
        self.proteina.configure(textvariable = self.cp)
        self.proteina.configure(background = 'light blue')        

        self.gordura = ttk.Label(self.pagina3)
        self.gordura.grid(row = 1, column = 2, sticky = 'nse')
        self.gordura.configure(textvariable = self.cg)
        self.gordura.configure(background = 'light blue')
        
        self.frase_2 = ttk.Label(self.pagina3)
        self.frase_2.grid(row = 2, column = 0, columnspan=2,sticky = 'nsw')
        self.frase_2.configure(text = "Quantidades já consumidas:", font ="ComicSansMS 14")
        self.frase_2.configure(background = 'light blue')
        
        self.carboidrato_2 = ttk.Label(self.pagina3)
        self.carboidrato_2.grid(row = 3, column = 0, sticky = 'nsw')
        self.carboidrato_2.configure(textvariable = self.carbo_consumidos)
        self.carboidrato_2.configure(background = 'light blue')
        
        self.proteina_2 = ttk.Label(self.pagina3)
        self.proteina_2.grid(row = 3, column = 1, sticky = 'nsw')
        self.proteina_2.configure(textvariable = self.prot_consumidos, background = 'light blue')
        
        self.gordura_2 = ttk.Label(self.pagina3)
        self.gordura_2.grid(row = 3, column = 2, sticky = 'nse')
        self.gordura_2.configure(textvariable = self.gordura_consumidos, background = 'light blue')
        
        self.frase_3 = ttk.Label(self.pagina3)
        self.frase_3.grid(row = 7, column = 0, sticky = 'nsw')
        self.frase_3.configure(text = "Alimentos consumidos:", background = 'light blue', font ="ComicSansMS 14")
        
        self.ad_alimento = ttk.Label(self.pagina3)
        self.ad_alimento.grid(row = 4, column = 0, columnspan = 1, sticky = 'nswe')
        self.ad_alimento.configure(text = "Adicione um alimento:", background = 'light blue', font ="ComicSansMS 14")
        
        
        self.v1 = tk.StringVar(self.pagina3)
        self.v1.set(self.categoria_comida_inicial)
        
        self.d1 = ttk.OptionMenu(self.pagina3, self.v1, "Escolha a categoria", *self.categorias_comida, command=self.option_1_selected)
        self.d1.grid(row=5, column=0,  columnspan=2, sticky="w")
        
        self.v2 = tk.StringVar(self.pagina3)
        self.v2.set(self.comida_inicial) # default value
        
        self.d2 = ttk.OptionMenu(self.pagina3, self.v2, "Escolha a comida", *self.comidas_na_categoria, command=self.option_2_selected)
        self.d2.grid(row=6, column=0, columnspan=2, sticky="w")
        
        
        self.quan_alimento = ttk.Label(self.pagina3)
        self.quan_alimento.grid(row = 5, column = 2,sticky = 'nswe')
        self.quan_alimento.configure(text = "Quantidade do alimento(g):", background = 'light blue')
        
        self.entry_quan = ttk.Entry(self.pagina3, textvariable = self.quantidade)
        self.entry_quan.grid(row = 5, column = 3)
        
        self.listbox_ad = tk.Listbox(self.pagina3, width=100)  
        self.listbox_ad.grid(row = 8, column = 0, columnspan = 4, sticky = 'nsw')
        #self.listbox_ad.configure(yscrollcommand=self.scrollbar_ad.set)
        
        self.scrollbar_ad = tk.Scrollbar(self.listbox_ad, orient = "vertical")
        #self.scrollbar_ad.configure(command=self.listbox_ad.yview)
        
        
         
        self.botao_voltar_pag2 = ttk.Button(self.pagina3, width=20)
        self.botao_voltar_pag2.grid(row=8,column=4,sticky='s')
        self.botao_voltar_pag2.configure(text="Voltar")
        self.botao_voltar_pag2.configure(command = self.pagina2.tkraise)
        
        self.botao_adicionar_alimento = ttk.Button(self.pagina3, width=20)
        self.botao_adicionar_alimento.grid(row=6,column=3)
        self.botao_adicionar_alimento.configure(text="Adicionar alimento")
        self.botao_adicionar_alimento.configure(command=self.clicar_adicionar)
        
        
        self.botao_remover_alimento = ttk.Button(self.pagina3, width=20)
        self.botao_remover_alimento.grid(row=7,column=3,sticky="n")
        self.botao_remover_alimento.configure(text="Remover alimento")
        self.botao_remover_alimento.configure(command=self.clicar_remover)
    
    
        self.botao_finalizar = ttk.Button(self.pagina3)
        self.botao_finalizar.grid(row= 7, column=3 ,sticky='s')
        self.botao_finalizar.configure(text = 'Finalizar o dia')
        self.botao_finalizar.configure(command = self.clicar_finalizar)
        
        #Chamando a primeira frame
        if self.inicio == 0:
            self.pagina0.tkraise() 
        else:
            self.pagina3.tkraise()
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
            self.cc.set("Carboidratos(g): {0}".format(int(self.dici['carboidratos a serem consumidos'])))
            self.cp.set("Proteinas(g): {0}".format(int(self.dici['proteinas a serem consumidos'])))
            self.cg.set("Gorduras(g): {0}".format(int(self.dici['gorduras a serem consumidos'])))
        
   #métodos do programa
    
    def iniciar(self):
        self.window.mainloop()
        
        

    
    def clicar_seguinte(self):
        self.pagina1.tkraise()
        
    def clicar_GanharMassa(self):
        self.objetivo_escolhido.set(1)
        self.pagina2.tkraise()
        
    def clicar_Emagrecer(self):
        self.objetivo_escolhido.set(2) 
        self.pagina2.tkraise()
        
        
    def atualiza_combo(self, event):
        print("atualiza_combo")
        
    def clicar_sedentario(self):
        o = int(self.objetivo_escolhido.get())
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())
 
        if self.carbo_consumidos.get() != "Carboidratos(g): 0":         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            
        if self.prot_consumidos.get() != "Proteinas(g): 0":         
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
        else:
            self.prot_consumidos.set("Proteinas(g): 0")
        
        if self.gordura_consumidos.get() != "Gorduras(g): 0":         
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.gordura_consumidos.set("Gorduras(g): 0")
            
        if o == 1:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.2 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.2 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
        else:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.2 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.2 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1

            
        
    def clicar_levemente(self):
        o = int(self.objetivo_escolhido.get())
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())

        if self.carbo_consumidos.get() != "Carboidratos(g): 0":         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            
        if self.prot_consumidos.get() != "Proteinas(g): 0":         
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
        else:
            self.prot_consumidos.set("Proteinas(g): 0")
        
        if self.gordura_consumidos.get() != "Gorduras(g): 0":         
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.gordura_consumidos.set("Gorduras(g): 0")
            

        if o == 1:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.375 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.375 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
        else:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.375 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.375 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1

        
    def clicar_moderamente(self):
        o = int(self.objetivo_escolhido.get())
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())

        if self.carbo_consumidos.get() != "Carboidratos(g): 0":         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            
        if self.prot_consumidos.get() != "Proteinas(g): 0":         
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
        else:
            self.prot_consumidos.set("Proteinas(g): 0")
        
        if self.gordura_consumidos.get() != "Gorduras(g): 0":         
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.gordura_consumidos.set("Gorduras(g): 0")
            
        if o == 1:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.55 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.55 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
        else:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.55 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.55 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1

        
    def clicar_muito(self):
        o = int(self.objetivo_escolhido.get())
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())

        if self.carbo_consumidos.get() != "Carboidratos(g): 0":         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            
        if self.prot_consumidos.get() != "Proteinas(g): 0":         
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
        else:
            self.prot_consumidos.set("Proteinas(g): 0")
        
        if self.gordura_consumidos.get() != "Gorduras(g): 0":         
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.gordura_consumidos.set("Gorduras(g): 0")
            
        if o == 1:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.725 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.725 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
        else:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.725 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.725 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1

        

    def clicar_extremamente(self):
        o = int(self.objetivo_escolhido.get())
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())
        


        if self.carbo_consumidos.get() != "Carboidratos(g): 0":         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            
        if self.prot_consumidos.get() != "Proteinas(g): 0":         
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
        else:
            self.prot_consumidos.set("Proteinas(g): 0")
        
        if self.gordura_consumidos.get() != "Gorduras(g): 0":         
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.gordura_consumidos.set("Gorduras(g): 0")
         

        

        if o == 1:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.9 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.9 + 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
        else:
            if g == 'Masculino':
                self.k= ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.9 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
            elif g == 'Feminino':
                self.k= ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.9 - 500
                self.prot= p*2
                self.p.set(self.prot)
                self.carbo= (self.k*0.6)/4
                self.c.set(self.carbo)
                self.g.set((self.k-(self.prot*4)-(self.carbo*4))/9)
                self.cc.set("Carboidratos(g): {0}".format(int(self.carbo)))
                self.cp.set("Proteinas(g): {0}".format(int(self.prot)))
                self.cg.set("Gorduras(g): {0}".format(int((self.k-(self.prot*4)-(self.carbo*4))/9)))
                self.pagina3.tkraise()
                self.inicio = 1
                
            
    def option_1_selected(self,categoria):
        if categoria in self.comidas:
            self.menu = self.d2['menu']
            self.menu.delete(0, 'end')
            self.comidas_na_categoria2 = [c for c in self.comidas[categoria]]
            self.comidas_na_categoria2.sort()

        for c in self.comidas_na_categoria2:
            self.menu.add_command(label=c, command=lambda x=c: self.option_2_selected(x))

        for c in self.comidas_na_categoria2:
            self.v2.set(c)
            break

    def option_2_selected(self,comida):
        self.categoria = self.v1.get()
        self.v2.set(comida)
        if self.categoria in self.comidas:
            self.nutrientes = self.comidas[self.categoria][comida]
            return self.nutrientes
            
    def clicar_adicionar(self):
        self.lista_alimentos_consumidos.append([self.ConsumoCarbo(),self.ConsumoProteina(),self.ConsumoGordura()])
        self.listbox_ad.insert(tk.END, "{0}:      Carboidratos: {1}      Proteinas: {2}      Gorduras: {3}".format(self.v2.get(),self.ConsumoCarbo(),self.ConsumoProteina(),self.ConsumoGordura()))
        
        
        
    def clicar_remover(self):
      #  if len(self.lista_alimentos_consumidos) == 0:
      #      return
            
      #  ultimo_alimento = self.lista_alimentos_consumidos[-1]
      # ultimo_carbo = ultimo_alimento[0]
      # ultimo_prot = ultimo_alimento[1]
      # ultimo_gord = ultimo_alimento[2]
        
        self.variavel_carbo_consumido -= float(self.ultimo_alimento_carbo.get())
        self.carbo_consumidos.set("Carboidratos(g): {0}" .format(self.variavel_carbo_consumido))
        self.variavel_prot_consumido -= float(self.ultimo_alimento_prot.get())
        self.prot_consumidos.set("Proteinas(g): {0}" .format(self.variavel_prot_consumido))
        self.variavel_gord_consumido -= float(self.ultimo_alimento_gord.get())
        self.gordura_consumidos.set("Gorduras(g): {0}" .format(self.variavel_gord_consumido))
        self.listbox_ad.delete(tk.END)
        
        
        
    def ConsumoCarbo(self):        
        
        self.carbo_alimento_quantidade = (self.comidas[self.v1.get()][self.v2.get()][0]*float(self.quantidade.get()))/100
        self.variavel_carbo_consumido += self.carbo_alimento_quantidade
        self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.variavel_carbo_consumido))
        self.ultimo_alimento_carbo.set(self.carbo_alimento_quantidade)        
        return self.carbo_alimento_quantidade
     
        
        
    def ConsumoProteina(self):
        
        self.prot_alimento_quantidade = (self.comidas[self.v1.get()][self.v2.get()][1]*float(self.quantidade.get()))/100
        self.variavel_prot_consumido += self.prot_alimento_quantidade
        self.prot_consumidos.set("Proteinas(g): {0}".format(self.variavel_prot_consumido))
        self.ultimo_alimento_prot.set(self.prot_alimento_quantidade)
        return self.prot_alimento_quantidade
        
        
    def ConsumoGordura(self):
        self.gord_alimento_quantidade = (self.comidas[self.v1.get()][self.v2.get()][2]*float(self.quantidade.get()))/100
        self.variavel_gord_consumido += self.gord_alimento_quantidade
        self.gordura_consumidos.set("Gorduras(g): {0}".format(self.variavel_gord_consumido))
        self.ultimo_alimento_gord.set(self.gord_alimento_quantidade)
        return self.gord_alimento_quantidade


        
    def irpagina3(self):
        self.inicio = 1
        self.pagina3.tkraise()
        
           
        
    def terminar(self):
        #criando dicionario
        self.dici['iniciar'] = self.inicio
        self.dici['carboidratos consumidas'] = float(self.variavel_carbo_consumido)
        self.dici['proteina consumidos'] = float(self.variavel_prot_consumido)
        self.dici['gordura consumidos'] = float(self.variavel_gord_consumido)
        self.dici['carboidratos a serem consumidos'] = float(self.c.get())
        self.dici['proteinas a serem consumidos'] = float(self.p.get())
        self.dici['gorduras a serem consumidos'] = float(self.g.get())
        
        #salvando no pickle
        salvar = open("projeto.pickle", "wb")
        pickle.dump(self.dici, salvar)
        salvar.close()
        
        
        #fechando o programa
        
        
        print(self.dici)
        self.window.quit()
        
    def clicar_finalizar(self):
        self.dici['iniciar'] = 0
        self.dici['carboidratos consumidas'] = 0
        self.dici['proteina consumidos'] = 0
        self.dici['gordura consumidos'] = 0
        self.dici['carboidratos a serem consumidos'] = 0
        self.dici['proteinas a serem consumidos'] = 0 
        self.dici['gorduras a serem consumidos'] = 0
        salvar = open("projeto.pickle", "wb") 
        pickle.dump(self.dici, salvar)
        salvar.close()
        print(self.dici)
        self.window.quit() 
        

            
        
    
        
app = Projeto_Final()
app.iniciar()