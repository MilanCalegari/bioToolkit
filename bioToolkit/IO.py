def remove_signal(header):
    header = header.replace('>','').rstrip()
    return header
    
def bioseq(file, inpfmt):
    if inpfmt == "fasta":
        fasta_reading = open(file,'r').readlines()
        
        dic = {}

        for l in range(len(fasta_reading)-1):
            if '>' in fasta_reading[l]:
                dic[remove_signal(fasta_reading[l])] = fasta_reading[l+1].rstrip()

    return list(dic.keys()), list(dic.values())
