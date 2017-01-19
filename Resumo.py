
class Resumo(object):
	
	def __init__(self,ano,mes,categoria):
		self.mes=mes
		self.ano=ano
		self.categoria=categoria

	def filtraCategoria(self):
		arq=open("dados.txt","r")
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano and valores[1]==self.mes and valores[3]==self.categoria:
				print valores
		arq.close()

	def filtraAnoMes(self):
		arq=open("dados.txt","r")
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano and valores[1]==self.mes:
				print valores
		arq.close()
