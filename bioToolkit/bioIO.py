class Fasta:
    def __init__(self, fastaId, fastaSeq):
        self.fastaId = fastaId 
        self.fastaSeq = fastaSeq

    def sequences(self):
        return self.fastaSeq
    def id(self):
        return self.fastaId


class BioReader:
    def __init__(self, file):
        self.file = file
    
    def readFasta(self):
        fasta_file = open(self.file, 'r')
        fasta_file_lines = fasta_file.readlines()
        fasta_file.close()

        fastaID, fastaSeq = [], []

        for l in range(len(fasta_file_lines)-1):
            if '>' in fasta_file_lines[l]:
                fastaID.append(fasta_file_lines[l].rstrip().replace('>',''))
                fastaSeq.append(fasta_file_lines[l+1].rstrip())
        
        opened_fasta = fasta(fastaID, fastaSeq)

        return opened_fasta
    



def bioReader(file):
    return BioReader(file)

def fasta(fastaId, fastaSeq):
    return Fasta(fastaId, fastaSeq)