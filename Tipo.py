import fileinput

class Tipo(object):
	def __init__(self,nome,categoria):
		self.nome = nome
		self.categoria = categoria

	def lerTipo(self):
		arq=open("Tipos.txt","r")
		for linha in arq:
			info.linha.split()
			print info

		arq.close()

	def novoTipo(self):
		arq=open("Tipos.txt","a")
		arq.write(self.nome + ' ' + self.categoria + '\n') #fazer com q de de escrever mais de uma categoria (pensei em inserir uma lista, mas daria problema se precisar add uma categoria a um tipo ja existente)
		arq.close()

	def pertencentesTipo(self):
		for linha in fileinput.input("Tipos.txt"):
			info=linha.split()
			if self.nome==info[0]:
				arq.write(' '+ self.categoria + '\n')
				

teste=Tipo('Habitação','Energia')
Tipo.novoTipo(teste)
Tipo.pertencentesTipo(teste)