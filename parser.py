import glob
import re

# https://stackoverflow.com/questions/14118352/how-to-convert-unicode-accented-characters-to-pure-ascii-without-accents
def remove_accents(string):
    #if type(string) is not unicode:
    #    string = unicode(string, encoding='utf-8')

    string = re.sub(u"[àáâãäå]", 'a', string)
    string = re.sub(u"[èéêë]", 'e', string)
    string = re.sub(u"[ìíîï]", 'i', string)
    string = re.sub(u"[òóôõö]", 'o', string)
    string = re.sub(u"[ùúûü]", 'u', string)
    string = re.sub(u"[ùúûü]", 'u', string)
    string = re.sub(u"[ç]", 'c', string)
    return string

# conteúdo html, nome do arquivo (nome-do-aluno no padrão com JOAO+PAULO+LINKEDIN.HTML)
def verificar_aluno(dados, aluno):
  #aluno = procurado[:-len("+LINKEDIN.HTML")] # pegar nome do aluno: remover LINKEDIN.HTML
  #aluno = aluno[len("alunos/"):] # remover "alunos/"
  #aluno = aluno.replace("+"," ")
  aluno = remove_accents(aluno)
  #result = aluno+":"
  # https://stackoverflow.com/questions/6579876/how-to-match-a-substring-in-a-string-ignoring-case
  if re.search(aluno, dados, re.IGNORECASE):
    result = "ok"
  else:
    result = "x"
  return result

#saved from url=(0060)https://www.linkedin.com/in/aline-da-silva-venera-a91212173/ -->
def buscar_url_linkedin_salva(dados):
  posi1 = dados.find("https://www.linkedin.com/in/")
  posi2 = dados.find("-->")
  url = dados[posi1:posi2-1]
  if (posi1 == -1) or (posi2 == -1) or (posi1 > posi2):
    return "x"
  else:
    return url



arqs = glob.glob("alunos/*.html")

for arq in arqs:
  
  f2 = open(arq, "r")
  try:
    data = f2.read()

    empresas = ''
    corta = data
    procurado = '"companyName":"'
    #procurado = '"worksFor":"'
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

    # se houver "+LINKEDIN.HTML" no nome do arquivo, está sendo feita a parte A;
    # senão, está sendo feita a parte B (nome do aluno sem + nem LINKEDIN)
    aluno = arq
    if re.search("LINKEDIN.HTML", arq, re.IGNORECASE):
      aluno = arq[:-len("+LINKEDIN.HTML")] # pegar nome do aluno: remover LINKEDIN.HTML
      aluno = aluno.replace("+"," ")
    else:
      aluno = arq[:-len(".HTML")] # pegar nome do aluno: remover .HTML
    
    aluno = aluno[len("alunos/"):] # remover "alunos/"

    nome_aluno = verificar_aluno(data, aluno)
    url_linkedin = buscar_url_linkedin_salva(data)
    if (nome_aluno == "x") or (url_linkedin == "x"):
      status = "x"
    else:
      status = "ok"
    print(aluno + "|" + url_linkedin + "|" + status + "|" + empresas)
  except:
    print("ERRO AO LER: "+arq)
  