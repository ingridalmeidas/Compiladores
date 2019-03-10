from idtipo import idtipo
import semantico as semantico

global tokens, indice, contador, var, operador

def sintatico(listaTokens):
	
	global tokens, indice, contador, var, operador
	
	contador = 0 #Usado para controlar o escopo do semantico
	var = "" #Guarda o nome de uma variavel que vai ser posteriormente analisada no semantico
	operador = "" #Vai guardar o operador para depois verificar no semantico se ele está sendo utilizado com os tipos adequados
	
	semantico.pilhaVazia()

	tokens = listaTokens
	
	indice = 0
	
	programa()
	 
	
def programa():
	
	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == "program":
		
		#Abre escopo semântico
		semantico.entradaEscopo()
		semantico.printPilha()
		
		indice += 1
		
		if tokens[indice].classificacao == "identificador":
		
			#Adiciona identificador na pilha
			v = idtipo(tokens[indice].sIdentificador, "program")
			semantico.declaracao(v)
			semantico.printPilha()
			
			indice += 1
			
			if tokens[indice].sIdentificador == ";":
				indice += 1
				
				declaracoes_de_variaveis()
				declaracoes_de_subprogramas()
				comando_composto()
				
				if tokens[indice].sIdentificador != ".":
					print(tokens[indice].sIdentificador)
					print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador '.'")
					
			else:
				print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ';'")
			
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um identificador após a palavra 'program'")
		
	else:
		print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra 'program'")

		
def declaracoes_de_variaveis():

	global tokens, indice, contador, var, operador
	
	
	if tokens[indice].sIdentificador == "var":
		indice += 1
		
		lista_declaracao_variaveis()
		
		
def lista_declaracao_variaveis():

	global tokens, indice, contador, var, operador
	
	lista_de_identificadores()
	
	if tokens[indice].sIdentificador == ":":
		indice += 1
		
		tipo()
		
		if tokens[indice].sIdentificador == ";":
			indice += 1
			
			lista_declaracao_variaveis2()
		
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ';'")
		
		
	else:
		print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")
		
		
def lista_declaracao_variaveis2():

	global tokens, indice, contador, var, operador
	
	if (lista_de_identificadores()):
		
		if tokens[indice].sIdentificador == ":":
			indice += 1
		
			tipo()
		
			if tokens[indice].sIdentificador == ";":
				indice += 1
			
				lista_declaracao_variaveis2()
			else:
				print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ';'")
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")
			

def lista_de_identificadores():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].classificacao == "identificador":
	
		#Adiciona identificador na pilha
		v = idtipo(tokens[indice].sIdentificador, "0")
		semantico.declaracao(v)
		semantico.printPilha()
		
		indice += 1
		
		lista_de_identificadores2()
		
		return True
		
	else:
	
		return False

def lista_de_identificadores2():

	global tokens, indice, contador, var, operador

	if tokens[indice].sIdentificador == ",":
		indice += 1
		
		if tokens[indice].classificacao == "identificador":
		
			#Adiciona identificador na pilha
			v = idtipo(tokens[indice].sIdentificador, "0")
			semantico.declaracao(v)
			semantico.printPilha()
			
			indice += 1
			
			lista_de_identificadores2()
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um identificador após ','")
			
def tipo():

	global tokens, indice, contador, var, operador

	if tokens[indice].sIdentificador == "integer":
		indice += 1
		#Adiciona identificador
		semantico.atribuiTipo("inteiro")
		semantico.printPilha()
	
	elif tokens[indice].sIdentificador == "real":
		indice += 1
		#Adiciona identificador
		semantico.atribuiTipo("real")
		semantico.printPilha()
	
	elif tokens[indice].sIdentificador == "boolean":
		indice += 1
		#Adiciona identificador
		semantico.atribuiTipo("logico")
		semantico.printPilha()
		
	else:
		print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado as palavras reservadas 'integer', 'real' ou 'boolean'")
	

def declaracoes_de_subprogramas():

	global tokens, indice, contador, var, operador
	
	if (declaracao_de_subprograma()):
	
		if tokens[indice].sIdentificador == ";":
			indice += 1
		
			declaracoes_de_subprogramas()
		
def declaracao_de_subprograma():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == "procedure":
		indice += 1
		
		if tokens[indice].classificacao == "identificador":
			
			#Adiciona identificador na pilha
			v = idtipo(tokens[indice].sIdentificador, "procedure")
			semantico.declaracao(v)
			semantico.printPilha()
			
			#Abre um novo escopo
			semantico.entradaEscopo()
			
			indice += 1
			
			argumentos()
			
			if tokens[indice].sIdentificador == ';':
				indice += 1
				
				declaracoes_de_variaveis()
				declaracoes_de_subprogramas()
				comando_composto()
			else:
				print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ';'")
		
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um identificador após 'procedure'")
		
		return True
		
	else:
		return False
	
def argumentos():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == '(':
		indice += 1
		
		lista_de_parametros()
		
		if tokens[indice].sIdentificador == ')':
			indice += 1
		
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")
			

def lista_de_parametros():

	global tokens, indice, contador, var, operador
	
	lista_de_identificadores()
	
	if tokens[indice].sIdentificador == ':':
		indice += 1
		
		tipo()
		
		lista_de_parametros2()
	
	else:
		print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")
		
def lista_de_parametros2():
	
	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == ";":
		indice += 1
		
		lista_de_identificadores()
		
		if tokens[indice].sIdentificador == ":":
			indice += 1
			
			tipo()
			
			lista_de_parametros2()
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")
			

def comando_composto():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == "begin":
		
		#Incrementa o escopo
		contador += 1
		
		indice += 1
		
		comandos_opcionais()
		
		if tokens[indice].sIdentificador == "end":
		
			#Decrementa o escopo
			contador -= 1
			
			#Se o contador for 0 é pra limpar um escopo
			if contador == 0:
				semantico.saidaEscopo()
				semantico.printPilha()
			
			indice += 1
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'end'")
			
		return True
		
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'begin'")
		
		return False

def comandos_opcionais():

	global tokens, indice, contador, var, operador
	
	lista_de_comandos()
	
def lista_de_comandos():

	global tokens, indice, contador, var
	
	if (comando()):
		lista_de_comandos2()
	
def lista_de_comandos2():
	
	global tokens, indice, contador, var
	
	if tokens[indice].sIdentificador == ";":
		indice += 1
		
		comando()
		
		lista_de_comandos2()
		
def comando():

	global tokens, indice, contador, var, operador
	
	aux = False
	
	if (variavel()):
	
		if tokens[indice].sIdentificador == ":=":
			indice += 1
		
			expressao()
			
			#Passando a variavel para analisar se os tipos da atribuição são compatíveis
			semantico.atribuicao(var)
			
			semantico.limpaPilhaTipo()
			
			return True
		
		else:
			aux = True
			indice -= 1
			
	if aux:
		if (ativacao_de_procedimento()):
		
			return True
	
	elif (comando_composto()):
	
		return True
		
	elif tokens[indice].sIdentificador == "if":
		indice += 1
		
		expressao()
		
		semantico.limpaPilhaTipo()
		
		if tokens[indice].sIdentificador == "then":
			indice += 1
			
			comando()
			
			parte_else()
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'then'")
		
		return True
	
	elif tokens[indice].sIdentificador == "while":
		indice += 1
		
		expressao()
		
		semantico.limpaPilhaTipo()
		
		if tokens[indice].sIdentificador == "do":
			indice += 1
			
			comando()
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'do'")
			
		return True
	
	elif tokens[indice].sIdentificador == "case":
		indice += 1
		
		seletor()
		
		if tokens[indice].sIdentificador == "of":
			indice += 1
			
			lista_de_seletor()
			
			if tokens[indice].sIdentificador == "else":
				indice += 1
				
				if tokens[indice].sIdentificador == ":":
					indice += 1
					
					comando()
					
				else:
					print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")
			else:
				print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'else'")
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado a palavra reservada 'of'")
		
		return True
	
	else:
		return False
		
def seletor():

	global tokens, indice, contador, operador
	
	if tokens[indice].classificacao == "numero inteiro":
		indice += 1
	elif tokens[indice].classificacao == "numero real":
		indice += 1
	else:
		print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um numero inteiro ou um numero real")

def lista_de_seletor():

	global tokens, indice, contador
	
	seletor()
	
	if tokens[indice].sIdentificador == ":":
		indice += 1
		
		comando()
		
		lista_de_seletor2()
	else:
		print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")

def lista_de_seletor2():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador  == ";":
		indice += 1
		
		seletor()
		
		if tokens[indice].sIdentificador == ":":
			indice += 1
			
			comando()
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ':'")
		

def parte_else():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == "else":
		indice += 1
		
		comando()
		
def variavel():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].classificacao == "identificador":
		
		if contador > 0:
			print(tokens[indice].sIdentificador + " sendo usado")
			semantico.uso(tokens[indice].sIdentificador)
			var = tokens[indice].sIdentificador
		
		indice += 1
		
		return True
	else:
		return False

def ativacao_de_procedimento():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].classificacao == "identificador":
	
		if contador > 0:
			print(tokens[indice].sIdentificador + " procedimento sendo usado")
			semantico.uso(tokens[indice].sIdentificador)
		
		indice += 1
		
		ativacao_de_procedimento2()
		
		return True
	else:
		return False

def ativacao_de_procedimento2():

	global tokens, indice, contador, var, operador

	if tokens[indice].sIdentificador == '(':
		indice += 1
		
		lista_de_expressoes()
		
		if tokens[indice].sIdentificador == ')':
			indice += 1
			
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")
			
def lista_de_expressoes():

	global tokens, indice, contador, var, operador
	
	expressao()
	
	lista_de_expressoes2()
	
def lista_de_expressoes2():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == ',':
		indice += 1
		
		expressao()
		
		lista_de_expressoes2()


def expressao():

	global tokens, indice, contador, var, operador
	
	expressao_simples()
	expressao2()
	
def expressao2():

	global tokens, indice, contador, var, operador
	
	if (op_relacional()):
		expressao_simples()
		semantico.tipoOperador(operador)
		
def expressao_simples():

	global tokens, indice, contador, var, operador
	
	if (termo()):
		expressao_simples2()
	
	elif (sinal()):
		termo()
		semantico.tipoOperador(operador)
		expressao_simples2()
		
	else:
		print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um termo ou um sinal")

def expressao_simples2():

	global tokens, indice, contador, var, operador
	
	if (op_aditivo()):
		termo()
		expressao_simples2()
		semantico.tipoOperador(operador)
		
def termo():

	global tokens, indice, contador, var, operador

	if(fator()):
		termo2()
		return True
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um fator ou um termo")
		return False

def termo2():

	global tokens, indice, contador, var, operador
	
	if (op_multiplicativo()):
		fator()
		termo2()
		semantico.tipoOperador(operador)
	
		
def fator():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].classificacao == "identificador":
	
		if contador > 0:
			print(tokens[indice].sIdentificador + " sendo usado")
			
			
			semantico.uso(tokens[indice].sIdentificador)
			#Adiciona o tipo na pilha de tipos para a operação
			semantico.pushTipo(tokens[indice].sIdentificador, "variavel")
			
		indice += 1
		fator2()
		return True
	
	elif tokens[indice].classificacao == "numero inteiro":
		
		#Adiciona o tipo na pilha de tipos para a operação
		semantico.pushTipo(tokens[indice].sIdentificador, "inteiro")
		indice += 1
		return True
	
	elif tokens[indice].classificacao == "numero real":
		#Adiciona o tipo na pilha de tipos para a operação
		semantico.pushTipo(tokens[indice].sIdentificador, "real")
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "true":
		#Adiciona o tipo na pilha de tipos para a operação
		semantico.pushTipo(tokens[indice].sIdentificador, "logico")
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "false":
		semantico.pushTipo(tokens[indice].sIdentificador, "logico")
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "(":
		indice += 1
		
		expressao()
		
		if tokens[indice].sIdentificador == ")":
			indice += 1
			
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")
			
		return True
	
	elif tokens[indice].sIdentificador == "not":
		indice += 1
		
		fator()
		
		return True
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um fator")
		return False
		
def fator2():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == "(":
		indice += 1
		
		lista_de_expressoes()
		
		if tokens[indice].sIdentificador == ")":
			indice += 1
		else:
			print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado o delimitador ')'")
			
def sinal():

	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == "+":
		print("+")
		operador = "+"
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "-":
		print("-")
		operador = "-"
		indice += 1
		return True
		
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um sinal")
		return False
		

def op_relacional():

	global tokens, indice, contador, var, operador
	
	
	
	if tokens[indice].sIdentificador == "=":
		print("=")
		operador = "="
		indice += 1
		return True
		
	elif tokens[indice].sIdentificador == "<":
		print("<")
		operador = "<"
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == ">":
		print(">")
		operador = ">"
		indice += 1
		return True
		
	elif tokens[indice].sIdentificador == "<=":
		print("<=")
		operador = "<="
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == ">=":
		print(">=")
		operador = ">="
		indice += 1
		return True
		
	elif tokens[indice].sIdentificador == "<>":
		print("<>")
		operador = "<>"
		indice += 1
		return True
	
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um operador relacional")
		return False
		
def op_aditivo():
	
	global tokens, indice, contador, var, operador

	if tokens[indice].sIdentificador == "+":
		print("+")
		operador = "+"
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "-":
		print("-")
		operador = "-"
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "or":
		print("or")
		operador = "or"
		indice += 1
		return True
	
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um operador aditivo")
		return False
	
def op_multiplicativo():
	
	global tokens, indice, contador, var, operador
	
	if tokens[indice].sIdentificador == "*":
		print("*")
		operador = "*"
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "/":
		print("/")
		operador = "/"
		indice += 1
		return True
	
	elif tokens[indice].sIdentificador == "and":
		print("and")
		operador = "and"
		indice += 1
		return True
		
	else:
		#print(tokens[indice].nLinha + ": ERRO! Sintax inválida. Era esperado um operador multiplicativo")
		return False