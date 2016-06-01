# -*- coding: utf-8 -*-
from decimal import Decimal, ROUND_HALF_UP
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
        
        #Definindo os atributos iniciais
        self.window = tk.Tk()
        
        self.window.protocol("WM_DELETE_WINDOW", self.terminar)
        
        self.window.title("Projeto final")
        self.window.geometry('900x600+220+50')
        self.window.rowconfigure(0, minsize = 600)
        self.window.columnconfigure(0, minsize = 900)
        self.window.grid()
        
        
        self.objetivo_escolhido = tk.StringVar() #variavel que indica oo objetivo escolhido
        #pois o calculo dos macronutrientes depende disso, assim como as variaveis peso,
        #idade, altura e genero
        self.peso = tk.StringVar()
        self.altura = tk.StringVar()
        self.idade = tk.StringVar()
        self.genero = tk.StringVar()        
        self.cc = tk.StringVar()
        self.cg = tk.StringVar()
        self.cp = tk.StringVar()
        self.alimento = tk.StringVar()
        self.quantidade = tk.StringVar()
        self.carbo_consumidos = tk.StringVar()
        self.prot_consumidos = tk.StringVar()
        self.gordura_consumidos = tk.StringVar()
        self.c = tk.DoubleVar()
        self.p = tk.DoubleVar()
        self.g = tk.DoubleVar()
        
        arquivo = open("projeto.pickle", "rb") #abertura do arquivo no qual serão guardados
        #os macronutrientes a serem consumidos pelo usuario e os já consumidos
        self.dici = pickle.load(arquivo) 
        
        self.inicio = self.dici['iniciar']
        
        # Criação das variaveis que guardarão a quantidade de carboidratos já consumidos
        # Caso o usuario ja tenha começado a registrar seus alimentos consumidos, as varia-
        # veis serão iguais as respectivas quantidades ja ingeridas de macronutrientes
        
        if self.inicio == 0:
            self.variavel_carbo_consumido = 0
            self.variavel_prot_consumido = 0
            self.variavel_gord_consumido = 0
        else:
            self.variavel_carbo_consumido = self.dici['carboidratos consumidas']
            self.variavel_prot_consumido = self.dici['proteina consumidos']
            self.variavel_gord_consumido = self.dici['gordura consumidos']
        
        # Lista que guardará as quantidades de cada macronutriente consumido        
        
        self.lista_carbo_consumidos = []
        self.lista_prot_consumidos = []
        self.lista_gord_consumidos = []

        self.combo_value = tk.StringVar()
        
        # Ícone da janela        
        self.window.iconbitmap(self, default='ganhar-massa.ico')
        
        # Variável que guarda o dicionário de alimentos         
        self.comidas = comidas.ler_dicionario_comidas()
        
        # Variável que guarda as categorias das comidas
        self.categorias_comida = [c for c in self.comidas]
        self.categorias_comida.sort()
        self.categoria_comida_inicial = self.categorias_comida[0]
        
        # Variável que guarda as comidas de cada categoria
        self.comidas_na_categoria = [c for c in self.comidas[self.categoria_comida_inicial]]
        self.comida_inicial = self.comidas_na_categoria[0]    
        

        
        
                                      # Primeira frame
        
        
        self.pagina1 = tk.Frame(self.window)
        self.pagina1.rowconfigure(0, minsize = 100)
        self.pagina1.rowconfigure(1, minsize = 100)
        self.pagina1.rowconfigure(2, minsize = 300)
        self.pagina1.rowconfigure(3, minsize = 50)
        self.pagina1.columnconfigure(0, minsize = 450)
        self.pagina1.columnconfigure(1, minsize = 450)
        self.pagina1.grid(row=0, column=0, sticky="nsew")
        self.pagina1.configure(background = 'light blue')
        
        
        self.Saudacao = tk.Label(self.pagina1)
        self.Saudacao.grid(row=0, column=0, columnspan=2, sticky='sew')
        self.Saudacao.configure(text='BEM VINDO AO SEU CONTROLE DE ALIMENTAÇÃO', font ="ComicSansMS 25", background = 'light blue')

        # Label que indica o local no qual o usuario escolherá seu objetivo: 
        self.objetivo = tk.Label(self.pagina1)
        self.objetivo.grid(row=1, column=0, columnspan=2, sticky='sew')
        self.objetivo.configure(text='Escolha o seu objetivo:', font ="ComicSansMS 16", background = 'light blue')
        
        # Imagem associada ao ganho de massa
        self.massa = Image.open('ganhar-massa.jpg').resize((320,250))
        self.load_massa = ImageTk.PhotoImage(self.massa)
        self.label = tk.Label(self.pagina1,image=self.load_massa)
        self.label.grid(row=2,column=0,sticky='nsew')  
        self.label.configure(background = 'light blue')
        
        # Imagem associada à perda de peso
        self.emagrecer = Image.open('emagrecer.jpg').resize((320,250))
        self.load_emagrecer = ImageTk.PhotoImage(self.emagrecer)
        self.label = tk.Label(self.pagina1,image=self.load_emagrecer)
        self.label.grid(row=2,column=1,sticky='nsew')  
        self.label.configure(background = 'light blue')
        
        # Botões que permitem aos usuarios escolherem seu objetivo
        
        self.botao_massa = ttk.Button(self.pagina1, width=35)
        self.botao_massa.grid(row=3,column=0,sticky='ns')
        self.botao_massa.configure(text='Ganhar Massa')
        self.botao_massa.configure(command=self.clicar_GanharMassa)
        
        self.botao_emagrecer = ttk.Button(self.pagina1, width=35)
        self.botao_emagrecer.grid(row=3,column=1,sticky='ns')
        self.botao_emagrecer.configure(text='Emagrecer')
        self.botao_emagrecer.configure(command=self.clicar_Emagrecer)
        
        
                                       # Segunda frame
        
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
        
        # Label que indicará ao usuario o local onde escolherá seu genero
        self.lgenero = tk.Label(self.pagina2)
        self.lgenero.grid(row=0, column = 0, sticky = 'nse')
        self.lgenero.configure(fg='black', text = "Gênero:", background = 'light blue')
        
        # Combobox dos generos a serem escolhidos
        self.combo = ttk.Combobox(self.pagina2, textvariable = self.combo_value)
        self.combo.grid(row = 0, column = 1)
        self.combo['values'] = ['Masculino', 'Feminino']       
        
        # Label que indicará ao usuario o local onde inserirá seu peso
        self.lpeso = tk.Label(self.pagina2)
        self.lpeso.grid(row=1, column=0,sticky="nse")
        self.lpeso.configure(fg='black', text = 'Peso(Kg):', background = 'light blue')
        
        # Entry aonde o usuario inserirá seu peso
        self.bpeso = tk.Entry(self.pagina2, textvariable = self.peso)
        self.bpeso.grid(row = 1, column = 1, sticky = 'ew')
        
        # Label que indicará ao usuario o local onde inserirá sua altura
        self.laltura = tk.Label(self.pagina2)
        self.laltura.grid(row=1, column=2, sticky = 'nse')
        self.laltura.configure(fg='black', text = 'Altura(cm):', background = 'light blue')
        
        # Entry aonde o usuario inserirá sua altura
        self.baltura = tk.Entry(self.pagina2, textvariable = self.altura)
        self.baltura.grid(row=1, column=3, sticky='ew')       
        
        # Label que indicará ao usuario o local onde inserirá sua idade
        self.lidade = tk.Label(self.pagina2)
        self.lidade.grid(row=1, column=4, sticky = 'nse')
        self.lidade.configure(fg='black', text = 'Idade:', background = 'light blue')
        
        # Entry aonde o usuario inserirá sua idade
        self.bidade = tk.Entry(self.pagina2, textvariable = self.idade)
        self.bidade.grid(row = 1, column = 5, sticky = 'ew' )
        
        # Label que indicará ao usuário o local onde poderá selecionar seu nivel de ativida-
        #de física
        self.lfrase = tk.Label(self.pagina2)
        self.lfrase.grid(row=2,column=2,columnspan=3, sticky='nsew')
        self.lfrase.configure(fg="black", text="Selecione seu nivel de atividade fisica:",font ="ComicSansMS 16", background = 'light blue')
        
        # Botões que possibilitarão ao usuario escolher seu nivel de atividade fisica
        
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
    
        #Legenda contendo a explicação do que cada nível de atividade física representa
    
        self.legenda1 = tk.Label(self.pagina2)
        self.legenda1.grid(row = 4, column = 1, sticky = '')
        self.legenda1.configure(fg = 'black', text = 'Sedentário', background = 'light blue')
        ttp.CreateToolTip(self.legenda1, 'Pouco ou nenhum exercício diário.')
                       
        self.legenda2 = tk.Label(self.pagina2)
        self.legenda2.grid(row = 4, column = 3, sticky = '')
        self.legenda2.configure(fg = 'black', text = 'Levemente ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda2, 'Exercício leve durante 1 a 3 dias por semana.')
        
        self.legenda3 = tk.Label(self.pagina2)
        self.legenda3.grid(row = 4, column = 5, sticky = '')
        self.legenda3.configure(fg = 'black', text = 'Moderadamente ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda3, 'Exercício moderado durante 3 a 5 dias por semana')
        
        self.legenda4 = tk.Label(self.pagina2)
        self.legenda4.grid(row = 6, column = 1, sticky = 'nsew')
        self.legenda4.configure(fg = 'black', text = 'Muito ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda4, 'Exercício intenso durante 6 a 7 dias na semana')        
        
        self.legenda5 = tk.Label(self.pagina2)
        self.legenda5.grid(row = 6, column = 3, sticky = 'nsew')
        self.legenda5.configure(fg = 'black', text = 'Extremamente ativo', background = 'light blue')
        ttp.CreateToolTip(self.legenda5, 'Exercício intenso todos os dias da semana ou com treinos bi-diários')

        # Botão que permite ao usuario voltar à primeira pagina, caso queira modificar 
        # seu objetivo
        self.botao_voltar_pag1 = ttk.Button(self.pagina2, width=20)
        self.botao_voltar_pag1.grid(row=6,column=5,sticky='se')
        self.botao_voltar_pag1.configure(text="Voltar")
        self.botao_voltar_pag1.configure(command=self.pagina1.tkraise)
        
        
        
                                       # Terceira frame
        
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
        
        
        # Label que indica as quantidade de macronutrientes a serem consumidas
        self.frase_1 = ttk.Label(self.pagina3)
        self.frase_1.grid(row = 0, column = 0, sticky = 'nsew')
        self.frase_1.configure(text = "Quantidades a serem consumidas:", font ="ComicSansMS 14")
        self.frase_1.configure(background = 'light blue')
        
        #Labels que indicam a quantidade de cada macronutriente
        
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
        
        # Label que indica as quantidade de macronutrientes ja consumidas
        self.frase_2 = ttk.Label(self.pagina3)
        self.frase_2.grid(row = 2, column = 0, columnspan=2,sticky = 'nsw')
        self.frase_2.configure(text = "Quantidades já consumidas:", font ="ComicSansMS 14")
        self.frase_2.configure(background = 'light blue')
        
        #Labels que indicam a quantidade de cada macronutriente já consumido
        
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
        
        #Label que indica aonde serão expostos os alimentos já consumidos, assim como seus 
        # macronutrientes
        self.frase_3 = ttk.Label(self.pagina3)
        self.frase_3.grid(row = 7, column = 0, sticky = 'nsw')
        self.frase_3.configure(text = "Alimentos consumidos:", background = 'light blue', font ="ComicSansMS 14")
        
        # Label que indica ao usuario o local onde o usuario registrará os alimentos consumidos
        # por ele
        self.ad_alimento = ttk.Label(self.pagina3)
        self.ad_alimento.grid(row = 4, column = 0, columnspan = 1, sticky = 'nswe')
        self.ad_alimento.configure(text = "Adicione um alimento:", background = 'light blue', font ="ComicSansMS 14")
        
        # Variavel que guarda a categoria de alimento escolhida
        self.v1 = tk.StringVar(self.pagina3)
        self.v1.set(self.categoria_comida_inicial)
        
        # Option Menu das categorias de alimentos
        self.d1 = ttk.OptionMenu(self.pagina3, self.v1, "Escolha a categoria", *self.categorias_comida, command=self.option_1_selected)
        self.d1.grid(row=5, column=0,  columnspan=2, sticky="w")
        
        # Variavel que guarda o alimento da categoria esoclhida
        self.v2 = tk.StringVar(self.pagina3)
        self.v2.set(self.comida_inicial) # default value
        
        # Option Menu das dos alimentos da categoria escolhida
        self.d2 = ttk.OptionMenu(self.pagina3, self.v2, "Escolha a comida", *self.comidas_na_categoria, command=self.option_2_selected)
        self.d2.grid(row=6, column=0, columnspan=2, sticky="w")
        
        # Label que indicará o local aonde o usuario inserirá a quantidade do alimento con-
        # sumido
        self.quan_alimento = ttk.Label(self.pagina3)
        self.quan_alimento.grid(row = 5, column = 2,sticky = 'nswe')
        self.quan_alimento.configure(text = "Quantidade do alimento(g):", background = 'light blue')
        
        # Entry na qual o usuario inserirá a quantidade do alimento consumido
        self.entry_quan = ttk.Entry(self.pagina3, textvariable = self.quantidade)
        self.entry_quan.grid(row = 5, column = 3)
        
        # Lisbox que mostrará os alimentos adicionados pelo usuario
        self.listbox_ad = tk.Listbox(self.pagina3, selectmode = tk.SINGLE, width=100)  
        self.listbox_ad.grid(row = 8, column = 0, columnspan = 4, sticky = 'nsw')
        
        self.scrollbar_ad = tk.Scrollbar(self.listbox_ad, orient = "vertical")

        # Botão que permitirá ao usuário adicionar o alimento ao listbox
        self.botao_adicionar_alimento = ttk.Button(self.pagina3, width=20)
        self.botao_adicionar_alimento.grid(row=6,column=3)
        self.botao_adicionar_alimento.configure(text="Adicionar alimento")
        self.botao_adicionar_alimento.configure(command=self.clicar_adicionar)
        
        # Botão que permitirá ao usuário remover o alimento do listbox
        self.botao_remover_alimento = ttk.Button(self.pagina3, width=20)
        self.botao_remover_alimento.grid(row=7,column=3,sticky="n")
        self.botao_remover_alimento.configure(text="Remover alimento")
        self.botao_remover_alimento.configure(command=self.clicar_remover)
    
        # Botão que permitirá ao usuário a finalizar seu dia e zerar os dados do dia
        self.botao_finalizar = ttk.Button(self.pagina3, width=20)
        self.botao_finalizar.grid(row= 8, column=4 ,sticky='s')
        self.botao_finalizar.configure(text = 'Finalizar o dia')
        self.botao_finalizar.configure(command = self.clicar_finalizar)
        
        #Chamando a primeira frame
        if self.inicio == 0:
            self.pagina1.tkraise() 
        else:
            self.pagina3.tkraise()
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
            self.cc.set(self.dici['carboidratos a serem consumidos'])
            self.cp.set(self.dici['proteinas a serem consumidos'])
            self.cg.set(self.dici['gorduras a serem consumidos'])
   
   
                                    # Métodos do programa
    
    
    # Função que abre a janela
    def iniciar(self):
        self.window.mainloop()
    
    # Função que troca a frame atual para a primeira frame    
    def clicar_seguinte(self):
        self.pagina1.tkraise()
    
    # Função que muda o valor da variável objetivo_escolhido para ser utilizado no cálculo 
    # dos macronutrientes e troca a frame atual para a segunda frame     
    def clicar_GanharMassa(self):
        self.objetivo_escolhido.set(1)
        self.pagina2.tkraise()
    
    # Função que muda o valor da variável objetivo_escolhido para ser utilizado no cálculo 
    # dos macronutrientes e troca a frame atual para a segunda frame     
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
 
        if self.inicio == 1:         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            self.prot_consumidos.set("Proteinas(g): 0")
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

        if self.inicio == 1:         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            self.prot_consumidos.set("Proteinas(g): 0")
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

        if self.inicio == 1:         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            self.prot_consumidos.set("Proteinas(g): 0")
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

        if self.inicio == 1:         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            self.prot_consumidos.set("Proteinas(g): 0")
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
        


        if self.inicio == 1:         
            self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.dici['carboidratos consumidas']))
            self.prot_consumidos.set("Proteinas(g): {0}".format(self.dici['proteina consumidos']))
            self.gordura_consumidos.set("Gorduras(g): {0}".format(self.dici['gordura consumidos']))
        else:
            self.carbo_consumidos.set("Carboidratos(g): 0")
            self.prot_consumidos.set("Proteinas(g): 0")
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
        #adicionando o alimento e seus macronutrientes ao listbox
        self.listbox_ad.insert(tk.END, "{0}:      Carboidratos: {1}      Proteinas: {2}      Gorduras: {3}".format(self.v2.get(),Decimal(self.ConsumoCarbo().quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),Decimal(self.ConsumoProteina().quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),Decimal(self.ConsumoGordura().quantize(Decimal('.01'), rounding=ROUND_HALF_UP))))
        #adicionando os macronutrientes as suas respectivas listas
        self.lista_carbo_consumidos.append(Decimal(self.ConsumoCarbo().quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))    
        self.lista_prot_consumidos.append(Decimal(self.ConsumoProteina().quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        self.lista_gord_consumidos.append(Decimal(self.ConsumoGordura().quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        #adicionando os macronutrientes aos labels
        self.variavel_carbo_consumido += Decimal(self.ConsumoCarbo().quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
        self.carbo_consumidos.set("Carboidratos(g): {0}".format(self.variavel_carbo_consumido))
        self.variavel_prot_consumido += Decimal(self.ConsumoProteina().quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
        self.prot_consumidos.set("Proteinas(g): {0}".format(self.variavel_prot_consumido))
        self.variavel_gord_consumido += Decimal(self.ConsumoGordura().quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
        self.gordura_consumidos.set("Gorduras(g): {0}".format(self.variavel_gord_consumido))
        
        
    def clicar_remover(self):
              
        if self.listbox_ad.size() > 0: 
            #removendo os macronutrientes das labels
            if self.listbox_ad.curselection() != ():
                self.variavel_carbo_consumido -= Decimal(float(self.lista_carbo_consumidos[self.listbox_ad.curselection()[0]])).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
                self.carbo_consumidos.set("Carboidratos(g): {0}" .format(self.variavel_carbo_consumido))
                del self.lista_carbo_consumidos[self.listbox_ad.curselection()[0]]
                self.variavel_prot_consumido -= Decimal(float(self.lista_prot_consumidos[self.listbox_ad.curselection()[0]])).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
                self.prot_consumidos.set("Proteinas(g): {0}" .format(self.variavel_prot_consumido))
                del self.lista_prot_consumidos[self.listbox_ad.curselection()[0]]                
                self.variavel_gord_consumido -= self.lista_gord_consumidos[self.listbox_ad.curselection()[0]]
                self.gordura_consumidos.set("Gorduras(g): {0}" .format(Decimal(self.variavel_gord_consumido.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))))
                del self.lista_gord_consumidos[self.listbox_ad.curselection()[0]]                
            
            
            # Removendo os macronutrientes e alimentos da listbox            
            items = self.listbox_ad.curselection()
            pos = 0
            for i in items :
                idx = int(i) - pos
                self.listbox_ad.delete( idx,idx )
                pos = pos + 1
        else:
            return
        
         
        
    def ConsumoCarbo(self):        
        
        self.carbo_alimento_quantidade = Decimal((self.comidas[self.v1.get()][self.v2.get()][0]*float(self.quantidade.get()))/100)
        return self.carbo_alimento_quantidade
     

    def ConsumoProteina(self):
        
        self.prot_alimento_quantidade = Decimal((self.comidas[self.v1.get()][self.v2.get()][1]*float(self.quantidade.get()))/100)
        return self.prot_alimento_quantidade
        
        
    def ConsumoGordura(self):
        self.gord_alimento_quantidade = Decimal((self.comidas[self.v1.get()][self.v2.get()][2]*float(self.quantidade.get()))/100)
        return self.gord_alimento_quantidade

        
           
        
    def terminar(self):
        
        # Criando dicionario
        self.dici['iniciar'] = self.inicio
        self.dici['carboidratos consumidas'] = Decimal(self.variavel_carbo_consumido)
        self.dici['proteina consumidos'] = Decimal(self.variavel_prot_consumido)
        self.dici['gordura consumidos'] = Decimal(self.variavel_gord_consumido)
        if self.inicio == 0:            
            self.dici['carboidratos a serem consumidos'] = (self.c.get())
            self.dici['proteinas a serem consumidos'] = (self.p.get())
            self.dici['gorduras a serem consumidos'] =  (self.g.get())
        else:
            self.dici['carboidratos a serem consumidos'] = (self.cc.get())
            self.dici['proteinas a serem consumidos'] = (self.cp.get())
            self.dici['gorduras a serem consumidos'] =  (self.cg.get())
        
        
        # Salvando no pickle
        salvar = open("projeto.pickle", "wb")
        pickle.dump(self.dici, salvar)
        salvar.close()
        
        
        # Fechando o programa
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
        self.window.quit() 
        

            
        
    
        
app = Projeto_Final()
app.iniciar()