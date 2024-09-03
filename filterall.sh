list=$1

for f in $(cat $list); do
    fafile=$(ls *.pep.all.fa | grep -i $f)
    echo $fafile

    python3 filter.py -i $fafile -l 200 -m > ${f}_200_m.fa
done

cd OrthoFinder
mkdir all200seq
mv ../*200_m.fa all200seq
./orthofinder -f all200seq
