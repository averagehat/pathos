HUM_STAR=test/star-index-dir
HUM_BOWTIE_DIR=test/human-bowtie
FAKE_HUMAN=fake_human.fa
mkdir test/
mkdir -p $HUM_STAR
STAR --runMode genomeGenerate --runThreadN 24 --genomeFastaFiles $FAKE_HUMAN --genomeDir $HUM_STAR  2>&1 > star-build.log 

mkdir -p $HUM_BOWTIE_DIR
bowtie2-build  $FAKE_HUMAN $HUM_BOWTIE_DIR 2>&1 > bowtie-build.log 

mkdir -p test/nt && cd test/nt && makeblastdb -taxid_map ../../taxid_map.txt  -in ../../cut_10k.fa  -dbtype nucl -parse_seqids -out ./nt
