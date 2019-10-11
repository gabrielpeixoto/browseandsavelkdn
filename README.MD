PARTE A (feita somente uma vez): descobrir URLs do linkedin dos alunos

1) abra o google chrome
2) abra uma guia no chrome; faça login no linkedin; 
3) obter nomes de todos os alunos do curso; 
4) preencher nomes de alunos no arquivo nomes_alunos_base.txt (um nome abaixo do outro). Pode-se copiar-e-colar os nomes de um relatório do SIGAA (listagem de docentes ativos).
5) rodar o processar_nomes_alunos_base.py (execução sugerida: python3 processar_nomes_alunos_base.py), que vai:
- gravar a saída do programa no arquivo "nomes_alunos.txt"
- remover acentos
- formatar os nomes conforme exemplo:
ALVORI+FELICIANO+LINKEDIN
ANDREI+ANTONIO+CAMPIGOTTO+LINKEDIN
6) deve haver uma pasta vazia (apague todos os arquivos/pastas pré-existentes, caso existam) chamada "alunos";
7) executar primeiravez.sh
- aguardar... esse programa vai visitar o google informando como critério de busca os itens do passo 2 e vai salvar os arquivos com esse mesmo nome
8) executar o programa parser.py, para ler os arquivos em /alunos e gerar a saída com diversas informações. Execução sugerida: python3 parser.py > primeiro.csv

9) abrir primeiro.csv no libreoffice, usar delimitador: "|"
10) ordenar linhas pela terceira coluna ("ok" ou "x"). Campos com "ok" estão corretos, mas pode-se verificar se as empresas retornadas aparentam estar certas (pode haver alguns errados). Salvar as duas colunas desses nomes com "ok" num arquivo chamado "corretos.txt".
=> selecionar colunas A e B até a linha do último correto
=> copiar
=> abrir gedit
=> colar
=> substituir: \t (tab) por vírgula
=> salvar no arquivo corretos.txt
11) salvar o arquivo .csv aberto no libreoffice como "dados-ANO-MÊS.ods" (exemplo: dados-2019-JUNHO.ods)

as informações disponíveis corretas são, em primeiro momento, aquelas com o status "ok"

12) se desejar, buscar e acertar as URLs dos incorretos (quanto desejar; melhor deixar os alunos constatarem o erro e informarem a URL correta)
13) os que forem consertados podem ser adicionados no arquivo "corretos.txt"

FIM DA PARTE A


PARTE B: feita periodicamente

1) aplicar correções de URL de linkedin na planilha de dados.ods, guia alunos
2) obter da planilha dados.ods os nomes dos alunos que tiverem os links corretos (ou seja, não-em-branco; pode-se ordernar por URL e considerar apenas aqueles com URL do linkedin): copiar colunas A e C, salvar em arquivo corretos.txt, contendo nome e url; trocar TAB por vírgula (corretos.txt deve ter as 2 colunas separadas por vírgula)
3) abra o google chrome
4) abra uma guia no chrome; faça login no linkedin
5) deve haver uma pasta vazia chamada "alunos" (apague todos os arquivos/pastas pré-existentes, caso existam)
6) ===> executar periodico.sh
- aguardar... esse programa vai percorrer o arquivo corretos.txt, visitando a url informada ao lado do nome do aluno, e vai salvar os arquivos com o nome de cada aluno
8) executar o programa parser.py, para ler os arquivos em /alunos e gerar a saída com diversas informações. Execução sugerida: python3 parser.py > periodico.csv
9) fazer análise como no passo 9 em diante da PARTE A (considerando periodico.csv em vez de primeiro.csv)

final) 

PARTE GERAL: resultados do parser.py
1) ordenar por "status"
2) apagar os que não estão "ok"
3) ordenar pelo primeiro campo de local de trabalho
4) apagar o que não possuem informação
5) publicar o resultado com os registros coerentes
