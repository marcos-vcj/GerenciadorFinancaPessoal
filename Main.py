from Dados import *
from Resumo import *
from Fundo import *

test=Dados('2017','01','18','Mercado','affs','Itau','-200')
Dados.novoDado(test)
Dados.carregaArquivo(test)
cat=Dados.categorias(test)
fun=Dados.fundos(test) 
print fun
print cat
res=Resumo('2017','01','Mercado')
tc=Resumo.totalCategoria(res)
print tc
f=Fundo('2017','01','Itau')
total=Fundo.rendaMes(f)
print total
