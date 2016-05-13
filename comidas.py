# -*- coding: utf-8 -*-
"""
Created on Fri May 13 07:51:33 2016

@author: Yago
"""

def ler_dicionario_comidas():
    comidas = {
        "Cereais e derivados": {
            "	Arroz, integral, cozido	"	:	[	25.8	,	2.6	,	1.0	]	,
            "	Arroz, integral, cru	"	:	[	77.5	,	7.3	,	1.9	]	,
            "	Arroz, tipo 1, cozido	"	:	[	28.1	,	2.5	,	0.2	]	,
            "	Arroz, tipo 1, cru	"	:	[	78.8	,	7.2	,	0.3	]	,
            "	Arroz, tipo 2, cozido	"	:	[	28.2	,	2.6	,	0.4	]	,
            "	Arroz, tipo 2, cru	"	:	[	78.9	,	7.2	,	0.3	]	,
            "	Aveia, flocos, crua	"	:	[	66.6	,	13.9	,	8.5	]	,
            "	Biscoito, doce, maisena	"	:	[	75.2	,	8.1	,	12.0	]	,
            "	Biscoito, doce, recheado com chocolate	"	:	[	70.5	,	6.4	,	19.6	]	,
            "	Biscoito, doce, recheado com morango	"	:	[	71.0	,	5.7	,	19.6	]	,
            "	Biscoito, doce, wafer, recheado de chocolate	"	:	[	67.5	,	5.6	,	24.7	]	,
            "	Biscoito, doce, wafer, recheado de morango	"	:	[	67.4	,	4.5	,	26.4	]	,
            "	Biscoito, salgado, cream cracker	"	:	[	68.7	,	10.1	,	14.4	]	,
            "	Bolo, mistura para	"	:	[	84.7	,	6.2	,	6.1	]	,
            "	Bolo, pronto, aipim	"	:	[	47.9	,	4.4	,	12.7	]	,
            "	Bolo, pronto, chocolate	"	:	[	54.7	,	6.2	,	18.5	]	,
            "	Bolo, pronto, coco	"	:	[	52.3	,	5.7	,	11.3	]	,
            "	Bolo, pronto, milho	"	:	[	45.1	,	4.8	,	12.4	]	,
            "	Canjica, branca, crua	"	:	[	78.1	,	7.2	,	1.0	]	,
            "	Canjica, com leite integral	"	:	[	23.6	,	2.4	,	1.2	]	,
            "	Cereais, milho, flocos, com sal	"	:	[	80.8	,	7.3	,	1.6	]	,
            "	Cereais, milho, flocos, sem sal	"	:	[	80.4	,	6.9	,	1.2	]	,
            "	Cereais, mingau, milho, infantil	"	:	[	87.3	,	6.4	,	1.1	]	,
            "	Cereais, mistura para vitamina, trigo, cevada e aveia	"	:	[	81.6	,	8.9	,	2.1	]	,
            "	Cereal matinal, milho	"	:	[	83.8	,	7.2	,	1.0	]	,
            "	Cereal matinal, milho, açúcar	"	:	[	88.8	,	4.7	,	0.7	]	,
            "	Creme de arroz, pó	"	:	[	83.9	,	7.0	,	1.2	]	,
            "	Creme de milho, pó	"	:	[	86.1	,	4.8	,	1.6	]	,
            "	Curau, milho verde	"	:	[	13.9	,	2.4	,	1.6	]	,
            "	Curau, milho verde, mistura para	"	:	[	79.8	,	2.2	,	13.4	]	,
            "	Farinha, de arroz, enriquecida	"	:	[	85.5	,	1.3	,	0.3	]	,
            "	Farinha, de centeio, integral	"	:	[	73.3	,	12.5	,	1.8	]	,
            "	Farinha, de milho, amarela	"	:	[	79.1	,	7.2	,	1.5	]	,
            "	Farinha, de rosca	"	:	[	75.8	,	11.4	,	1.5	]	,
            "	Farinha, de trigo	"	:	[	75.1	,	9.8	,	1.4	]	,
            "	Farinha, láctea, de cereais	"	:	[	77.8	,	11.9	,	5.8	]	,
            "	Lasanha, massa fresca, cozida	"	:	[	32.5	,	5.8	,	1.2	]	,
            "	Lasanha, massa fresca, crua	"	:	[	45.1	,	7.0	,	1.3	]	,
            "	Macarrão, instantâneo	"	:	[	62.4	,	8.8	,	17.2	]	,
            "	Macarrão, trigo, cru	"	:	[	77.9	,	10.0	,	1.3	]	,
            "	Macarrão, trigo, cru, com ovos	"	:	[	76.6	,	10.3	,	2.0	]	,
            "	Milho, amido, cru	"	:	[	87.1	,	0.6	,	0	]	,
            "	Milho, fubá, cru	"	:	[	78.9	,	7.2	,	1.9	]	,
            "	Milho, verde, cru	"	:	[	28.6	,	6.6	,	0.6	]	,
            "	Milho, verde, enlatado, drenado	"	:	[	17.1	,	3.2	,	2.4	]	,
            "	Mingau tradicional, pó	"	:	[	89.3	,	0.6	,	0.4	]	,
            "	Pamonha, barra para cozimento, pré-cozida	"	:	[	30.7	,	2.6	,	4.8	]	,
            "	Pão, aveia, forma	"	:	[	59.6	,	12.4	,	5.7	]	,
            "	Pão, de soja	"	:	[	56.5	,	11.3	,	3.6	]	,
            "	Pão, glúten, forma	"	:	[	44.1	,	12.0	,	2.7	]	,
            "	Pão, milho, forma	"	:	[	56.4	,	8.3	,	3.1	]	,
            "	Pão, trigo, forma, integral	"	:	[	49.9	,	9.4	,	3.7	]	,
            "	Pão, trigo, francês	"	:	[	58.6	,	8.0	,	3.1	]	,
            "	Pão, trigo, sovado	"	:	[	61.5	,	8.4	,	2.8	]	,
            "	Pastel, de carne, cru	"	:	[	42.0	,	10.7	,	8.8	]	,
            "	Pastel, de carne, frito	"	:	[	43.8	,	10.1	,	20.1	]	,
            "	Pastel, de queijo, cru	"	:	[	45.9	,	9.9	,	9.6	]	,
            "	Pastel, de queijo, frito	"	:	[	48.1	,	8.7	,	22.7	]	,
            "	Pastel, massa, crua	"	:	[	57.4	,	6.9	,	5.5	]	,
            "	Pastel, massa, frita	"	:	[	49.3	,	6.0	,	40.9	]	,
            "	Pipoca, com óleo de soja, sem sal	"	:	[	70.3	,	9.9	,	15.9	]	,
            "	Polenta, pré-cozida	"	:	[	23.3	,	2.3	,	0.3	]	,
            "	Torrada, pão francês	"	:	[	74.6	,	10.5	,	3.3	]	,
        },
        "Verduras, Horatliças e derivados": {
            "	Abóbora, cabotian, cozida	"	:	[	10.8	,	1.4	,	0.7	]	,
            "	Abóbora, cabotian, crua	"	:	[	8.4	,	1.7	,	0.5	]	,
            "	Abóbora, menina brasileira, crua	"	:	[	3.3	,	0.6	,	0	]	,
            "	Abóbora, moranga, crua	"	:	[	2.7	,	1.0	,	0.1	]	,
            "	Abóbora, moranga, refogada	"	:	[	6.0	,	0.4	,	0.8	]	,
            "	Abóbora, pescoço, crua	"	:	[	6.1	,	0.7	,	0.1	]	,
            "	Abobrinha, italiana, cozida	"	:	[	3.0	,	1.1	,	0.2	]	,
            "	Abobrinha, italiana, crua	"	:	[	4.3	,	1.1	,	0.1	]	,
            "	Abobrinha, italiana, refogada	"	:	[	4.2	,	1.1	,	0.8	]	,
            "	Abobrinha, paulista, crua	"	:	[	7.9	,	0.6	,	0.1	]	,
            "	Acelga, crua	"	:	[	4.6	,	1.4	,	0.1	]	,
            "	Agrião, cru	"	:	[	2.3	,	2.7	,	0.2	]	,
            "	Aipo, cru	"	:	[	4.3	,	0.8	,	0.1	]	,
            "	Alface, americana, crua	"	:	[	1.7	,	0.6	,	0.1	]	,
            "	Alface, crespa, crua	"	:	[	1.7	,	1.3	,	0.2	]	,
            "	Alface, lisa, crua	"	:	[	2.4	,	1.7	,	0.1	]	,
            "	Alface, roxa, crua	"	:	[	2.5	,	0.9	,	0.2	]	,
            "	Alfavaca, crua	"	:	[	5.2	,	2.7	,	0.5	]	,
            "	Alho, cru	"	:	[	23.9	,	7.0	,	0.2	]	,
            "	Alho-poró, cru	"	:	[	6.9	,	1.4	,	0.1	]	,
            "	Almeirão, cru	"	:	[	3.3	,	1.8	,	0.2	]	,
            "	Almeirão, refogado	"	:	[	5.7	,	1.7	,	4.8	]	,
            "	Batata, baroa, cozida	"	:	[	18.9	,	0.9	,	0.2	]	,
            "	Batata, baroa, crua	"	:	[	24.0	,	1.0	,	0.2	]	,
            "	Batata, doce, cozida	"	:	[	18.4	,	0.6	,	0.1	]	,
            "	Batata, doce, crua	"	:	[	28.2	,	1.3	,	0.1	]	,
            "	Batata, frita, tipo chips, industrializada	"	:	[	51.2	,	5.6	,	36.6	]	,
            "	Batata, inglesa, cozida	"	:	[	11.9	,	1.2	,	0	]	,
            "	Batata, inglesa, crua	"	:	[	14.7	,	1.8	,	0	]	,
            "	Batata, inglesa, frita	"	:	[	35.6	,	5.0	,	13.1	]	,
            "	Batata, inglesa, sauté	"	:	[	14.1	,	1.3	,	0.9	]	,
            "	Berinjela, cozida	"	:	[	4.5	,	0.7	,	0.1	]	,
            "	Berinjela, crua	"	:	[	4.4	,	1.2	,	0.1	]	,
            "	Beterraba, cozida	"	:	[	7.2	,	1.3	,	0.1	]	,
            "	Beterraba, crua	"	:	[	11.1	,	1.9	,	0.1	]	,
            "	Biscoito, polvilho doce	"	:	[	80.5	,	1.3	,	12.2	]	,
            "	Brócolis, cozido	"	:	[	4.4	,	2.1	,	0.5	]	,
            "	Brócolis, cru	"	:	[	4.0	,	3.6	,	0.3	]	,
            "	Cará, cozido	"	:	[	18.9	,	1.5	,	0.1	]	,
            "	Cará, cru	"	:	[	23.0	,	2.3	,	0.1	]	,
            "	Caruru, cru	"	:	[	6.0	,	3.2	,	0.6	]	,
            "	Catalonha, crua	"	:	[	4.8	,	1.9	,	0.3	]	,
            "	Catalonha, refogada	"	:	[	4.8	,	2.0	,	4.8	]	,
            "	Cebola, crua	"	:	[	8.9	,	1.7	,	0.1	]	,
            "	Cebolinha, crua	"	:	[	3.4	,	1.9	,	0.4	]	,
            "	Cenoura, cozida	"	:	[	6.7	,	0.8	,	0.2	]	,
            "	Cenoura, crua	"	:	[	7.7	,	1.3	,	0.2	]	,
            "	Chicória, crua	"	:	[	2.9	,	1.1	,	0.1	]	,
            "	Chuchu, cozido	"	:	[	4.8	,	0.4	,	0	]	,
            "	Chuchu, cru	"	:	[	4.1	,	0.7	,	0.1	]	,
            "	Coentro, folhas desidratadas	"	:	[	48.0	,	20.9	,	10.4	]	,
            "	Couve, manteiga, crua	"	:	[	4.3	,	2.9	,	0.5	]	,
            "	Couve, manteiga, refogada 	"	:	[	8.7	,	1.7	,	6.6	]	,
            "	Couve-flor, crua	"	:	[	4.5	,	1.9	,	0.2	]	,
            "	Couve-flor, cozida	"	:	[	3.9	,	1.2	,	0.3	]	,
            "	Espinafre, Nova Zelândia, cru	"	:	[	2.6	,	2.0	,	0.2	]	,
            "	Espinafre, Nova Zelândia, refogado	"	:	[	4.2	,	2.7	,	5.4	]	,
            "	Farinha, de mandioca, crua	"	:	[	87.9	,	1.6	,	0.3	]	,
            "	Farinha, de mandioca, torrada	"	:	[	89.2	,	1.2	,	0.3	]	,
            "	Farinha, de puba	"	:	[	87.3	,	1.6	,	0.5	]	,
            "	Fécula, de mandioca	"	:	[	81.1	,	0.5	,	0.3	]	,
            "	Feijão, broto, cru	"	:	[	7.8	,	4.2	,	0.1	]	,
            "	Inhame, cru	"	:	[	23.2	,	2.1	,	0.2	]	,
            "	Jiló, cru	"	:	[	6.2	,	1.4	,	0.2	]	,
            "	Jurubeba, crua	"	:	[	23.1	,	4.4	,	3.9	]	,
            "	Mandioca, cozida	"	:	[	30.1	,	0.6	,	0.3	]	,
            "	Mandioca, crua	"	:	[	36.2	,	1.1	,	0.3	]	,
            "	Mandioca, farofa, temperada	"	:	[	80.3	,	2.1	,	9.1	]	,
            "	Mandioca, frita	"	:	[	50.3	,	1.4	,	11.2	]	,
            "	Manjericão, cru	"	:	[	3.6	,	2.0	,	0.4	]	,
            "	Maxixe, cru	"	:	[	2.7	,	1.4	,	0.1	]	,
            "	Mostarda, folha, crua	"	:	[	3.2	,	2.1	,	0.2	]	,
            "	Nhoque, batata, cozido	"	:	[	36.8	,	5.9	,	1.9	]	,
            "	Nabo, cru	"	:	[	4.1	,	1.2	,	0.1	]	,
            "	Palmito, juçara, em conserva	"	:	[	4.3	,	1.8	,	0.4	]	,
            "	Palmito, pupunha, em conserva	"	:	[	5.5	,	2.5	,	0.5	]	,
            "	Pão, de queijo, assado	"	:	[	34.2	,	5.1	,	24.6	]	,
            "	Pão, de queijo, cru	"	:	[	38.5	,	3.6	,	14.0	]	,
            "	Pepino, cru	"	:	[	2.0	,	0.9	,	0	]	,
            "	Pimentão, amarelo, cru	"	:	[	6.0	,	1.2	,	0.4	]	,
            "	Pimentão, verde, cru	"	:	[	4.9	,	1.1	,	0.2	]	,
            "	Pimentão, vermelho, cru	"	:	[	5.5	,	1.0	,	0.1	]	,
            "	Polvilho, doce	"	:	[	86.8	,	0.4	,	0	]	,
            "	Quiabo, cru	"	:	[	6.4	,	1.9	,	0.3	]	,
            "	Rabanete, cru	"	:	[	2.7	,	1.4	,	0.1	]	,
            "	Repolho, branco, cru	"	:	[	3.9	,	0.9	,	0.1	]	,
            "	Repolho, roxo, cru	"	:	[	7.2	,	1.9	,	0.1	]	,
            "	Repolho, roxo, refogado	"	:	[	7.6	,	1.8	,	1.2	]	,
            "	Rúcula, crua	"	:	[	2.2	,	1.8	,	0.1	]	,
            "	Salsa, crua	"	:	[	5.7	,	3.3	,	0.6	]	,
            "	Seleta de legumes, enlatada	"	:	[	12.7	,	3.4	,	0.4	]	,
            "	Serralha, crua	"	:	[	4.9	,	2.7	,	0.7	]	,
            "	Taioba, crua	"	:	[	5.4	,	2.9	,	0.9	]	,
            "	Tomate, com semente, cru	"	:	[	3.1	,	1.1	,	0.2	]	,
            "	Tomate, extrato	"	:	[	15.0	,	2.4	,	0.2	]	,
            "	Tomate, molho industrializado	"	:	[	7.7	,	1.4	,	0.9	]	,
            "	Tomate, purê	"	:	[	6.9	,	1.4	,	0	]	,
            "	Tomate, salada	"	:	[	5.1	,	0.8	,	0	]	,
            "	Vagem, crua	"	:	[	5.3	,	1.8	,	0.2	]	,
        },
        "Frutas e derivados": {
            "	Abacate, cru	"	:	[	6.0	,	1.2	,	8.4	]	,
            "	Abacaxi, cru	"	:	[	12.3	,	0.9	,	0.1	]	,
            "	Abacaxi, polpa, congelada	"	:	[	7.8	,	0.5	,	0.1	]	,
            "	Abiu, cru	"	:	[	14.9	,	0.8	,	0.7	]	,
            "	Açaí, polpa, com xarope de guaraná e glucose	"	:	[	21.5	,	0.7	,	3.7	]	,
            "	Açaí, polpa, congelada	"	:	[	6.2	,	0.8	,	3.9	]	,
            "	Acerola, crua	"	:	[	8.0	,	0.9	,	0.2	]	,
            "	Acerola, polpa, congelada	"	:	[	5.5	,	0.6	,	0	]	,
            "	Ameixa, calda, enlatada 	"	:	[	46.9	,	0.4	,	0	]	,
            "	Ameixa, crua	"	:	[	13.9	,	0.8	,	0	]	,
            "	Ameixa, em calda, enlatada, drenada 	"	:	[	47.7	,	1.0	,	0.3	]	,
            "	Atemóia, crua	"	:	[	25.3	,	1.0	,	0.3	]	,
            "	Banana, da terra, crua	"	:	[	33.7	,	1.4	,	0.2	]	,
            "	Banana, doce em barra	"	:	[	75.7	,	2.2	,	0.1	]	,
            "	Banana, figo, crua	"	:	[	27.8	,	1.1	,	0.1	]	,
            "	Banana, maçã, crua	"	:	[	22.3	,	1.8	,	0.1	]	,
            "	Banana, nanica, crua	"	:	[	23.8	,	1.4	,	0.1	]	,
            "	Banana, ouro, crua	"	:	[	29.3	,	1.5	,	0.2	]	,
            "	Banana, pacova, crua	"	:	[	20.3	,	1.2	,	0.1	]	,
            "	Banana, prata, crua	"	:	[	26.0	,	1.3	,	0.1	]	,
            "	Cacau, cru	"	:	[	19.4	,	1.0	,	0.1	]	,
            "	Cajá-Manga, cru	"	:	[	11.4	,	1.3	,	0	]	,
            "	Cajá, polpa, congelada	"	:	[	6.4	,	0.6	,	0.2	]	,
            "	Caju, cru	"	:	[	10.3	,	1.0	,	0.3	]	,
            "	Caju, polpa, congelada	"	:	[	9.4	,	0.5	,	0.2	]	,
            "	Caju, suco concentrado, envasado	"	:	[	10.7	,	0.4	,	0.2	]	,
            "	Caqui, chocolate, cru	"	:	[	19.3	,	0.4	,	0.1	]	,
            "	Carambola, crua	"	:	[	11.5	,	0.9	,	0.2	]	,
            "	Ciriguela, crua	"	:	[	18.9	,	1.4	,	0.4	]	,
            "	Cupuaçu, cru	"	:	[	10.4	,	1.2	,	1.0	]	,
            "	Cupuaçu, polpa, congelada	"	:	[	11.4	,	0.8	,	0.6	]	,
            "	Figo, cru	"	:	[	10.2	,	1.0	,	0.2	]	,
            "	Figo, enlatado, em calda	"	:	[	50.3	,	0.6	,	0.2	]	,
            "	Fruta-pão, crua	"	:	[	17.2	,	1.1	,	0.2	]	,
            "	Goiaba, branca, com casca, crua	"	:	[	12.4	,	0.9	,	0.5	]	,
            "	Goiaba, doce em pasta	"	:	[	74.1	,	0.6	,	0.0	]	,
            "	Goiaba, doce, cascão	"	:	[	78.7	,	0.4	,	0.1	]	,
            "	Goiaba, vermelha, com casca, crua	"	:	[	13.0	,	1.1	,	0.4	]	,
            "	Graviola, crua	"	:	[	15.8	,	0.8	,	0.2	]	,
            "	Graviola, polpa, congelada	"	:	[	9.8	,	0.6	,	0.1	]	,
            "	Jabuticaba, crua	"	:	[	15.3	,	0.6	,	0.1	]	,
            "	Jaca, crua	"	:	[	22.5	,	1.4	,	0.3	]	,
            "	Jambo, cru	"	:	[	6.5	,	0.9	,	0.1	]	,
            "	Jamelão, cru	"	:	[	10.6	,	0.5	,	0.1	]	,
            "	Kiwi, cru	"	:	[	11.5	,	1.3	,	0.6	]	,
            "	Laranja, baía, crua	"	:	[	11.5	,	1.0	,	0.1	]	,
            "	Laranja, baía, suco	"	:	[	8.7	,	0.7	,	0	]	,
            "	Laranja, da terra, crua	"	:	[	12.9	,	1.1	,	0.2	]	,
            "	Laranja, da terra, suco	"	:	[	9.6	,	0.7	,	0.1	]	,
            "	Laranja, lima, crua	"	:	[	11.5	,	1.1	,	0.1	]	,
            "	Laranja, lima, suco	"	:	[	9.2	,	0.7	,	0.1	]	,
            "	Laranja, pêra, crua	"	:	[	8.9	,	1.0	,	0.1	]	,
            "	Laranja, pêra, suco	"	:	[	7.6	,	0.7	,	0.1	]	,
            "	Laranja, valência, crua	"	:	[	11.7	,	0.8	,	0.2	]	,
            "	Laranja, valência, suco	"	:	[	8.6	,	0.5	,	0.1	]	,
            "	Limão, cravo, suco	"	:	[	5.2	,	0.3	,	0	]	,
            "	Limão, galego, suco	"	:	[	7.3	,	0.6	,	0.1	]	,
            "	Limão, tahiti, cru	"	:	[	11.1	,	0.9	,	0.1	]	,
            "	Maçã, Argentina, com casca, crua	"	:	[	16.6	,	0.2	,	0.2	]	,
            "	Maçã, Fuji, com casca, crua	"	:	[	15.2	,	0.3	,	0	]	,
            "	Macaúba, crua	"	:	[	13.9	,	2.1	,	40.7	]	,
            "	 Mamão, doce em calda, drenado	"	:	[	54.0	,	0.2	,	0.1	]	,
            "	Mamão, Formosa, cru	"	:	[	11.6	,	0.8	,	0.1	]	,
            "	Mamão, Papaia, cru	"	:	[	10.4	,	0.5	,	0.1	]	,
            "	 Mamão verde, doce em calda, drenado	"	:	[	57.6	,	0.3	,	0.1	]	,
            "	Manga, Haden, crua	"	:	[	16.7	,	0.4	,	0.3	]	,
            "	Manga, Palmer, crua	"	:	[	19.4	,	0.4	,	0.2	]	,
            "	Manga, polpa, congelada	"	:	[	12.5	,	0.4	,	0.2	]	,
            "	Manga, Tommy Atkins, crua	"	:	[	12.8	,	0.9	,	0.2	]	,
            "	Maracujá, cru	"	:	[	12.3	,	2.0	,	2.1	]	,
            "	Maracujá, polpa, congelada	"	:	[	9.6	,	0.8	,	0.2	]	,
            "	Maracujá, suco concentrado, envasado	"	:	[	9.6	,	0.8	,	0.2	]	,
            "	Melancia, crua	"	:	[	8.1	,	0.9	,	0	]	,
            "	Melão, cru	"	:	[	7.5	,	0.7	,	0	]	,
            "	Mexerica, Murcote, crua	"	:	[	14.9	,	0.9	,	0.1	]	,
            "	Mexerica, Rio, crua	"	:	[	9.3	,	0.7	,	0.1	]	,
            "	Morango, cru	"	:	[	6.8	,	0.9	,	0.3	]	,
            "	Nêspera, crua	"	:	[	11.5	,	0.3	,	0	]	,
            "	Pequi, cru	"	:	[	13.0	,	2.3	,	18.0	]	,
            "	Pêra, Park, crua	"	:	[	16.1	,	0.2	,	0.2	]	,
            "	Pêra, Williams, crua	"	:	[	14.0	,	0.6	,	0.1	]	,
            "	Pêssego, Aurora, cru	"	:	[	9.3	,	0.8	,	0	]	,
            "	Pêssego, enlatado, em calda	"	:	[	16.9	,	0.7	,	0	]	,
            "	Pinha, crua	"	:	[	22.4	,	1.5	,	0.3	]	,
            "	Pitanga, crua	"	:	[	10.2	,	0.9	,	0.2	]	,
            "	Pitanga, polpa, congelada	"	:	[	4.8	,	0.3	,	0.1	]	,
            "	Romã, crua	"	:	[	15.1	,	0.4	,	0	]	,
            "	Tamarindo, cru	"	:	[	72.5	,	3.2	,	0.5	]	,
            "	Tangerina, Poncã, crua	"	:	[	9.6	,	0.8	,	0.1	]	,
            "	Tangerina, Poncã, suco	"	:	[	8.8	,	0.5	,	0	]	,
            "	Tucumã, cru	"	:	[	26.5	,	2.1	,	19.1	]	,
            "	Umbu, cru	"	:	[	9.4	,	0.8	,	0	]	,
            "	Umbu, polpa, congelada	"	:	[	8.8	,	0.5	,	0.1	]	,
            "	Uva, Itália, crua	"	:	[	13.6	,	0.7	,	0.2	]	,
            "	Uva, Rubi, crua	"	:	[	12.7	,	0.6	,	0.2	]	,
            "	Uva, suco concentrado, envasado	"	:	[	14.7	,	0	,	0	]	,
        },
        "Gorduras e Óleos": {
            "	Azeite, de dendê	"	:	[	0	,	0	,	100.0	]	,
            "	Azeite, de oliva, extra virgem	"	:	[	0	,	0	,	100.0	]	,
            "	Manteiga, com sal	"	:	[	0.1	,	0.4	,	82.4	]	,
            "	Manteiga, sem sal	"	:	[	0.0	,	0.4	,	86.0	]	,
            "	Margarina, com óleo hidrogenado, com sal (65% de lipídeos)	"	:	[	0.0	,	0	,	67.4	]	,
            "	Margarina, com óleo hidrogenado, sem sal (80% de lipídeos)	"	:	[	0.0	,	0	,	81.7	]	,
            "	Margarina, com óleo interesterificado, com sal (65%de lipídeos)	"	:	[	0.0	,	0	,	67.2	]	,
            "	Margarina, com óleo interesterificado, sem sal (65% de lipídeos)	"	:	[	0.0	,	0	,	67.1	]	,
            "	Óleo, de babaçu	"	:	[	0	,	0	,	100.0	]	,
            "	Óleo, de canola	"	:	[	0	,	0	,	100.0	]	,
            "	Óleo, de girassol	"	:	[	0	,	0	,	100.0	]	,
            "	Óleo, de milho	"	:	[	0	,	0	,	100.0	]	,
            "	Óleo, de pequi	"	:	[	0	,	0	,	100.0	]	,
            "	Óleo, de soja	"	:	[	0	,	0	,	100.0	]	,
        },
        "Pescados e Frutos do mar": {
            "	Abadejo, filé, congelado, assado	"	:	[	0.0	,	23.5	,	1.2	]	,
            "	Abadejo, filé, congelado,cozido	"	:	[	0.0	,	19.3	,	0.9	]	,
            "	Abadejo, filé, congelado, cru	"	:	[	0.0	,	13.1	,	0.4	]	,
            "	Abadejo, filé, congelado, grelhado	"	:	[	0.0	,	27.6	,	1.3	]	,
            "	Atum, conserva em óleo	"	:	[	0.0	,	26.2	,	6.0	]	,
            "	Atum, fresco, cru	"	:	[	0.0	,	25.7	,	0.9	]	,
            "	Bacalhau, salgado, cru	"	:	[	0.0	,	29.0	,	1.3	]	,
            "	Bacalhau, salgado, refogado	"	:	[	1.2	,	24.0	,	3.6	]	,
            "	Cação, posta, com farinha de trigo, frita	"	:	[	3.1	,	25.0	,	10.0	]	,
            "	Cação, posta, cozida	"	:	[	0.0	,	25.6	,	0.7	]	,
            "	Cação, posta, crua	"	:	[	0.0	,	17.9	,	0.8	]	,
            "	Camarão, Rio Grande, grande, cozido	"	:	[	0.0	,	19.0	,	1.0	]	,
            "	Camarão, Rio Grande, grande, cru	"	:	[	0.0	,	10.0	,	0.5	]	,
            "	Camarão, Sete Barbas, sem cabeça, com casca, frito	"	:	[	2.9	,	18.4	,	15.6	]	,
            "	Caranguejo, cozido	"	:	[	0.0	,	18.5	,	0.4	]	,
            "	Corimba, cru	"	:	[	0.0	,	17.4	,	6.0	]	,
            "	Corimbatá, assado	"	:	[	0.0	,	19.9	,	19.6	]	,
            "	Corimbatá, cozido	"	:	[	0.0	,	20.1	,	16.9	]	,
            "	Corvina de água doce, crua	"	:	[	0.0	,	18.9	,	2.2	]	,
            "	Corvina do mar, crua	"	:	[	0.0	,	18.6	,	1.6	]	,
            "	Corvina grande, assada	"	:	[	0.0	,	26.8	,	3.6	]	,
            "	Corvina grande, cozida	"	:	[	0.0	,	23.4	,	2.6	]	,
            "	Dourada de água doce, fresca	"	:	[	0.0	,	18.8	,	5.6	]	,
            "	Lambari, congelado, cru	"	:	[	0.0	,	16.8	,	6.5	]	,
            "	Lambari, congelado, frito	"	:	[	0.0	,	28.4	,	22.8	]	,
            "	Lambari, fresco, cru	"	:	[	0.0	,	15.7	,	9.4	]	,
            "	Manjuba, com farinha de trigo, frita	"	:	[	10.2	,	23.5	,	22.6	]	,
            "	Manjuba, frita	"	:	[	0.0	,	30.1	,	24.5	]	,
            "	Merluza, filé, assado	"	:	[	0.0	,	26.6	,	0.9	]	,
            "	Merluza, filé, cru	"	:	[	0.0	,	16.6	,	2.0	]	,
            "	Merluza, filé, frito	"	:	[	0.0	,	26.9	,	8.5	]	,
            "	Pescada, branca, crua	"	:	[	0.0	,	16.3	,	4.6	]	,
            "	Pescada, branca, frita	"	:	[	0.0	,	27.4	,	11.8	]	,
            "	Pescada, filé, com farinha de trigo, frito	"	:	[	5.0	,	21.4	,	19.1	]	,
            "	Pescada, filé, cru	"	:	[	0.0	,	16.7	,	4.0	]	,
            "	Pescada, filé, frito	"	:	[	0.0	,	28.6	,	3.6	]	,
            "	Pescada, filé, molho escabeche	"	:	[	5.0	,	11.8	,	8.0	]	,
            "	Pescadinha, crua	"	:	[	0.0	,	15.5	,	1.1	]	,
            "	Pintado, assado	"	:	[	0.0	,	36.5	,	4.0	]	,
            "	Pintado, cru	"	:	[	0.0	,	18.6	,	1.3	]	,
            "	Pintado, grelhado	"	:	[	0.0	,	30.8	,	2.3	]	,
            "	Porquinho, cru	"	:	[	0.0	,	20.5	,	0.6	]	,
            "	Salmão, filé, com pele, fresco,  grelhado	"	:	[	0.0	,	23.9	,	14.0	]	,
            "	Salmão, sem pele, fresco, cru	"	:	[	0.0	,	19.3	,	9.7	]	,
            "	Salmão, sem pele, fresco, grelhado	"	:	[	0.0	,	26.1	,	14.5	]	,
            "	Sardinha, assada	"	:	[	0.0	,	32.2	,	3.0	]	,
            "	Sardinha, conserva em óleo	"	:	[	0.0	,	15.9	,	24.0	]	,
            "	Sardinha, frita	"	:	[	0.0	,	33.4	,	12.7	]	,
            "	Sardinha, inteira, crua	"	:	[	0.0	,	21.1	,	2.7	]	,
            "	Tucunaré, filé, congelado, cru	"	:	[	0.0	,	18.0	,	1.2	]	,
        },
        "Carnes e derivados": {
            "	Apresuntado	"	:	[	2.9	,	13.5	,	6.7	]	,
            "	Caldo de carne, tablete	"	:	[	15.1	,	7.8	,	16.6	]	,
            "	Caldo de galinha, tablete	"	:	[	10.6	,	6.3	,	20.4	]	,
            "	Carne, bovina, acém, moído, cozido	"	:	[	0.0	,	26.7	,	10.9	]	,
            "	Carne, bovina, acém, moído, cru	"	:	[	0.0	,	19.4	,	5.9	]	,
            "	Carne, bovina, acém, sem gordura, cozido	"	:	[	0.0	,	27.3	,	10.9	]	,
            "	Carne, bovina, acém, sem gordura, cru	"	:	[	0.0	,	20.8	,	6.1	]	,
            "	Carne, bovina, almôndegas, cruas	"	:	[	9.8	,	12.3	,	11.2	]	,
            "	Carne, bovina, almôndegas, fritas	"	:	[	14.3	,	18.2	,	15.8	]	,
            "	Carne, bovina, bucho, cozido	"	:	[	0.0	,	21.6	,	4.5	]	,
            "	Carne, bovina, bucho, cru	"	:	[	0.0	,	20.5	,	5.5	]	,
            "	Carne, bovina, capa de contra-filé, com gordura, crua	"	:	[	0.0	,	19.2	,	15.0	]	,
            "	Carne, bovina, capa de contra-filé, com gordura, grelhada	"	:	[	0.0	,	30.7	,	20.0	]	,
            "	Carne, bovina, capa de contra-filé, sem gordura, crua	"	:	[	0.0	,	21.5	,	4.3	]	,
            "	Carne, bovina, capa de contra-filé, sem gordura, grelhada	"	:	[	0.0	,	35.1	,	10.0	]	,
            "	Carne, bovina, charque, cozido	"	:	[	0.0	,	36.4	,	11.9	]	,
            "	Carne, bovina, charque, cru	"	:	[	0.0	,	22.7	,	16.8	]	,
            "	Carne, bovina, contra-filé, à milanesa	"	:	[	12.2	,	20.6	,	24.0	]	,
            "	Carne, bovina, contra-filé de costela, cru	"	:	[	0.0	,	19.8	,	13.1	]	,
            "	Carne, bovina, contra-filé de costela, grelhado	"	:	[	0.0	,	29.9	,	16.3	]	,
            "	Carne, bovina, contra-filé, com gordura, cru	"	:	[	0.0	,	21.2	,	12.8	]	,
            "	Carne, bovina, contra-filé, com gordura, grelhado	"	:	[	0.0	,	32.4	,	15.5	]	,
            "	Carne, bovina, contra-filé, sem gordura, cru	"	:	[	0.0	,	24.0	,	6.0	]	,
            "	Carne, bovina, contra-filé, sem gordura, grelhado	"	:	[	0.0	,	35.9	,	4.5	]	,
            "	Carne, bovina, costela, assada	"	:	[	0.0	,	28.8	,	27.7	]	,
            "	Carne, bovina, costela, crua	"	:	[	0.0	,	16.7	,	31.8	]	,
            "	Carne, bovina, coxão duro, sem gordura, cozido	"	:	[	0.0	,	31.9	,	8.9	]	,
            "	Carne, bovina, coxão duro, sem gordura, cru	"	:	[	0.0	,	21.5	,	6.2	]	,
            "	Carne, bovina, coxão mole, sem gordura, cozido	"	:	[	0.0	,	32.4	,	8.9	]	,
            "	Carne, bovina, coxão mole, sem gordura, cru	"	:	[	0.0	,	21.2	,	8.7	]	,
            "	Carne, bovina, cupim, assado	"	:	[	0.0	,	28.6	,	23.0	]	,
            "	Carne, bovina, cupim, cru	"	:	[	0.0	,	19.5	,	15.3	]	,
            "	Carne, bovina, fígado, cru	"	:	[	1.1	,	20.7	,	5.4	]	,
            "	Carne, bovina, fígado, grelhado	"	:	[	4.2	,	29.9	,	9.0	]	,
            "	Carne, bovina, filé mingnon, sem gordura, cru	"	:	[	0.0	,	21.6	,	5.6	]	,
            "	Carne, bovina, filé mingnon, sem gordura, grelhado	"	:	[	0.0	,	32.8	,	8.8	]	,
            "	Carne, bovina, flanco, sem gordura, cozido	"	:	[	0.0	,	29.4	,	7.8	]	,
            "	Carne, bovina, flanco, sem gordura, cru	"	:	[	0.0	,	20.0	,	6.2	]	,
            "	Carne, bovina, fraldinha, com gordura, cozida	"	:	[	0.0	,	24.2	,	26.0	]	,
            "	Carne, bovina, fraldinha, com gordura, crua	"	:	[	0.0	,	17.6	,	16.1	]	,
            "	Carne, bovina, lagarto, cozido	"	:	[	0.0	,	32.9	,	9.1	]	,
            "	Carne, bovina, lagarto, cru	"	:	[	0.0	,	20.5	,	5.2	]	,
            "	Carne, bovina, língua, cozida	"	:	[	0.0	,	21.4	,	24.8	]	,
            "	Carne, bovina, língua, crua	"	:	[	0.0	,	17.1	,	15.8	]	,
            "	Carne, bovina, maminha, crua	"	:	[	0.0	,	20.9	,	7.0	]	,
            "	Carne, bovina, maminha, grelhada	"	:	[	0.0	,	30.7	,	2.4	]	,
            "	Carne, bovina, miolo de alcatra, sem gordura, cru	"	:	[	0.0	,	21.6	,	7.8	]	,
            "	Carne, bovina, miolo de alcatra, sem gordura, grelhado	"	:	[	0.0	,	31.9	,	11.6	]	,
            "	Carne, bovina, músculo, sem gordura, cozido	"	:	[	0.0	,	31.2	,	6.7	]	,
            "	Carne, bovina, músculo, sem gordura, cru	"	:	[	0.0	,	21.6	,	5.5	]	,
            "	Carne, bovina, paleta, com gordura, crua	"	:	[	0.0	,	21.4	,	7.5	]	,
            "	Carne, bovina, paleta, sem gordura, cozida	"	:	[	0.0	,	29.7	,	7.4	]	,
            "	Carne, bovina, paleta, sem gordura, crua	"	:	[	0.0	,	21.0	,	5.7	]	,
            "	Carne, bovina, patinho, sem gordura, cru	"	:	[	0.0	,	21.7	,	4.5	]	,
            "	Carne, bovina, patinho, sem gordura, grelhado	"	:	[	0.0	,	35.9	,	7.3	]	,
            "	Carne, bovina, peito, sem gordura, cozido	"	:	[	0.0	,	22.2	,	27.0	]	,
            "	Carne, bovina, peito, sem gordura, cru	"	:	[	0.0	,	17.6	,	20.4	]	,
            "	Carne, bovina, picanha, com gordura, crua	"	:	[	0.0	,	18.8	,	14.7	]	,
            "	Carne, bovina, picanha, com gordura, grelhada	"	:	[	0.0	,	26.4	,	19.5	]	,
            "	Carne, bovina, picanha, sem gordura, crua	"	:	[	0.0	,	21.3	,	4.7	]	,
            "	Carne, bovina, picanha, sem gordura, grelhada	"	:	[	0.0	,	31.9	,	11.3	]	,
            "	Carne, bovina, seca, cozida	"	:	[	0.0	,	26.9	,	21.9	]	,
            "	Carne, bovina, seca, crua	"	:	[	0.0	,	19.7	,	25.4	]	,
            "	Coxinha de frango, frita	"	:	[	34.5	,	9.6	,	11.8	]	,
            "	Croquete, de carne, cru	"	:	[	13.9	,	12.0	,	15.6	]	,
            "	Croquete, de carne, frito	"	:	[	18.1	,	16.9	,	22.7	]	,
            "	Empada de frango, pré-cozida, assada	"	:	[	47.5	,	6.9	,	15.6	]	,
            "	Empada, de frango, pré-cozida	"	:	[	35.5	,	7.3	,	22.9	]	,
            "	Frango, asa, com pele, crua	"	:	[	0.0	,	18.1	,	15.1	]	,
            "	Frango, caipira, inteiro, com pele, cozido	"	:	[	0.0	,	23.9	,	15.6	]	,
            "	Frango, caipira, inteiro, sem pele, cozido	"	:	[	0.0	,	29.6	,	7.7	]	,
            "	Frango, coração, cru	"	:	[	0.0	,	12.6	,	18.6	]	,
            "	Frango, coração, grelhado	"	:	[	0.6	,	22.4	,	12.1	]	,
            "	Frango, coxa, com pele, assada	"	:	[	0.1	,	28.5	,	10.4	]	,
            "	Frango, coxa, com pele, crua	"	:	[	0.0	,	17.1	,	9.8	]	,
            "	Frango, coxa, sem pele, cozida	"	:	[	0.0	,	26.9	,	5.8	]	,
            "	Frango, coxa, sem pele, crua	"	:	[	0.0	,	17.8	,	4.9	]	,
            "	Frango, fígado, cru	"	:	[	0.0	,	17.6	,	3.5	]	,
            "	Frango, filé, à milanesa	"	:	[	7.5	,	28.5	,	7.8	]	,
            "	Frango, inteiro, com pele, cru	"	:	[	0.0	,	16.4	,	17.3	]	,
            "	Frango, inteiro, sem pele, assado	"	:	[	0.0	,	28.0	,	7.5	]	,
            "	Frango, inteiro, sem pele, cozido	"	:	[	0.0	,	25.0	,	7.1	]	,
            "	Frango, inteiro, sem pele, cru	"	:	[	0.0	,	20.6	,	4.6	]	,
            "	Frango, peito, com pele, assado	"	:	[	0.0	,	33.4	,	7.6	]	,
            "	Frango, peito, com pele, cru	"	:	[	0.0	,	20.8	,	6.7	]	,
            "	Frango, peito, sem pele, cozido	"	:	[	0.0	,	31.5	,	3.2	]	,
            "	Frango, peito, sem pele, cru	"	:	[	0.0	,	21.5	,	3.0	]	,
            "	Frango, peito, sem pele, grelhado	"	:	[	0.0	,	32.0	,	2.5	]	,
            "	Frango, sobrecoxa, com pele, assada	"	:	[	0.0	,	28.7	,	15.2	]	,
            "	Frango, sobrecoxa, com pele, crua	"	:	[	0.0	,	15.5	,	20.9	]	,
            "	Frango, sobrecoxa, sem pele, assada	"	:	[	0.0	,	29.2	,	12.0	]	,
            "	Frango, sobrecoxa, sem pele, crua	"	:	[	0.0	,	17.6	,	9.6	]	,
            "	Hambúrguer, bovino, cru	"	:	[	4.2	,	13.2	,	16.2	]	,
            "	Hambúrguer, bovino, frito	"	:	[	6.3	,	20.0	,	17.0	]	,
            "	Hambúrguer, bovino, grelhado	"	:	[	11.3	,	13.2	,	12.4	]	,
            "	Lingüiça, frango, crua	"	:	[	0.0	,	14.2	,	17.4	]	,
            "	Lingüiça, frango, frita	"	:	[	0.0	,	18.3	,	18.5	]	,
            "	Lingüiça, frango, grelhada	"	:	[	0.0	,	18.2	,	18.4	]	,
            "	Lingüiça, porco, crua	"	:	[	0.0	,	16.1	,	17.6	]	,
            "	Lingüiça, porco, frita	"	:	[	0.0	,	20.5	,	21.3	]	,
            "	Lingüiça, porco, grelhada	"	:	[	0.0	,	23.2	,	21.9	]	,
            "	Mortadela	"	:	[	5.8	,	12.0	,	21.6	]	,
            "	Peru, congelado, assado	"	:	[	0.0	,	26.2	,	5.7	]	,
            "	Peru, congelado, cru	"	:	[	0.0	,	18.1	,	1.8	]	,
            "	Porco, bisteca, crua	"	:	[	0.0	,	21.5	,	8.0	]	,
            "	Porco, bisteca, frita	"	:	[	0.0	,	33.7	,	18.5	]	,
            "	Porco, bisteca, grelhada	"	:	[	0.0	,	28.9	,	17.4	]	,
            "	Porco, costela, assada	"	:	[	0.0	,	30.2	,	30.3	]	,
            "	Porco, costela, crua	"	:	[	0.0	,	18.0	,	19.8	]	,
            "	Porco, lombo, assado	"	:	[	0.0	,	35.7	,	6.4	]	,
            "	Porco, lombo, cru	"	:	[	0.0	,	22.6	,	8.8	]	,
            "	Porco, orelha, salgada, crua	"	:	[	0.0	,	18.5	,	19.9	]	,
            "	Porco, pernil, assado	"	:	[	0.0	,	32.1	,	13.9	]	,
            "	Porco, pernil, cru	"	:	[	0.0	,	20.1	,	11.1	]	,
            "	Porco, rabo, salgado, cru	"	:	[	0.0	,	15.6	,	34.5	]	,
            "	Presunto, com capa de gordura	"	:	[	1.4	,	14.4	,	6.8	]	,
            "	Presunto, sem capa de gordura	"	:	[	2.1	,	14.3	,	2.7	]	,
            "	Quibe, assado	"	:	[	12.9	,	14.6	,	2.7	]	,
            "	Quibe, cru	"	:	[	10.8	,	12.4	,	1.7	]	,
            "	Quibe, frito	"	:	[	12.3	,	14.9	,	15.8	]	,
            "	Salame	"	:	[	2.9	,	25.8	,	30.6	]	,
            "	Toucinho, cru	"	:	[	0.0	,	11.5	,	60.3	]	,
            "	Toucinho, frito	"	:	[	0.0	,	27.3	,	64.3	]	,
        },
    "Leite e derivados": {
    "	Bebida láctea, pêssego	"	:	[	7.6	,	2.1	,	1.9	]	,
    "	Creme de Leite	"	:	[	4.5	,	1.5	,	22.5	]	,
    "	Iogurte, natural	"	:	[	1.9	,	4.1	,	3.0	]	,
    "	Iogurte, natural, desnatado	"	:	[	5.8	,	3.8	,	0.3	]	,
    "	Iogurte, sabor morango	"	:	[	9.7	,	2.7	,	2.3	]	,
    "	Iogurte, sabor pêssego	"	:	[	9.4	,	2.5	,	2.3	]	,
    "	Leite, condensado	"	:	[	57.0	,	7.7	,	6.7	]	,
    "	Leite, de cabra	"	:	[	5.2	,	3.1	,	3.8	]	,
    "	Leite, de vaca, achocolatado	"	:	[	14.2	,	2.1	,	2.2	]	,
    "	Leite, de vaca, desnatado, pó	"	:	[	53.0	,	34.7	,	0.9	]	,
    "	Leite, de vaca, integral	"	:	[	5	,	3.1	,	3.5	]	,
    "	Leite, de vaca, integral, pó	"	:	[	39.2	,	25.4	,	26.9	]	,
    "	Leite, fermentado	"	:	[	15.7	,	1.9	,	0.1	]	,
    "	Queijo, minas, frescal	"	:	[	3.2	,	17.4	,	20.2	]	,
    "	Queijo, minas, meia cura	"	:	[	3.6	,	21.2	,	24.6	]	,
    "	Queijo, mozarela	"	:	[	3.0	,	22.6	,	25.2	]	,
    "	Queijo, parmesão	"	:	[	1.7	,	35.6	,	33.5	]	,
    "	Queijo, pasteurizado	"	:	[	5.7	,	9.4	,	27.4	]	,
    "	Queijo, petit suisse, morango	"	:	[	18.5	,	5.8	,	2.8	]	,
    "	Queijo, prato	"	:	[	1.9	,	22.7	,	29.1	]	,
    "	Queijo, requeijão, cremoso	"	:	[	2.4	,	9.6	,	23.4	]	,
    "	Queijo, ricota	"	:	[	3.8	,	12.6	,	8.1	]	,
    
    
    },
    "Bebidas (alcoólicas e não alcoólicas)": {
    "	Bebida isotônica, sabores variados	"	:	[	6.4	,	0.0	,	0.0	]	,
    "	Café, infusão 10%	"	:	[	1.5	,	0.7	,	0.1	]	,
    "	Cana, caldo de	"	:	[	18.2	,	0	,	0	]	,
    "	Cerveja, pilsen 2	"	:	[	3.3	,	0.6	,	0	]	,
    "	Chá, erva-doce, infusão 5%	"	:	[	0.4	,	0.0	,	0.0	]	,
    "	Chá, mate, infusão 5%	"	:	[	0.6	,	0.0	,	0.1	]	,
    "	Chá, preto, infusão 5%	"	:	[	0.6	,	0.0	,	0.0	]	,
    "	Coco, água de	"	:	[	5.3	,	0.0	,	0.0	]	,
    "	Refrigerante, tipo água tônica	"	:	[	8.0	,	0.0	,	0.0	]	,
    "	Refrigerante, tipo cola	"	:	[	8.7	,	0.0	,	0.0	]	,
    "	Refrigerante, tipo guaraná	"	:	[	10.0	,	0.0	,	0.0	]	,
    "	Refrigerante, tipo laranja	"	:	[	11.8	,	0.0	,	0.0	]	,
    "	Refrigerante, tipo limão	"	:	[	10.3	,	0.0	,	0.0	]	,
    
    
    },
    "Ovos e derivados": {
    "	Omelete, de queijo	"	:	[	0.4	,	15.6	,	22.0	]	,
    "	Ovo, de codorna, inteiro, cru	"	:	[	0.8	,	13.7	,	12.7	]	,
    "	Ovo, de galinha, clara, cozida/10minutos	"	:	[	0.0	,	13.4	,	0.1	]	,
    "	Ovo, de galinha, gema, cozida/10minutos	"	:	[	1.6	,	15.9	,	30.8	]	,
    "	Ovo, de galinha, inteiro, cozido/10minutos	"	:	[	0.6	,	13.3	,	9.5	]	,
    "	Ovo, de galinha, inteiro, cru	"	:	[	1.6	,	13.0	,	8.9	]	,
    "	Ovo, de galinha, inteiro, frito	"	:	[	1.2	,	15.6	,	18.6	]	,
    
    },
    "Produtos açucarados": {
    "	Achocolatado, pó	"	:	[	91.2	,	4.2	,	2.2	]	,
    "	Açúcar, cristal	"	:	[	99.6	,	0.3	,	0	]	,
    "	Açúcar, mascavo	"	:	[	94.5	,	0.8	,	0.1	]	,
    "	Açúcar, refinado	"	:	[	99.5	,	0.3	,	0	]	,
    "	Chocolate, ao leite	"	:	[	59.6	,	7.2	,	30.3	]	,
    "	Chocolate, ao leite, com castanha do Pará	"	:	[	55.4	,	7.4	,	34.2	]	,
    "	Chocolate, ao leite, dietético	"	:	[	56.3	,	6.9	,	33.8	]	,
    "	Chocolate, meio amargo	"	:	[	62.4	,	4.9	,	29.9	]	,
    "	Cocada branca	"	:	[	81.4	,	1.1	,	13.6	]	,
    "	Doce, de abóbora, cremoso	"	:	[	54.6	,	0.9	,	0.2	]	,
    "	Doce, de leite, cremoso	"	:	[	59.5	,	5.5	,	6.0	]	,
    "	Geléia, mocotó, natural	"	:	[	24.2	,	2.1	,	0.1	]	,
    "	Glicose de milho	"	:	[	79.4	,	0.0	,	0.0	]	,
    "	Maria mole	"	:	[	73.6	,	3.8	,	0.2	]	,
    "	Maria mole, coco queimado	"	:	[	75.1	,	3.9	,	0.1	]	,
    "	Marmelada	"	:	[	70.8	,	0.4	,	0.1	]	,
    "	Mel, de abelha	"	:	[	84.0	,	0.0	,	0.0	]	,
    "	Melado	"	:	[	76.6	,	0.0	,	0.0	]	,
    "	Quindim	"	:	[	46.3	,	4.7	,	24.4	]	,
    "	Rapadura	"	:	[	90.8	,	1.0	,	0.1	]	,
    
    },
    "Miscelâneas": {
    "	Café, pó, torrado	"	:	[	65.8	,	14.7	,	11.9	]	,
    "	Capuccino, pó	"	:	[	73.6	,	11.3	,	8.6	]	,
    "	Fermento em pó, químico	"	:	[	43.9	,	0.5	,	0.1	]	,
    "	Fermento, biológico, levedura, tablete	"	:	[	7.7	,	17.0	,	1.5	]	,
    "	Gelatina, sabores variados, pó	"	:	[	89.2	,	8.9	,	0	]	,
    "	Sal, dietético	"	:	[	0	,	0	,	0	]	,
    "	Sal, grosso	"	:	[	0	,	0	,	0	]	,
    "	Shoyu	"	:	[	11.6	,	3.3	,	0.3	]	,
    "	Tempero a base de sal	"	:	[	2.1	,	2.7	,	0.3	]	,
    
    },
    "Outros alimentos industrializados": {
    "	Azeitona, preta, conserva	"	:	[	5.5	,	1.2	,	20.3	]	,
    "	Azeitona, verde, conserva	"	:	[	4.1	,	0.9	,	14.2	]	,
    "	Chantilly, spray, com gordura vegetal	"	:	[	16.9	,	0.5	,	27.3	]	,
    "	Leite, de coco	"	:	[	2.2	,	1.0	,	18.4	]	,
    "	Maionese, tradicional com ovos	"	:	[	7.9	,	0.6	,	30.5	]	,
    
    },
    "Alimentos Preparados": {
    "	Acarajé	"	:	[	19.1	,	8.3	,	19.9	]	,
    "	Arroz carreteiro	"	:	[	11.6	,	10.8	,	7.1	]	,
    "	Baião de dois, arroz e feijão-de-corda	"	:	[	20.4	,	6.2	,	3.2	]	,
    "	Barreado	"	:	[	0.2	,	18.3	,	9.5	]	,
    "	Bife à cavalo, com contra filé	"	:	[	0.0	,	23.7	,	21.1	]	,
    "	Bolinho de arroz	"	:	[	41.7	,	8.0	,	8.3	]	,
    "	Camarão à baiana	"	:	[	3.2	,	7.9	,	6.0	]	,
    "	Charuto, de repolho	"	:	[	10.1	,	6.8	,	1.1	]	,
    "	Cuscuz, de milho, cozido com sal	"	:	[	25.3	,	2.2	,	0.7	]	,
    "	Cuscuz, paulista	"	:	[	22.5	,	2.6	,	4.6	]	,
    "	Cuxá, molho	"	:	[	5.7	,	5.6	,	3.6	]	,
    "	Dobradinha	"	:	[	0.0	,	19.8	,	4.4	]	,
    "	Estrogonofe de carne	"	:	[	3.0	,	15.0	,	10.8	]	,
    "	Estrogonofe de frango	"	:	[	2.6	,	17.6	,	8.0	]	,
    "	Feijão tropeiro mineiro	"	:	[	19.6	,	10.2	,	6.8	]	,
    "	Feijoada	"	:	[	11.6	,	8.7	,	6.5	]	,
    "	Frango, com açafrão	"	:	[	4.1	,	9.7	,	6.2	]	,
    "	Macarrão, molho bolognesa	"	:	[	22.5	,	4.9	,	0.9	]	,
    "	Maniçoba	"	:	[	3.4	,	10.0	,	8.7	]	,
    "	Quibebe	"	:	[	6.6	,	8.6	,	2.7	]	,
    "	Salada, de legumes, com maionese	"	:	[	8.9	,	1.1	,	7.0	]	,
    "	Salada, de legumes, cozida no vapor	"	:	[	7.1	,	2.0	,	0.3	]	,
    "	Salpicão, de frango	"	:	[	4.6	,	13.9	,	7.8	]	,
    "	Sarapatel	"	:	[	1.1	,	18.5	,	4.4	]	,
    "	Tabule	"	:	[	10.6	,	2.0	,	1.2	]	,
    "	Tacacá	"	:	[	3.4	,	7.0	,	0.4	]	,
    "	Tapioca, com manteiga	"	:	[	63.6	,	0.1	,	10.9	]	,
    "	Tucupi, com pimenta-de-cheiro	"	:	[	4.7	,	2.1	,	0.3	]	,
    "	Vaca atolada	"	:	[	10.1	,	5.1	,	9.3	]	,
    "	Vatapá	"	:	[	9.7	,	6.0	,	23.2	]	,
    "	Virado à paulista	"	:	[	14.1	,	10.2	,	25.6	]	,
    "	Yakisoba	"	:	[	18.3	,	7.5	,	2.6	]	,
    
    
    },
    "Leguminosas e derivados": {
       "	Amendoim, grão, cru	"	:	[	20.3	,	27.2	,	43.9	]	,
    "	Amendoim, torrado, salgado	"	:	[	18.7	,	22.5	,	54.0	]	,
    "	Ervilha, em vagem	"	:	[	14.2	,	7.5	,	0.5	]	,
    "	Ervilha, enlatada, drenada	"	:	[	13.4	,	4.6	,	0.4	]	,
    "	Feijão, carioca, cozido	"	:	[	13.6	,	4.8	,	0.5	]	,
    "	Feijão, carioca, cru	"	:	[	61.2	,	20.0	,	1.3	]	,
    "	Feijão, fradinho, cozido	"	:	[	13.5	,	5.1	,	0.6	]	,
    "	Feijão, fradinho, cru	"	:	[	61.2	,	20.2	,	2.4	]	,
    "	Feijão, jalo, cozido	"	:	[	16.5	,	6.1	,	0.5	]	,
    "	Feijão, jalo, cru	"	:	[	61.5	,	20.1	,	0.9	]	,
    "	Feijão, preto, cozido	"	:	[	14.0	,	4.5	,	0.5	]	,
    "	Feijão, preto, cru	"	:	[	58.8	,	21.3	,	1.2	]	,
    "	Feijão, rajado, cozido	"	:	[	15.3	,	5.5	,	0.4	]	,
    "	Feijão, rajado, cru	"	:	[	62.9	,	17.3	,	1.2	]	,
    "	Feijão, rosinha, cozido	"	:	[	11.8	,	4.5	,	0.5	]	,
    "	Feijão, rosinha, cru	"	:	[	62.2	,	20.9	,	1.3	]	,
    "	Feijão, roxo, cozido	"	:	[	12.9	,	5.7	,	0.5	]	,
    "	Feijão, roxo, cru	"	:	[	60.0	,	22.2	,	1.2	]	,
    "	Grão-de-bico, cru	"	:	[	57.9	,	21.2	,	5.4	]	,
    "	Guandu, cru	"	:	[	64.0	,	19.0	,	2.1	]	,
    "	Lentilha, cozida	"	:	[	16.3	,	6.3	,	0.5	]	,
    "	Lentilha, crua	"	:	[	62.0	,	23.2	,	0.8	]	,
    "	Paçoca, amendoim	"	:	[	52.4	,	16.0	,	26.1	]	,
    "	Pé-de-moleque, amendoim	"	:	[	54.7	,	13.2	,	28.0	]	,
    "	Soja, farinha	"	:	[	38.4	,	36.0	,	14.6	]	,
    "	Soja, extrato solúvel, natural, fluido	"	:	[	4.3	,	2.4	,	1.6	]	,
    "	Soja, extrato solúvel, pó	"	:	[	28.5	,	35.7	,	26.2	]	,
    "	Soja, queijo (tofu)	"	:	[	2.1	,	6.6	,	4.0	]	,
    "	0emoço, cru	"	:	[	43.8	,	33.6	,	10.3	]	,
    "	0emoço, em conserva	"	:	[	12.4	,	11.1	,	3.8	]	,
    
    },
    "Nozes e Sementes": {
    "	Amêndoa, torrada, salgada	"	:	[	29.5	,	18.6	,	47.3	]	,
    "	Castanha-de-caju, torrada, salgada	"	:	[	29.1	,	18.5	,	46.3	]	,
    "	Castanha-do-Brasil, crua	"	:	[	15.1	,	14.5	,	63.5	]	,
    "	Coco, cru	"	:	[	10.4	,	3.7	,	42.0	]	,
    "	Farinha, de mesocarpo de babaçu, crua	"	:	[	79.2	,	1.4	,	0.2	]	,
    "	Gergelim, semente	"	:	[	21.6	,	21.2	,	50.4	]	,
    "	Linhaça, semente	"	:	[	43.3	,	14.1	,	32.3	]	,
    "	Pinhão, cozido	"	:	[	43.9	,	3.0	,	0.7	]	,
    "	Pupunha, cozida	"	:	[	29.6	,	2.5	,	12.8	]	,
    "	Noz, crua	"	:	[	18.4	,	14.0	,	59.4	]	,
    
    }
    }
    return comidas
    
