import lexico as lexico
import sintatico as sintatico
from token import token

def main():

	listaTokens = lexico.lexico()
		
	sintatico.sintatico(listaTokens)
		
if __name__	== '__main__':
	main()