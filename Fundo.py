class Fundo(object):
	
	def __init__(self, ano, mes, fundo):
		self.ano=ano
		self.mes=mes
		self.fundo=fundo


	def rendaMes(self):
		arq=open("dados.txt","r")
		total=0.0
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano and valores[1]==self.mes:
				total+=(float(valores[6]))
		return total
		arq.close()

	def rendaAno(self):
		arq=open("dados.txt","r")
		total=0.0
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano:

				total+=(float(valores[6]))
		return total
		arq.close()


	def saldoFundoMes(self):
		arq=open("dados.txt","r")
		total=0.0
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano and valores[1]==self.mes and valores[5]==self.fundo:

				total+=(float(valores[6]))
		return total
		arq.close()

	def saldoFundoAno(self):
		arq=open("dados.txt","r")
		total=0.0
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano and valores[5]==self.fundo:

				total+=(float(valores[6]))
		return total
		arq.close()

