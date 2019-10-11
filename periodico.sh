while read i; do
  IFS=',' # , is set as delimiter
  read -ra ADDR <<< "$i" # i is read into an array as tokens separated by IFS
  echo ${ADDR[1]}
  echo "accessing ${ADDR[1]}"
  ./save_page_as.sh "${ADDR[1]}" --destination "./alunos/${ADDR[0]}.html" --load-wait-time 15 --save-wait-time 15;
done < corretos.txt

