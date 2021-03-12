from collections import Counter
from random import randint

def counting(dna):
    counter = Counter(dna)
    
    return counter

def transcription(dna):
    tdna = dna.replace('T','U').replace('t','u')
    
    return tdna

def translastion(dna):
  protein = ''
  codon_table = {
      'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
      'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
      'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
      'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
      'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
      'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
      'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
      'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
      'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
      'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
      'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
      'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
      'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
      'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
      'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
      'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    for i in range(0,len(dna),3):
    if len(dna[i:i+3]) == 3:
      codon = codon_table[dna[i:i+3]]
      if codon == '_':
        break
      protein += codon

  return protein

def reverseComplement(dna):
    conversion_table = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement = [conversion_table[i] for i in dna]
    
    return ''.join(complement)[::-1]

def RandomDNA(length):
    table = {0:'A', 1:'T', 2:'C', 3:'G'}
    seq = ''
    for _ in range(length):
        seq += table[randint(0,3)]
    
    return seq

def consensus(dna_list):
    pass

def profile(dna_list):
    pass
