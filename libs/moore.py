#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Escrito em Python V 3
#
# (C) João Carlos Pandolfi Santana
#
# Maquina de Moore.
# Se converte para maquina de Mealy
#
#####################################

#importa Classe pai
from libs import maquina

#classe Moore
class Moore(maquina.Maquina):

	#metodo construtor
	def __init__(self):
		super().__init__()
		self.transicao = [] # [[<estado>,<destino>,<condicao>]] #lista
		self.saidas = [] # [[<estado>,<saida>]] #lista


	def set_saidas(self,string_outs):
		#defino vazio como *
		string_outs = string_outs.replace("( )","*")
		string_outs = string_outs.replace("()","*")		
		#separo por transições
		tam = len(string_outs)
		i = 0
		buff = ""
		tagIn = False
		while(i < tam):
			if(string_outs[i] == '('):
				tagIn = True
				buff = ""
			elif(string_outs[i] == ')'):
				tagIn = False
				# se buff vazio, chegou ao fim
				if(buff == ""):
					break
				aux = self.custom_split(buff)
				self.saidas += [aux]
			elif(tagIn):
				buff +=string_outs[i]
			#incremento
			i+=1

	def change_machine(self):
		tam_transicao = len(self.transicao)
		
		#percorro a lista de saidas
		for saida in self.saidas:
			i = 0
			#percorro a lista de transicoes e adicono a saida
			while (i<tam_transicao):
				if(self.transicao[i][1] == saida[0] and len(self.transicao[i]) < 4): #<destino> == <estado> && <nao insere 2 vezes>
					self.transicao[i].append(saida[1])
				i += 1
