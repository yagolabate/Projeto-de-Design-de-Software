# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import comidas

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
        self.peso = tk.StringVar()
        self.altura = tk.StringVar()
        self.idade = tk.StringVar()        
        self.cc = tk.StringVar()
        self.cg = tk.StringVar()
        self.cp = tk.StringVar()

        self.genero = tk.StringVar()

        self.combo_value = tk.StringVar()
        
        self.window.iconbitmap(self, default='ganhar-massa.ico')
        
        self.comidas = comidas.ler_dicionario_comidas()

        self.categorias_comida = [c for c in self.comidas]
        self.categorias_comida.sort()
        self.categoria_comida_inicial = self.categorias_comida[0]
        
        self.comidas_na_categoria = [c for c in self.comidas[self.categoria_comida_inicial]]
        self.comida_inicial = self.comidas_na_categoria[0]        
        
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
        
        
        self.Bem_vindo = tk.Label(self.pagina1)
        self.Bem_vindo.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.Bem_vindo.configure(text='Bem vindo ao ..', font = 50, background = 'light blue')
        
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
        self.pagina3.rowconfigure(7, minsize = 150)
        self.pagina3.columnconfigure(0, minsize = 100)
        self.pagina3.columnconfigure(1, minsize = 50)
        self.pagina3.columnconfigure(2, minsize = 150)
        self.pagina3.columnconfigure(3, minsize = 150)
        self.pagina3.columnconfigure(4, minsize = 150)
        self.pagina3.columnconfigure(5, minsize = 150)
        self.pagina3.grid(row=0, column=0, sticky="nsew")
        self.pagina3.configure(background = 'light blue')
        
        
        
        self.frase_1 = ttk.Label(self.pagina3)
        self.frase_1.grid(row = 0, column = 0, sticky = 'nsw')
        self.frase_1.configure(text = "Quantidades a serem consumidas:")
        self.frase_1.configure(background = 'white')
        
        self.carboidrato = ttk.Label(self.pagina3)
        self.carboidrato.grid(row = 1, column = 0, sticky = 'nse')
        self.carboidrato.configure(text = "Carboidratos(g):")
        self.carboidrato.configure(background = 'light blue')
        
        self.total_carbo = ttk.Label(self.pagina3)
        self.total_carbo.grid(row = 1, column = 1, sticky = 'nswe')
        self.total_carbo.configure(textvariable = self.cc)
        self.total_carbo.configure(background = 'light blue')

        
        
        self.proteina = ttk.Label(self.pagina3)
        self.proteina.grid(row = 1, column = 2, sticky = 'nse')
        self.proteina.configure(text = "Proteínas(g):")
        self.proteina.configure(background = 'light blue')        
        
        self.total_proteina = ttk.Label(self.pagina3)
        self.total_proteina.grid(row = 1, column = 3, sticky = 'nswe')
        self.total_proteina.configure(textvariable = self.cp)
        self.total_proteina.configure(background = 'light blue')

        
        self.gordura = ttk.Label(self.pagina3)
        self.gordura.grid(row = 1, column = 4, sticky = 'nse')
        self.gordura.configure(text = "Gorduras(g):")
        self.gordura.configure(background = 'light blue')
        
        self.total_gordura = ttk.Label(self.pagina3)
        self.total_gordura.grid(row = 1, column = 5, sticky = 'nswe')
        self.total_gordura.configure(textvariable = self.cg)
        self.total_gordura.configure(background = 'light blue')
        
        self.frase_2 = ttk.Label(self.pagina3)
        self.frase_2.grid(row = 2, column = 0, sticky = 'nsw')
        self.frase_2.configure(text = "Quantidades já consumidas:")
        self.frase_2.configure(background = 'light blue')
        
        self.carboidrato_2 = ttk.Label(self.pagina3)
        self.carboidrato_2.grid(row = 3, column = 0, sticky = 'nse')
        self.carboidrato_2.configure(text = "Carboidratos(g):")
        self.carboidrato_2.configure(background = 'light blue')
        
        self.consumo_carbo = ttk.Label(self.pagina3)
        self.consumo_carbo.grid(row = 3, column = 1, sticky = 'nswe')
        self.consumo_carbo.configure(text = self.ConsumoCarbo(), background = 'light blue' )
        
        self.proteina_2 = ttk.Label(self.pagina3)
        self.proteina_2.grid(row = 3, column = 2, sticky = 'nse')
        self.proteina_2.configure(text = "Proteínas(g):", background = 'light blue')
        
        self.consumo_proteina = ttk.Label(self.pagina3)
        self.consumo_proteina.grid(row = 3, column = 3, sticky = 'nswe')
        self.consumo_proteina.configure(text= self.ConsumoProteina(), background = 'light blue')
        
        self.gordura_2 = ttk.Label(self.pagina3)
        self.gordura_2.grid(row = 3, column = 4, sticky = 'nse')
        self.gordura_2.configure(text = "Gorduras(g):", background = 'light blue')
        
        self.consumo_gordura = ttk.Label(self.pagina3)
        self.consumo_gordura.grid(row = 3, column = 5, sticky = 'nswe')
        self.consumo_gordura.configure(text= self.ConsumoGordura(), background = 'light blue')
        
        self.frase_3 = ttk.Label(self.pagina3)
        self.frase_3.grid(row = 4, column = 0, sticky = 'nsw')
        self.frase_3.configure(text = "Alimentos consumidos:", background = 'light blue')
        
        self.ad_alimento = ttk.Label(self.pagina3)
        self.ad_alimento.grid(row = 5, column = 0, columnspan = 1, sticky = 'nswe')
        self.ad_alimento.configure(text = "Adicione um alimento:", background = 'light blue')
        
        
        self.v1 = tk.StringVar(self.pagina3)
        self.v1.set(self.categoria_comida_inicial)
        
        self.d1 = ttk.OptionMenu(self.pagina3, self.v1, *self.categorias_comida, command=self.option_1_selected)
        self.d1.grid(row=5, column=1, columnspan = 2,)
        
        self.v2 = tk.StringVar(self.pagina3)
        self.v2.set(self.comida_inicial) # default value
        
        self.d2 = ttk.OptionMenu(self.pagina3, self.v2, *self.comidas_na_categoria, command=self.option_2_selected)
        self.d2.grid(row=6, column=1, columnspan = 2)
        
        self.quan_alimento = ttk.Label(self.pagina3)
        self.quan_alimento.grid(row = 5, column = 3, columnspan = 1, sticky = 'nswe')
        self.quan_alimento.configure(text = "Quantidade do alimento(g):", background = 'light blue')
        
        self.entry_quan = ttk.Entry(self.pagina3)
        self.entry_quan.grid(row = 5, column = 4)
        
        self.alimentos_ad = ttk.Scrollbar(self.pagina3, orient = 'vertical')
        self.alimentos_ad.grid(row = 7, column = 0, columnspan = 4, sticky = 'nse')
        
        self.botao_voltar_pag2 = ttk.Button(self.pagina3, width=20)
        self.botao_voltar_pag2.grid(row=7,column=4, columnspan = 2, sticky='s')
        self.botao_voltar_pag2.configure(text="Voltar")
        self.botao_voltar_pag2.configure(command = self.pagina2.tkraise)
        
    
        
        #Chamando a primeira frame
        self.pagina1.tkraise() 
        
        
   #métodos do programa
    
    def iniciar(self):
        self.window.mainloop()
        
    def clicar_GanharMassa(self):
        self.objetivo_escolhido = 1
        self.pagina2.tkraise()
        
    def clicar_Emagrecer(self):
        self.objetivo_escolhido = 2 
        self.pagina2.tkraise()
        
        
    def atualiza_combo(self, event):
        print("atualiza_combo")
        
    def clicar_sedentario(self):
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())
        if g == 'Masculino':
            k = ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.2
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        elif g == 'Feminino':
            k = ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.2
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
            
        
    def clicar_levemente(self):
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())
        if g == 'Masculino':
            k = ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.375
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        elif g == 'Feminino':
            k = ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.375
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        
    def clicar_moderamente(self):
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())
        if g == 'Masculino':
            k = ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.55
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        elif g == 'Feminino':
            k = ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.55
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        
    def clicar_muito(self):
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())
        if g == 'Masculino':
            k = ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.725
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        elif g == 'Feminino':
            k = ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.725
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        

    def clicar_extremamente(self):
        g = self.combo_value.get()
        p = float(self.peso.get())
        a = float(self.altura.get())
        i = float(self.idade.get())
        if g == 'Masculino':
            k = ((13.4*p)+(4.8*a)-(5.68*i)+88.36)*1.9
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        elif g == 'Feminino':
            k = ((9.25*p)+(3.1*a)-(4.33*i)+447.6)*1.9
            prot = p*2
            carbo = (k*0.6)/4
            self.cc.set(int(carbo))
            self.cp.set(int(prot))
            self.cg.set(int((k-(prot*4)-(carbo*4))/9))
            self.pagina3.tkraise()
        

    def clicar_genero(self):
        if self.genero == 'Masculino':
            self.genero = 1
            
        elif self.genero == 'Feminino':
            self.genero = 2
            
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
    
            

        
        
    def ConsumoCarbo(self):
        return 0
        
    def ConsumoProteina(self):
        return 0
        
    def ConsumoGordura(self):
        return 0
        

        
        
    
        
app = Projeto_Final()
app.iniciar()