
# This class is called by fasta function Usage: x = fasta(fastqID, fastqSeq, fastqQuality)
class Fasta: 
    def __init__(self, fastaId, fastaSeq):
        self.fastaId = fastaId 
        self.fastaSeq = fastaSeq

    def sequences(self): #return the sequences from fasta file in a list (usage: x.sequences())
        return self.fastaSeq
    def id(self): #return the id from fasta file in a list (usage: x.id())
        return self.fastaId
    def write(self, outputName): #write a fasta file (usage: x.write("output.fasta"))
        w = open(outputName, 'w')
        for i in range(len(self.fastaId)):
            w.write(f">{self.fastaId[i]}\n{self.fastaSeq[i]}\n")
        w.close()

# This class is called by fastq function  Usage: x = fastq(fastqID, fastqSeq, fastqQuality)
class FastQ:
    def __init__(self, fastqID, fastqSeq, fastqQuality):
        self.fastqID = fastqID
        self.fastqSeq = fastqSeq
        self.fastqQuality = fastqQuality

    def sequences(self): #return the sequences from fastq file in a list (usage: x.sequences())
        return self.fastqSeq
    def id(self): #return the id from fastq file in a list (usage: x.id())
        return self.fastqID
    def write(self, outputName): #write a fastq file (usage: x.write("output.fasta"))
        w = open(outputName, 'w')
        for i in range(len(self.fastqID)):
            w.write(f"@{self.fastqID[i]}\n{self.fastqSeq[i]}\n+\n{self.fastqQuality[i]}")

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

    def readFastq(self):
        fastq_file = open(self.file, 'r')
        fastq_file_line = fastq_file.readlines()
        fastq_file.close()

        fastqID, fastqSeq, fastqQuality = [], [], []

        for l in range(len(fastq_file_line)-3):
            if '@' in fastq_file_line[l]:
                fastqID.append(fastq_file_line[l].rstrip().replace('@',''))
                fastqSeq.append(fastq_file_line[l+1].rstrip())
                fastqQuality.append(fastq_file_line[l+3].rstrip())

        return fastqID, fastqSeq, fastqQuality

def bioReader(file):
    return BioReader(file)

def fasta(fastaID, fastaSeq):
    return Fasta(fastaID, fastaSeq)

def fastq(fastqID, fastqSeq, fastqQuality):
    return FastQ(fastqID, fastqSeq, fastqQuality)