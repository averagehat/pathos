dir=$HOME/path-pipe
mkdir -p star-index-dir
# STAR --runMode genomeGenerate --runThreadN 4 --genomeFastaFiles $dir/hg38.fa $dir/panTro4.fa --genomeDir star-index-dir 
STAR --runMode genomeGenerate --runThreadN 16 --genomeFastaFiles $dir/hg38.fa $dir/panTro4.fa --genomeDir star-index-dir --limitGenomeGenerateRAM 35085737173

gmap_build -D gmap-conf -d nt-gmap -k 16 $dir/nt2.fasta 
