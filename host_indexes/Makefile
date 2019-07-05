
all:  star-index-dir/SAindex bowtie-index.1.bt21

hg38.fa.gz:
	wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz

panTro4.fa.gz:
	wget http://hgdownload.cse.ucsc.edu/goldenPath/panTro4/bigZips/panTro4.fa.gz

panTro4.fa: panTro4.fa.gz
	gunzip panTro4.fa.gz

hg38.fa: hg38.fa.gz
	gunzip hg38.fa.gz

star-index-dir/SAindex: hg38.fa panTro4.fa
	mkdir -p star-index-dir
	STAR --runMode genomeGenerate --runThreadN 24 --genomeFastaFiles hg38.fa panTro4.fa --genomeDir star-index-dir --limitGenomeGenerateRAM 35085737173  2>&1 > star-build.log 

bowtie-index.1.bt21: hg38.fa panTro4.fa
	bowtie2-build  panTro4.fa,hg38.fa bowtie-index --threads 24  --large-index 2>&1 > bowtie-build.log 


# TODO: ktUpdateTaxonomy.sh $SOMEDIR
