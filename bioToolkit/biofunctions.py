from collections import Counter
from random import randint

def counting(dna):
    counter = Counter(dna)
    
    return counter

def transcription(dna):
    tdna = dna.replace('T','U').replace('t','u')
    
    return tdna

def tranlastion(dna):
    pass

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
