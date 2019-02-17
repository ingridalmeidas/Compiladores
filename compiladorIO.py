def	lePrograma():
	"""
	Função	para leitura do	programa
	Retorna lista com o conteúdo do programa, cada	elemento da	lista
	é uma linha do	arquivo
	"""
	
	arquivo =	open('teste', 'r')
	#arquivo = open('teste', 'r')
	conteudoArquivo = arquivo.readlines()
	arquivo.close()
	
	return	conteudoArquivo

def	lePalavrasReservadas():
	"""
	Função	para carregamento de palavras reservadas
	Retorna lista com de palavras reservadas, cada	elemento da	lista
	é uma palavra reservada
	"""
	
	arquivo = open('palavrasReservadas', 'r')
	conteudoArquivo = arquivo.readlines()
	arquivo.close()

	palavrasReservadas = []

	for linha in	conteudoArquivo:
		palavrasReservadas.append(linha[:-1])

	return palavrasReservadas

def	salvaTokens(lista):
	arquivo = open('Tokens', 'w')
	arquivo.writelines(lista)
	arquivo.close()