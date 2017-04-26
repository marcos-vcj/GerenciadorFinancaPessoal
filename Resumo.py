
class Resumo(object):
	
	def __init__(self,ano,mes,categoria):
		self.mes=mes
		self.ano=ano
		self.categoria=categoria

	def totalCategoria(self):
		arq=open("dados.txt","r")
		total=0.0
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano and valores[1]==self.mes and valores[3]==self.categoria:
				total+=(float(valores[6]))
		arq.close()
		return total

	def filtraAnoMes(self):
		arq=open("dados.txt","r")
		lista=[]
		for linha in arq:
			valores=linha.split()
			if valores[0]==self.ano and valores[1]==self.mes:
				lista.append(valores)
		arq.close()
		return lista
