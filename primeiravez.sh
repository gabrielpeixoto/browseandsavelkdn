while read i; do
  echo "accessing https://www.google.com/webhp?#q={$i}&btnI=I"
  ./save_page_as.sh "https://www.google.com/webhp?#q={$i}&btnI=I" --destination "./alunos/$i.html" --load-wait-time 15 --save-wait-time 15;
done <nomes_alunos.txt

