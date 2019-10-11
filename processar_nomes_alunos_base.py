
import glob
import unidecode # pip3 install unidecode
import sys

ler = open("nomes_alunos_base.txt", "r")
#data = ler.readline()

gravar = open("nomes_alunos.txt","w")


encoding = "utf-8" # or iso-8859-15, or cp1252, or whatever encoding you use

for nome in ler:
  sem_quebra_de_linha = nome[:-1] # remover quebra de linha
  nome_limpo = unidecode.unidecode(sem_quebra_de_linha) # remove acentos

  #print(sys.argv[1])

  if len(sys.argv) == 2 and sys.argv[1] == 'single':
    novo = nome_limpo
  else:
    novo = nome_limpo.replace(" ","+") + "+LINKEDIN"

  gravar.write(novo+"\n")

gravar.close()

print("concluido")
'''

empresas = ''
corta = data
procurado = '"companyName":"'
pos = corta.find(procurado) # procura o procurado
while pos != -1:
  corta = corta[pos:] # corta o que tem pra trás
  fim = corta.find(',') # procura a vírgula
  item = corta[len(procurado):fim-1] # pega o item até a vírgula
  empresas += item + ", "
  corta = corta[fim:] # tira o que já foi utilizado
  pos = corta.find('"companyName":"') # repete a busca

if len(empresas) > 0:
  empresas = empresas[:-2]

aluno = arq[:-len("+LINKEDIN.HTML")] # pegar nome do aluno: remover LINKEDIN.HTML
aluno = aluno.replace("+"," ")

print(aluno + " => " + empresas)
'''