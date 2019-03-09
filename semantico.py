global pilhaTBS

def pilhaVazia():
	
	global pilhaTBS
	
	pilhaTBS = []
	
def printPilha():

	global pilhaTBS
	
	print(pilhaTBS)

def entradaEscopo():

	global pilhaTBS
	
	pilhaTBS.append("$")
	
def saidaEscopo():
	
	global pilhaTBS
	
	for i in pilhaTBS[::-1]:
		
		if i == "$":
			pilhaTBS.pop()
			break
		
		pilhaTBS.pop()

	
def declaracao(simbolo):
	
	global pilhaTBS
	
	for i in pilhaTBS[::-1]:
	
		if i == simbolo:
		
			print("SEMANTICO ERROR: Variável já declarada com esse nome nesse escopo")
			
		else:
			if i == "$":
			
				#Se chegou na marca e não apresentou o símbolo, pode adicionar porque não existe o identificador com esse nome no escopo
				pilhaTBS.append(simbolo)
			
				break
	
def uso(simbolo):

	global pilhaTBS
	
	encontrou = False
	
	for i in pilhaTBS[::-1]:
		
		if i == simbolo:
			encontrou = True
			break
	
	if not encontrou:
		print("SEMANTICO ERROR: Variável não declarada")


	