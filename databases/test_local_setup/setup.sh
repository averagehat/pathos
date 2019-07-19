
# Head to generate the following on a machine with acess to NT database.
# somehow it may be possible to use the smaller: wget http://ftp.ncbi.nlm.nih.gov/blast/db/taxdb.tar.gz
# LOCAL_NT_DB=
#echo "don't use me."
#exit 1
grep -o -- '>[^ ]*' head_nt_10k.fa | cut -c2- >  ids.lst 
blastdbcmd -db $LOCAL_NT_DB/nt -outfmt "%a %T" -entry_batch=ids.lst > taxid_map.txt 
sed "s/^>\([^ ]*\) />ref|\1| /g" head_nt_10k.fa > cut_10k.fa

mkdir -p smallnt && cd smallnt/ && makeblastdb -taxid_map ../taxid_map.txt  -in ../cut_10k.fa  -dbtype nucl -parse_seqids -out ./nt
