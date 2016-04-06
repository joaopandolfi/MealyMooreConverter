#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Escrito em Python V 3
#
# (C) João Carlos Pandolfi Santana

class Maquina():

	#metodo construtor
	def __init__(self):
		self.estados = [] # é uma lista
		self.inicial = [] # lista
		self.finais = [] # Lista
		self.transicao = [] # Lista
		self.simbolos_entrada = [] #lista
		self.simbolos_saida = [] #lista
		self.saidas = [] # [[<estado>,<saida>]] #lista

	def set_estados(self,estados,inicial,finais):
		self.estados = estados
		self.inicial = inicial
		self.finais = finais

	def set_simbolos(self,entrada,saida):
		self.simbolos_entrada = entrada
		self.simbolos_saida = saida

	def set_transitions(self,string_transitions):
		#separo por transições
		tam = len(string_transitions)
		i = 0
		buff = ""
		tagIn = False
		while(i < tam):
			if(string_transitions[i] == '('):
				tagIn = True
				buff = ""
			elif(string_transitions[i] == ')'):
				tagIn = False
				# se buff vazio, chegou ao fim
				if(buff == ""):
					break
				aux = self.custom_split(buff)
				self.transicao += [aux]
			elif(tagIn):
				buff +=string_transitions[i]
			#incremento
			i+=1

	def get_transitions(self):
		return self.transicao

	def get_saidas(self):
		return self.saidas

	def get_iniciais(self):
		return self.inicial

	def get_finais(self):
		return self.finais

	def get_estados(self):
		return self.estados

	def get_simbolos_entrada(self):
		return self.simbolos_entrada

	def get_simbolos_saida(self):
		return self.simbolos_saida

	def custom_split(self, val):
		i = 0
		tam = len(val)
		buff = ""
		saida = []
		while(i<tam):
			if(val[i] == ' ' and buff != ""):
				saida += [buff]
				buff = ""
			elif (val[i] != ' '):
				buff += val[i]

			i +=1

		if(buff != ""):
			saida += [buff]
		return saida

	def change_machine(self):
		pass