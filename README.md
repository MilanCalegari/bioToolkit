# bioinfoToolkit

![Bioinfo](https://img.shields.io/badge/-bioinformatics-brightgreen)  ![Python](https://img.shields.io/badge/Py-module-red)  ![forks](https://img.shields.io/github/forks/MilanCalegari/bioinfoToolkit)  ![Stars](https://img.shields.io/github/stars/MilanCalegari/bioinfoToolkit)  ![issues](https://img.shields.io/github/issues/MilanCalegari/bioinfoToolkit)  ![license](https://img.shields.io/github/license/MilanCalegari/bioinfoToolkit)  ![WIP](https://img.shields.io/badge/work%20in%20progress-WIP-yellow)

bioToolkit is a Python library to deal with biological data

## Usage

1. bioIO
   1. Reading, creating and writing FASTA files  
      ```python
      from bioinfoToolkit.bioIO import *

      #Reading a fasta file

      fasta_file = bioreader("file.fasta").readFasta() 
      fasta_id = fasta_file.id() #Create a list with the description lines contained in the fasta file.
      fasta_seq = fasta_file.sequences() #Create a list with the sequences contained in the fasta file.

      #Creating and writing your own fasta

      my_sequences = ['ATCG','CGAT']
      my_id = ['exemple_1', 'exemple_2']

      my_fasta = fasta(my_id, my_sequences)
      my_fasta.write("output.fasta")
      ```

   2. Reading, creating and writing FASTQ files  

       ```python
       from bioinfoToolkit.bioIO import *
       
       #Reading a fastq file
       
       fastq_file = bioReader("file.fastq").readFastq()
       fastq_id = fastq_file.id()
       fastq_seq = fastq_file.sequences()
       fastq_quality = fastq_file.qualities()
       
       ```
2. biofunctions
    1. couting
    2. transcription
    3. translastion
    4. reverseComplement
    5. RandomDNA
    6. consensus
    7. profile

3. biodistance
   1. editDistace
   2. hammingDistance
