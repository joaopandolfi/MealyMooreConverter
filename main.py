#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Escrito em Python V 3
#
# (C) João Carlos Pandolfi Santana
#
# Arquivo responsável por Converter maquinas
#
# Modo de uso python3 <programa>.py -i <arqEntrada> -o <arqSaida>
#
#################################################################

#importo libs do programa
from libs import mealy
from libs import moore
from libs import parser

#importo lib do sistema
import sys

# Classe main
class Main():
	#escreve string no arquivo	, a+ (concatena), w (substitui)
	def write_arq(self,arquivo,string,modo):
		arq = open("./"+arquivo,modo)
		arq.write(string)
		arq.close()

	#le arquivo completo
	def read_arq(self,arquivo):
		conteudo =""
		result = ""
		arq = open('./'+arquivo , 'rt',encoding='utf-8')
		conteudo = arq.readline()
		while conteudo != '':
			if(conteudo[-1] =='\n'):
				conteudo = conteudo[:-1] 
			result +=conteudo
			conteudo = arq.readline()
		arq.close()
		return result


	def processa_argumento(self,arg):
		saida = ["",""] #[<arqEntrada>,<arqSaida>]
		if(not("-i" in arg) and not("-o" in arg)):
			print("Argumentos invalidos")
			exit()

		tam = len(arg)
		i = 0
		while(i<tam):
			if(arg[i] == "-i"):
				saida[0] = arg[i+1]
			elif(arg[i] == "-o"):
				saida[1] = arg[i+1]
			i+= 1
		return saida

	def main(self):
		#variaveis
		arquivos = [] #[<entrada>,<saida>]
		arquivo_lido = "" #arquivo de entrada lido
		typeMachine = "" #"mealy"| "moore"
		machine = None
		coder = parser.Parser()
		arquivos = self.processa_argumento(sys.argv[1:])
		
		arquivo_lido = self.read_arq(arquivos[0])

		typeMachine = coder.decode_type_machine(arquivo_lido)
		if(typeMachine == "mealy"):
			machine = mealy.Mealy()
		else:
			machine = moore.Moore()
			machine.set_saidas(coder.decode_saidas(arquivo_lido))

		#decodifico o arquivo
		machine.set_estados(coder.decode_estados(arquivo_lido),coder.decode_iniciais(arquivo_lido),coder.decode_finais(arquivo_lido))
		machine.set_transitions(coder.decode_transicoes(arquivo_lido))
		machine.set_simbolos(coder.decode_simbolos_entrada(arquivo_lido),coder.decode_simbolos_saida(arquivo_lido))

		#converto a maquina
		machine.change_machine()

		if(typeMachine == "mealy"):
			self.write_arq(arquivos[1],coder.codify_notation_moore(machine),"w")
		else:
			self.write_arq(arquivos[1],coder.codify_notation_mealy(machine),"w")

# ========= MAIN ============
main = Main()
main.main()