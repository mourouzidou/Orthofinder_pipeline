import argparse
import re

parser =  argparse.ArgumentParser(description = 'Filter fasta files')
parser.add_argument('-i', '--input', help = 'Input File Name')
parser.add_argument('-l', '--length', type = int, help = 'Minimum length of sequence')
parser.add_argument('-m', '--meth', help = 'Methionine as the first aminoacid', action = "store_true")


args = parser.parse_args()

with open(args.input) as f:
    seq = ""
    entry = ""
    while True:
        line = f.readline().strip()

        if ">" in line:
            if len(seq.strip()) > args.length and ( (args.meth and seq.strip()[0] =='M') or (args.meth == False)):
                print(entry,"\n"+seq)
            entry = re.sub("pep.*", "", line)

            seq = ""
            continue

        seq = "".join([seq, line])
        if not line:
            break

    if len(seq.strip()) > args.length:
        print(entry, seq)


