#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Escrito em Python V 3
#
# (C) João Carlos Pandolfi Santana
#
# Maquina de Mealy.
# Se converte para maquina de Moore
#
#####################################

#importa Classe Pai
from libs import maquina

#classe Mealy
class Mealy(maquina.Maquina):

	#metodo construtor
	def __init__(self):
		super().__init__()
		self.transicao = [] # [[<estado>,<destino>,<condicao>,<saidas>]] #lista

	def change_machine(self):
		estados_criados = [] # [<estado>]
		tam_transicao = len(self.transicao)
		i = 0
		while (i<tam_transicao):
			#recupero o estado
			aux = [self.transicao[i][1],self.transicao[i][3]] #[<destino>,<saida>]
			while(aux[0] in estados_criados and not(aux in self.saidas)):
				aux[0] = aux[0]+"'" #coloco ' no nome do estado
				if(self.transicao[i][1] in self.finais and not(aux[0] in self.finais)): # se quem deu origem for estado final
					self.finais.append(aux[0])
	
			if(not(aux in self.saidas)):
				self.saidas.append(aux)
				estados_criados.append(aux[0])
			
			self.transicao[i] = [self.transicao[i][0], aux[0],self.transicao[i][2]]
			#incremento
			i +=1
		#atualizo estados criados e estados finais
		self.estados = estados_criados