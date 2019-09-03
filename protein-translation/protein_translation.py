
import re

d_codon = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
           'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}


def proteins(strand):
    len_strand = len(strand)
    if len_strand % 3 != 0:
        raise ValueError
    else:
        acids = []
        l_cod = re.findall('...', strand)
        print(l_cod)
        for i in l_cod:
            atom = d_codon.get(i)
            if atom == 'STOP':
                break
            else:
                acids.append(atom)
    return acids
