import compiladorIO	as cio
from token import token
from automato import automato
from estado	import estado
import string

global q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21, q22, q23, q24, q25


def	main():

	"""
	Função	principal do analisador	léxico
	Controla as chamadas das funções utilizadas pelo analisador
	"""

	programa =	cio.lePrograma()
	
	#print(programa)

	#print('\n')

	palavrasReservadas	= cio.lePalavrasReservadas()
	
	#print(palavrasReservadas)
	
	criaEstados()
	
	automato =	criaAutomato()
	
	execucao(programa, palavrasReservadas, automato)
	
	#automato(programa, mapaReservadas, palavrasReservadas)

	#classificaoTokens	= automato(programa)
	#cio.salvaTokens(classificaoTokens
	
def	criaAutomato():

	estado	= ['q0', 'q1', 'q2', 'q3', 'q4', 'q5','q6',	'q7', 'q8',	'q9', 'q10', 'q11',	'q12', 'q13', 'q14', 'q15',	'q16', 'q17', 'q18', 'q19',	'q20', 'q21', 'q22', 'q23', 'q24', 'q25']
	
	estadoInicial = 'q0'
	
	estadosFinais = ['q3',	'q13', 'q2', 'q17',	'q19', 'q15', 'q16', 'q18',	'q14', 'q11', 'q12', 'q10',	'q9', 'q21', 'q8','q20', 'q7', 'q6', 'q5', 'q4', 'q25']
	
	a =	automato(estado, estadoInicial,	estadosFinais)
	
	
	return	a
	
	
	
def	criaEstados():

	global	q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21, q22, q23, q24, q25

	minusculas	= list(string.ascii_lowercase)
	maiusculas	= list(string.ascii_uppercase)
	numeros = ['0', '1','2','3','4','5','6','7','8','9']
	
	nome =	''
	transicoes	= {}
	classificacao = ''
	
	#estado inicial
	nome =	'q0'
	
	transicoes['q0'] =	['\n','\t','\r', ' ']
	transicoes['q1'] =	['{']
	transicoes['q2'] =	minusculas + maiusculas
	transicoes['q3'] =	numeros
	transicoes['q4'] =	[',']
	transicoes['q5'] =	['.']
	transicoes['q6'] =	[';']
	transicoes['q7'] =	['+']
	transicoes['q20'] = ['-']
	transicoes['q8'] =	['*']
	transicoes['q21'] = ['/']
	transicoes['q9'] =	['(']
	transicoes['q10'] = [')']
	transicoes['q11'] = [':']
	transicoes['q17'] = ['>']
	transicoes['q15'] = ['<']
	transicoes['q14'] = ['=']
	
	classificacao = ''
	
	q0	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q1
	nome =	'q1'

	transicoes['q1'] =	minusculas + maiusculas	+ ['_',	'\n','\t','\r',	' ', '.', '>', '<', '=', ':', '(', ')', '/', '*', '-', '+', ';', ','] + numeros
	transicoes['q0'] =	['}']
	classificacao = ''

	q1	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q2
	nome =	'q2'

	transicoes['q2'] =	minusculas + maiusculas	+ ['_']	+ numeros
	transicoes['q23'] = ['[']
	classificacao = 'identificador'

	q2	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q3
	nome =	'q3'

	transicoes['q3'] =	numeros
	transicoes['q13'] = ['.']
	classificacao = 'numero inteiro'

	q3	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q13
	nome =	'q13'

	transicoes['q13'] = numeros
	classificacao = 'numero real'

	q13 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q4

	nome =	'q4'

	transicoes	= {}
	classificacao = 'delimitador'

	q4	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q5
	nome =	'q5'

	transicoes	= {}
	classificacao = 'delimitador'

	q5	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q6
	nome =	'q6'

	transicoes	= {}
	classificacao = 'delimitador'

	q6	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q7
	nome =	'q7'

	transicoes	= {}
	classificacao = 'operador aditivo'

	q7	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q20
	nome =	'q20'

	transicoes	= {}
	classificacao = 'operador aditivo'

	q20 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q8
	nome =	'q8'

	transicoes	= {}
	classificacao = 'operador multiplicativo'

	q8	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q21
	nome =	'q21'

	transicoes['q22'] = ['/']
	classificacao = 'operador multiplicativo'

	q21 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q9
	nome =	'q9'

	transicoes	= {}
	classificacao = 'delimitador'

	q9	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q10
	nome =	'q10'

	transicoes	= {}
	classificacao = 'delimitador'

	q10 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q11
	nome =	'q11'

	transicoes['q12'] = ['=']
	classificacao = 'delimitador'

	q11 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q12
	nome =	'q12'

	transicoes	= {}
	classificacao = 'atribuicao'

	q12 = estado(nome,	transicoes,	classificacao)
	
	nome =	''
	transicoes	= {}
	classificacao = ''

	#q17
	nome =	'q17'

	transicoes['q19'] = ['=']
	classificacao = 'operador relacional'

	q17 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q15
	nome =	'q15'

	transicoes['q16'] = ['>']
	transicoes['q18'] = ['=']
	classificacao = 'operador relacional'

	q15 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q14
	nome =	'q14'

	transicoes	= {}
	classificacao = 'operador relacional'

	q14 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q19
	nome =	'q19'

	transicoes	= {}
	classificacao = 'operador relacional'

	q19 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q16
	nome =	'q16'

	transicoes	= {}
	classificacao = 'operador relacional'

	q16 = estado(nome,	transicoes,	classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''

	#q18
	nome =	'q18'

	transicoes	= {}
	classificacao = 'operador relacional'

	q18 = estado(nome,	transicoes,	classificacao)
	
	nome =	''
	transicoes	= {}
	classificacao = ''
	
	#q22
	
	nome = 'q22'
	
	transicoes = {}
	classificao = ''
	
	q22 = estado(nome, transicoes, classificao)
	
	nome =	''
	transicoes	= {}
	classificacao = ''
	
	#q23
	nome =	'q23'

	transicoes['q24'] =	numeros
	classificacao = ''

	q23	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''
	
	#q24
	nome = 'q24'
	
	transicoes['q24'] = numeros
	transicoes['q25'] = [']']
	classificacao = ''
	
	q24	= estado(nome, transicoes, classificacao)

	nome =	''
	transicoes	= {}
	classificacao = ''
	
	#q25
	nome = 'q25'
	
	transicoes = {}
	classificacao = 'array'
	
	q25	= estado(nome, transicoes, classificacao)
	
def	execucao(programa, palavrasReservadas, automato):

	global	q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21, q22, q23, q24, q25

	estadoAtual = q0
	estadoAnterior	= None
	indiceCaractere = 0 #Indice do caractere avaliado
	
	temTransicao =	False #Variavél que indica se tem transição de um automato pra outro a partir do caractere avaliado
	transicao = '' #Indica o estado para qual a transição aponta
	
	nLinha = 1 #Contador de linha
	tokens = [] #Lista que guarda os tokens classificados
	
	encerra = False #Indica se foi detectado algum símbolo não pertencente a linguagem para encerrar o loop
	comentario = False #Indica se o programa acabou e se algum comentario ficou aberto
	
	dictEstados = {
		'q0' : q0, 'q1' :	q1,	'q2' : q2, 'q3'	: q3, 'q4' : q4, 'q5' :	q5,	'q6' : q6, 'q7'	: q7, 'q8' : q8, 'q9' :	q9,	'q10' :	q10, 'q11' : q11, 'q12'	: q12,
		'q13': q13, 'q14' : q14, 'q15' : q15, 'q16' : q16, 'q17': q17, 'q18' : q18,	'q19' :	q19, 'q20' : q20, 'q21'	: q21, 'q22' : q22, 'q23' : q23,
		'q24' : q24, 'q25' : q25}
	
	#Para cada linha no programa
	for linha in programa:
	
		#print("\nlinha: " , linha)
		
		#Percorre todos os caracteres da linha
		while (indiceCaractere < len(linha)):
			
			#print("\nCaractere: " + linha[indiceCaractere] + '\n')
		
			#Se estivermos no estado inicial, quer dizer que começamos a avaliar um novo token
			if estadoAtual.nome == automato.estadoInicial:
				inicio = indiceCaractere
				#print("aqui2", inicio)
		
			#Percorrer as transições	do estado atual
			for t in estadoAtual.transicoes.keys():
				
				#Se o caractere for um '{', deve-se indicar que tem um comentário aberto
				if linha[indiceCaractere] == '{':
					comentario = True
					
				#Se o caractere for um '}', deve-se indicar o fechamento de um comentário	
				if linha[indiceCaractere] == '}':
					comentario = False
					
				#Verifica se o caractere possui alguma transição no estado atual	
				if linha[indiceCaractere] in estadoAtual.transicoes[t]:
					temTransicao =	True
					transicao = t #t armazena a chave do dicionário que indica para qual estado a transição direciona
			
			#print(estadoAtual.nome)
			
			#Se tiver uma transição
			if temTransicao:
			
				#Se a transicao for pra o estado 22 devemos ignorar a linha
				if transicao == 'q22':
					estadoAtual	= dictEstados[automato.estadoInicial]
					temTransicao = False
					break
				else:
				
					#Se o estado atual é um estado final, precisamos guardar ele como um estado anterior que é pra poder voltar para o último estado final
					if estadoAtual.nome	in automato.estadosFinais:
						estadoAnterior = estadoAtual
					
					#print(transicao)
					#Atualiza o estado	que	essa transicao indica
					estadoAtual = dictEstados[transicao]
				
					#Vamos analisar o proximo caractere
					indiceCaractere +=	1
				
			else: #Se não tiver transição
				
				#Se não tiver transição e estivermos no estado inicial, quer dizer que o símbolo não é reconhecido pela linguagem
				if estadoAtual.nome == automato.estadoInicial:
					#print("ERRRROR")
					
					#Indica o erro
					sIdentificador = linha[indiceCaractere]
					classificacao = "ERROR - Símbolo inválido"
					tkn = token(sIdentificador, classificacao, str(nLinha))
					tokens.append(tkn)
					encerra = True
					break
				
				#Se não tiver transição e o estado atual é um estado final
				if estadoAtual.nome	in automato.estadosFinais:
					
					#Pega o token que vai ser classificado
					sIdentificador	= linha[inicio:indiceCaractere]
					
					#O estado q2 pode classificar como palavra reservada, como identificador, como operador aditivo e como operador multiplicativo,
					#então temos que verificar
					if	estadoAtual.nome ==	'q2':
						if sIdentificador in palavrasReservadas:
							classificacao = 'palavra reservada'
							tkn = token(sIdentificador, classificacao, str(nLinha))
						elif sIdentificador == 'and':
							classificacao = 'operador multiplicativo'
							tkn = token(sIdentificador, classificacao, str(nLinha))
						elif sIdentificador == 'or':
							classificacao = 'operador aditivo'
							tkn = token(sIdentificador, classificacao, str(nLinha))	
						else:
							tkn = token(sIdentificador, estadoAtual.classificacao, str(nLinha))
					
					#Se não tivermos no estado q2, vamos classificar com a classificação do estado atual
					else:
						tkn = token(sIdentificador, estadoAtual.classificacao, str(nLinha))
					
					#Adiciona a nova classificação na lista de tokens classificados
					tokens.append(tkn)
					
				#Se não tiver transição e o estado atual não é um estado final	
				else:
				
					#pega o token que vai ser classificado
					sIdentificador = linha[inicio:indiceCaractere]
					
					#E classifica a partir do estado anterior que é o último estado final
					if	estadoAnterior.nome	== 'q2':
						if sIdentificador	in palavrasReservadas:
							classificacao = 'palavra	reservada'
							tkn = token(sIdentificador, classificacao, str(nLinha))
						elif sIdentificador == 'and':
							classificacao = 'operador multiplicativo'
							tkn = token(sIdentificador, classificacao, str(nLinha))
						elif sIdentificador == 'or':
							classificacao = 'operador aditivo'
							tkn = token(sIdentificador, classificacao, str(nLinha))
							
						else:
							tkn = token(sIdentificador, estadoAnterior.classificacao,	str(nLinha))
					#Se não é o estado q2	
					else:
						tkn = token(sIdentificador, estadoAtual.classificacao, str(nLinha))
					
					#Adiciona a nova classificação na lista de tokens classificados
					tokens.append(tkn)
				
				#Se não tiver transição, quer dizer que classificamos um token, então devemos voltar para o estado inicial
				estadoAtual	= dictEstados[automato.estadoInicial]
			
			#A variavel que indica se tem transição retorna para false para verificarmos o próximo caractere
			temTransicao = False
		
		#Final do while que indica o final da linha

		#Incrementa a linha
		nLinha += 1
		#O indice do caractere avaliado vai para o começo da nova linha
		indiceCaractere = 0
		#Variavel que indica o inicio do token também vai pra 0
		inicio = 0
		
		#Se encerra for true quer dizer que houve erro de símbolo não pertencente a linguagem, então temos que encerrar
		if encerra:
			break
	
	#Se comentario for true, quer dizer que o programa terminou com um comentario aberto e devemos indicar o erro
	if comentario:
		#print("ERRRROR")
		sIdentificador = ''
		classificacao = "ERROR - Símbolo '}' não encontrado"
		tkn = token(sIdentificador, classificacao, '')
		tokens.append(tkn)
					
	
	#Lista que salva os tokens classificados
	tokensSalvar = []
	
	#Pega todas as informaçõs do token para salvar
	for t in tokens:
		print(t.getTokenInfo())
		tokensSalvar.append(t.getTokenInfo() + '\n')
	
	cio.salvaTokens(tokensSalvar)
		
	
		
if __name__	== '__main__':
	main()
