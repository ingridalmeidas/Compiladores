from idtipo import idtipo
from sys import exit

global pilhaTBS
global pilhaTipo

#Inicia as pilhas de tipos e de identificadores
def pilhaVazia():
	
	global pilhaTBS, pilhaTipo
	
	pilhaTBS = []
	pilhaTipo = []
	

#Printa a pilha	
def printPilha():

	global pilhaTBS
	
	
	print("\n\n Pilha identificador ")
	
	for i in pilhaTBS:
		print(i.identificador, i.tipo)
	
	print("\n\n")

	
#Abre um novo escopo de identificadores	
def entradaEscopo():

	global pilhaTBS
	
	v = idtipo("$", None)
	
	pilhaTBS.append(v)
	
#Fecha um escopo de identificadores	
def saidaEscopo():
	
	global pilhaTBS
	
	for i in pilhaTBS[::-1]:
		
		if i.identificador == "$":
			pilhaTBS.pop()
			break
		
		pilhaTBS.pop()

	
#Verifica se a declaração de variáveis segue a regra da linguagem
def declaracao(variavel):
	
	global pilhaTBS
	
	for i in pilhaTBS[::-1]:
	
		if i.identificador == variavel.identificador:
		
			exit("SEMANTICO ERROR: Variável já declarada com esse nome nesse escopo")
			
		else:
			if i.identificador == "$":
			
				#Se chegou na marca e não apresentou o símbolo, pode adicionar porque não existe o identificador com esse nome no escopo
				pilhaTBS.append(variavel)
			
				break
	
#Verifica se o uso de uma variavel segue as regras da linguagem	
def uso(simbolo):

	global pilhaTBS
	
	encontrou = False
	
	for i in pilhaTBS[::-1]:
		
		if i.identificador == simbolo:
			encontrou = True
			break
	
	if not encontrou:
		exit("SEMANTICO ERROR: Variável não declarada")

#Retorna o tipo de um identificador da tabela de identificadores
def tipoIdentificador(variavel):

	global pilhaTBS
	
	for i in pilhaTBS:
			if i.identificador == variavel:
				tipo = i.tipo
	
	return tipo
	

#Atribui o tipo aos identificadores do programa
def atribuiTipo(tipo):
	
	global pilhaTBS
	
	for i in pilhaTBS:
		
		if i.tipo == "0":
			i.tipo = tipo
			
#Adiciona o tipo utilizado na pilha de tipos para as operações			
def pushTipo(ident, tipo):
	
	global pilhaTipo, pilhaTBS

	
	if tipo == "variavel":
	
		aux = tipoIdentificador(ident)
		
		pilhaTipo.append(aux)
				
	else:
		pilhaTipo.append(tipo)
	
	print("Pilha tipo: ")
	print(pilhaTipo)
	
	if len(pilhaTipo) == 2:
		atualizaPilha()
		
	

#Faz a operação de tipos
def atualizaPilha():
	
	global pilhaTipo
	
	if pilhaTipo[0] == "inteiro" and pilhaTipo[1] == "inteiro":
		pilhaTipo.pop()
		pilhaTipo.pop()
		pilhaTipo.append("inteiro")
	
	elif pilhaTipo[0] == "real" and pilhaTipo[1] == "real":
		pilhaTipo.pop()
		pilhaTipo.pop()
		pilhaTipo.append("real")
	
	elif pilhaTipo[0] == "inteiro" and pilhaTipo[1] == "real":
		pilhaTipo.pop()
		pilhaTipo.pop()
		pilhaTipo.append("real")
	
	elif pilhaTipo[0] == "real" and pilhaTipo[1] == "inteiro":
		pilhaTipo.pop()
		pilhaTipo.pop()
		pilhaTipo.append("real")
	
	elif pilhaTipo[0] == "logico" and pilhaTipo[1] == "logico":
		
		pilhaTipo.pop()
		pilhaTipo.pop()
		pilhaTipo.append("logico")
	
	else:
		
		exit("SEMANTICO ERROR: Incopatibilidade de tipos")
		
		
	print("Pilha de tipos atualizadas: ")
	print(pilhaTipo)

#Verifica se a atribuição segue as regras da linguagem
def atribuicao(var):
	
	global pilhaTipo
	
	#Para a atribuição ser compatível o tipo da variável utilizada deve ser igual ao topo da pilha
	if tipoIdentificador(var) == pilhaTipo[0]:
		print("Atribuição compatível")
			
	else:
		exit("SEMANTICO ERROR: Incompatibilidade de tipos na atribuição")

#Verifica se os tipos utilizados em um operador são os aceitos
def tipoOperador(op):

	global pilhaTipo
	
	if op == "+" or op == "-" or op == "*" or op == "/":
		if pilhaTipo[0] == "inteiro" or pilhaTipo[0] == "real":
			print("Operação está sendo realizada com os tipos aceitos")
		else:
			exit("SEMANTICO ERROR: O operador não suporta os tipos utilizados")
			
	elif op == "=" or op == ">" or op == "<" or op == ">=" or op == "<=" or op == "<>":
		if pilhaTipo[0] == "inteiro" or pilhaTipo[0] == "real":
			print("Operação está sendo realizada com os tipos aceitos")
		else:
			exit("SEMANTICO ERROR: O operador não suporta os tipos utilizados")
			
	elif op == "and" or op == "or":
		if pilhaTipo[0] == "logico":
			print("Operação está sendo realizada com os tipos aceitos")
		else:
			exit("SEMANTICO ERROR: O operador não suporta os tipos utilizados")

#Limpa a pilha dos tipos quando é terminada uma avaliação
def limpaPilhaTipo():
	
	global pilhaTipo
	
	pilhaTipo = []
		


	