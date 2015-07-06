#!/bin/sh

wget http://hgdownload.cse.ucsc.edu/goldenPath/mm9/bigZips/chromFa.tar.gz
tar xvzf chromFa.tar.gz
cat chr*.fa > mm9.fa
bwa index -a bwt mm9.fa
samtools index mm9.fa
