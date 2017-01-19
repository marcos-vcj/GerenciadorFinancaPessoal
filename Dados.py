class Dados(object):
    
    def __init__(self,ano,mes,dia,categoria,descricao,fundo,valor):
        self.dia=dia
        self.mes=mes
        self.ano=ano
        self.categoria=categoria
        self.descricao=descricao
        self.fundo=fundo
        self.valor=valor
        
    def carregaArquivo(self):
        arq=open("dados.txt","r")
        
        for linha in arq:
            info=linha.split()
            print info               #colocar na interface
        arq.close()
        
    def novoDado(self):
        arq=open("dados.txt","a")

        arq.write(self.ano + ' ' + self.mes + ' ' + self.dia + ' ' + self.categoria + ' ' + self.descricao + ' ' + self.fundo + ' ' + self.valor + "\n")
        arq.close()

    def categorias(self):
        arq=open("dados.txt","r")
        lisCategoria=[]
        for linha in arq:
            valores=linha.split()
            if valores[3] not in lisCategoria:
                lisCategoria.append(valores[3])
        arq.close
        return lisCategoria

    def fundos(self):
        arq=open("dados.txt","r")
        lisFundos=[]
        for linha in arq:
            valores=linha.split()
            if valores[5] not in lisFundos:
                lisFundos.append(valores[5])
        arq.close()
        return lisFundos
            
