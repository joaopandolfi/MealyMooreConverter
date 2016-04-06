#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Escrito em Python V 3
#
# (C) João Carlos Pandolfi Santana
#
# Classe que faz o parsing do aquivo 
# Devolve pequenas estruturas
#
#####################################

class Parser():

	#metodo construtor
	def __init__(self):
		pass

	# ==== DECODIFICADORES ===

	def decode_type_machine(self,arq):
		if("mealy" in arq):
			return "mealy"

		return "moore"

	def decode_simbolos_entrada(self,arq):
		return self.decode_generic(arq,"symbols-in")

	def decode_simbolos_saida(self,arq):
		return self.decode_generic(arq,"symbols-out")

	def decode_iniciais(self,arq):
		return self.decode_generic(arq,"start")

	def decode_estados(self,arq):
		return self.decode_generic(arq,"states")

	def decode_finais(self,arq):
		return self.decode_generic(arq,"finals")

	def decode_transicoes(self,arq):
		return self.decode_generic2(arq,"trans")
	
	def decode_saidas(self,arq):
		return self.decode_generic2(arq,"out-fn")

	def decode_generic2(self,arq,tag):
		position = arq.find(tag) + len(tag) #tamanho da string
		buff = ""
		lock = 1
		tam = len(arq)
		while( lock > 0):
			if(arq[position] == '('):
				lock +=1
			elif(arq[position] == ')'):
				lock -=1

			buff+= arq[position]
			position+=1

		return buff

	def decode_generic(self,arq,tag):
		position = arq.find(tag) + len(tag)+1 #tamanho da string
		buff = ""
		tam = len(arq)
		while( arq[position] != ')'):
			buff+= arq[position]
			position +=1

		saida = buff.split(' ') 
		return saida[:1]

	# ===== CODIFICADORES ====

	def codify_notation_mealy(self,mealyMachine):
		notation = "(mealy \n "
		notation += self.codify_notation(mealyMachine)
		notation += ")"
		return notation

	def codify_notation_moore(self,mooreMachine):
		notation = "(moore \n "
		notation += self.codify_notation(mooreMachine)
		
		notation +="\n (out-fn\n"

		aux = mooreMachine.get_saidas()
		for saida in aux:
			notation += " ("
			for element in saida:
				notation += " "+element
			notation +=")"

		notation +="))"
		return notation

	def codify_notation(self,mealyMachine):
		notation = "(symbols-in"
		aux = mealyMachine.get_simbolos_entrada()
		for simbolo in aux:
			notation += " "+simbolo
		
		notation +=")\n (symbols-out"
		
		aux = mealyMachine.get_simbolos_saida()
		for simbolo in aux:
			notation += " "+simbolo

		notation +=")\n (states"

		aux = mealyMachine.get_estados()
		for estado in aux:
			notation += " "+estado

		notation +=")\n (start"

		aux = mealyMachine.get_iniciais()
		for inicial in aux:
			notation += " "+str(inicial)

		notation += ")\n (finals"

		aux = mealyMachine.get_finais()
		for finais in aux:
			notation += " "+finais

		notation += ")\n (trans\n"
		aux = mealyMachine.get_transitions()
		for transition in aux:
			notation += " ("
			for element in transition:
				notation += " "+element
			notation +=")"

		notation +=")"

		return notation