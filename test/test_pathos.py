import sh

def integrated1_test():
    sh.pathos_single(c='template.yaml', fastq="test/smalldata/R1.fq test/smalldata/R2.fq", o=testout_)
