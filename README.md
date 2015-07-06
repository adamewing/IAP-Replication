## IAP-Replication


# Prerequisites:

|what     | where                            | version |
|---------|----------------------------------|---------|
|bwa      | http://bio-bwa.sourceforge.net/  | 0.7.12  |
|samtools | http://samtools.sourceforge.net/ | 1.2     |
|pysam    | pip install pysam                | 0.8.1   |
|sra-tools| https://github.com/ncbi/sra-tools| 2.5.2   |



# Obtain reference information that was too big to put into this repository:

```
cd ref/bwa/mm9
./make_ref.sh
cd ../../map
./mouse_mappability.sh
```

# Obtain sequence data from SRA:

```
wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR201/SRR2014794/SRR2014794.sra
wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR201/SRR2014795/SRR2014795.sra
```

# Extract sequence data to FASTQ:

```
fastq-dump --split-files -O . SRR2014794.sra
fastq-dump --split-files -O . SRR2014795.sra
```

# Map sequence data to mouse reference genome:

```
bwa mem -t 8 -R "@RG\tID:H33WT\tSM:H33WT\tPL:ILLUMINA" ref/bwa/mm9/mm9.fa SRR2014794_1.fastq SRR2014794_2.fastq | samtools view -Su - | samtools sort -@ 8 -m 2G - H33WT.sorted
bwa mem -t 8 -R "@RG\tID:H33KO1\tSM:H33KO1\tPL:ILLUMINA" ref/bwa/mm9/mm9.fa SRR2014795_1.fastq SRR2014795_2.fastq | samtools view -Su - | samtools sort -@ 8 -m 2G - H33KO1.sorted
```

# Identify IAP insertions

```
./discocluster --bam H33WT.sorted.bam,H33KO1.sorted.bam --bed ref/rmsk/mm9/IAP.mm9.rmsk.bed > H33.result.txt
```

