from Bio import SeqIO
for seq_record in SeqIO.parse("gencode.v19.pc_transcripts.fa", "fasta"):
     print(seq_record.id)
    print(repr(seq_record.seq))
     print(len(seq_record))