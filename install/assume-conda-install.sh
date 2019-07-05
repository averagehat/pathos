# if needed . . . 
# export https_proxy=http://127.0.0.1:3128
# export http_proxy=http://127.0.0.1:3128 

# e.g. bash install.sh $PWD/../miniconda


set -e

if [ $# -ne 1 ]; then
  echo 1>&2 "Usage: $0 <INSTALL_DIRECTORY>"
  exit 3
fi

# CONDA install
MINICONDA=$1/miniconda
BIN=$MINICONDA/bin/
export PATH=$BIN:$PATH


# conda requirements
conda install -y --file conda-requirements-python.txt 
conda install -y --file conda-requirements-software.txt 

# python packages not present on conda
pip install -r requirements.txt 

# == PriceSeqFilter
PRICESOURCE=PriceSource140408
wget http://derisilab.ucsf.edu/software/price/${PRICESOURCE}.tar.gz 
tar -xvf ${PRICESOURCE}.tar.gz 
cd PriceSource140408 && make && ln -s $PWD/PriceSeqFilter $BIN/PriceSeqFilter && cd ..


# === cd-hit-dup ONLY (not the other cd-hit tools) 
git clone https://github.com/weizhongli/cdhit
cd cdhit/cd-hit-auxtools/ && make && ln -s $PWD/cd-hit-dup  $BIN/cd-hit-dup
