=============
Configuration
=============

The configuration file is specified with the `-c` option when running `pathos_sheet` or `pathos_single`. There is an example file at the bottom of the page. Particular options:

`assembler:` should be `ray2` or `abyss`

the assembly `options` are the commandline options used with the chosen assembler.

`param_file` is the pathdiscov param.txt file used for the ray2/CAP assembly. 

The `bowtieDB` and `starDB` filepaths refer to host index databases (they must have already been indexed by `bowtie-build` and `STAR` respectively).

The `minCompressionScore` of `lzwfilter` is the minimum "read complexity" that the filtering algorithm uses to determine to keep the read for further processing. The compression score of a read is calculated by dividing the length of the compressed read by the length of the original read.

The `max_target_seqs` flag of `blastn` tells BLAST to stop searching after finding that many sequence matches. A high number results in long BLAST runtimes. 

.. code-block:: yaml

    pricefilter:
      highQualPercent: 85
      calledPercent: 90
      highQualMin: 0.98
    bowtie2:
      bowtieDB: /Users/happyuser/pathos/databses/test/human-bowtie/bowtie-index
    star:
      starDB: /Users/happyuser/pathos/databses/test/star-index-dir/
      skip: true
    threads: 16
    assembly:
      assembler: ray2
      options: " "
      kmer: 25
      minimum_contig_length: 200
    cdhitdup:
      minDifference: 5
    ncbi:
      ntDB: /Users/happyuser/pathos/databses/test/nt/nt
      nrDB: /Users/happyuser/pathos/databses/test/nr/nr
      ktTaxonomy: /Users/happyuser/pathos/databses/test/krona
    lzwfilter:
      minCompressionScore: 0
    blastn:
      max_target_seqs: 3
    param_file: /Users/happyuser/pathos/param.txt
    ete2_db:
