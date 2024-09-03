list=$1

for f in $(cat $list);
do
    rsync -av rsync://ftp.ensembl.org/ensembl/pub/current_fasta/$f/pep/*all*.gz .
done

gunzip *.gz
