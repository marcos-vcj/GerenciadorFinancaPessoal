class Fundo(object):
	
	def __init__(self, ano, mes, fundo, valor):
		self.ano=ano
		self.mes=mes
		self.fundo=fundo
		self.valor=valor

"""	def debita(self):
		arqF=open("fundo.txt","r+")
		a=arqF
		if not a:
			arqF.write(self.ano + ' ' + self.mes + ' ' + self.fundo + ' ' + self.valor + "\n")
		else:
			for linha in arqF:
				info=linha.split()
				if info[0]==self.ano and info[1]==self.mes and info[2]==self.fundo:
					novoValor=(float(info[3]))+(float(self.valor))
					arqF.write(self.ano + ' ' + self.mes + ' ' + self.fundo + ' ' + str(novoValor) + "\n")
				else:
					arqF.write(self.ano + ' ' + self.mes + ' ' + self.fundo + ' ' + self.valor + "\n")
		arqF.close()
					

	#def credita():

"""
	def renda(self):
		arq=open("dado.txt","r")
		for linha in arq:
			valores=linha.split()
			if valores[0]==ano and valores[1]==mes and valores[2]==fundo:

		