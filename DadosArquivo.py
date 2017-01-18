'''
Created on 9 de jan de 2017

@author: mvcjk
'''

class Arquivos(object):
    
    def __init__(self,dia,mes,ano,categoria,descricao,fundo):
        self.dia=dia
        self.mes=mes
        self.ano=ano
        self.categoria=categoria
        self.descricao=descricao
        self.fundo=fundo
        
    def carregaArquivo(self):
        arq=open("dados.txt","r")
        
        for linha in arq:
            valores=linha.split() 
            print(valores[0])
        arq.close()
        
    def novoDado(self):
        arq=open("dados.txt","a")
        arq.write(self.ano,self.mes,self.dia,self.categoria,self.descricao,self.fundo,"\n")
        arq.close()
        
        
        