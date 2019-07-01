import pandas as pd
from operator import add
from itertools import accumulate
import os
from StringIO import StringIO



LCD_RANK_FIELD_NAME = 'Lowest Common Rank'


def n50(lens):
    half = sum(lens) / 2.0
    lns = sorted(lens, reverse=True)
    accumulated = accumulate(lns, add)
    whereOverHalf = [lns[i] for i,acc in enumerate(accumulated) if acc > half]
    return whereOverHalf[0]

DUMB_INDEX = [0]
# TODO: size doesn't do what I think it does!
def summ_contigs(tops):
  return pd.DataFrame(index = DUMB_INDEX, data={ 'N50' : n50(tops.qlen),
                       'contig_count' : len(tops),
                       'assembly_length' :  tops.qlen.sum(),
                       'species_count' : tops.species.unique().size })


def count(gen):
  return sum(1 for _ in gen)

def readCount(fp, format='fastq'):
    gen = SeqIO.parse(open(fp), format)
    return sum(1 for _ in gen)

#TODO: this needs to know about filepaths;
#
def summarize_nontaxon():
  # summary df ->
  # really all this needs is the filenames.
  # could return tops and summ_df to avoid any i/o here
  summ_df = pd.Dataframe(index = DUMB_INDEX)
  # actuallyt hese are totaly independent and should be treated as such
  summ_df['raw_contig_count'] = readCount(unfiltered_contigs)
  summ_df['sample_input'] = readCount(input1)
  summ_df['star_host_count'] = readCount(star1) - sample_input
  summ_df['bowtie_host_count'] = readCount(_bowtie1) - readCount(lzw1)
  summ_df['host_reads'] = star_host_count + bowtie_host_count
  summ_df['unblasted_contigs'] = readCount(contigs, 'fasta') - count(contig_top_summary) - 1 # for header lin
  return summ_df
  # return None

def to_tops(df):
  gbs = df.groupby('qseqid')
  lcd_ranks = gbs.apply(lcdRank)
  tops = df.sort_values('pident', ascending=False).groupby('qseqid').first()
  tops[LCD_RANK_FIELD_NAME] = lcd_ranks
  tops.reset_index(inplace=True)
  return tops


#NOTE: Text overlaps in e.g. kingdom, when most only fit into one.
#NOTE: This doesn't give info when the parent rank is under-represented,
# i.e. it won't give us the top 5
def plot_rank(group, rank, rankpath):
    read_sorted =  group.read_count.sort_values(ascending=False)
    tooBig = read_sorted.size > 7
    if tooBig:
        others = pd.Series(read_sorted[5:].sum() , index=['others'])
        to_plot = pd.concat([read_sorted[:5], others])
    else:
        to_plot = read_sorted
    # to_plot.plot.pie(y='read_count')
    to_plot.plot.pie()
    #plt.ylabel(rank)
    plt.ylabel('') # remove to make more space for labels
    plt.savefig(rankpath + '.png')
    plt.close() # otherwise plot will look weird with "others" apparently not working and lots of labels


def make_rank_summaries(df, rankdir):
  if not os.path.exists(rankdir): os.mkdir(rankdir)
  rank_dfs = []
  ranks_str = "SuperKingdom | Kingdom | Phylum | Class_ | Order | SuperFamily | Family | Genus | Species"
  ranks = list(map(str.lower, map(str.strip, ranks_str.split('|'))))
  # TODO: do the below also for the whole of the top contigs.
  for rank in ranks:
    gb = df.groupby(rank)
    aggregated = gb.agg({'qseqid' : lambda x: ','.join(set(x)), # 'qlen' : sum,
                      'staxids' : lambda x: ','.join(x.unique()),
                       'read_count' : sum })
    # the value is a function on the series of just that thing.
    N50s = gb.qlen.apply(n50)
    aggregated['N50'] = N50s
    aggregated['contig_count'] = gb.size() # no this isn't correct, is it?
    aggregated['assembly_length'] = gb.qlen.sum()
    aggregated['species_count'] = gb.species.unique().agg(len)
    rankpath = os.path.join(rankdir, rank)
    columns = ['N50', 'contig_count', 'assembly_length', 'read_count', 'species_count',  'staxids', 'qseqid']
    aggregated.to_csv(rankpath + '.tsv', sep='\t', columns=columns)
    plot_rank(aggregated, rank, rankpath)
    aggregated['taxon'] = rank
    rank_dfs.append(aggregated)
  big_df = pd.concat(rank_dfs)
  big_summary_fp os.path.join(rankdir, 'ranksummary.tsv')
  aggregated.to_csv(big_summary_fp, sep='\t', columns= (columns + ['taxon']))
  return None

in_fp = 'contigs.15383.nt.tsv'
def summarize(in_summary_fp, outdir):
  in_df = pd.read_csv(open(in_summary_fp, sep='\t')
  rankdir = os.path.join(outdir, 'ranks/')
  make_rank_summaries(in_df, rankdir)
  tops = to_tops(in_df)
  p = partial(os.path.join, outdir)
  tops_fp = p('top_summary.tsv')
  tops.to_csv(tops_fp, sep='\t') # do I need to specify columns?
# summ_df can't be done without knowledge of other files.

  summ_df_ctg = summ_contigs(tops)
  summ_df_reads = summarize_nontaxon(tops)
  summ_fp = p('run_summary.tsv')
  summ_df.to_csv(summ_fp, sep='\t')

if __name__ == '__main__':
  summarize(

# need to rename qlen->assemblyLength, add:
 # mean conting length
 # unblasted contig count
 #
 # possibly unfiltered stats




# don't really want sample->contaminant mapping count. We'll stop using it prob.
# STAR produces a sam file
# calculate number of host reads by subtracting readcounts from each other, or via samtools idxstats.
# then adding the results from the two host-mapping stages
# assumes its sorted/indexed. must be a BAM.
# get unmapped reads from 'unmapped' column of last (ref='*') row.

def get_idx_stats(indexed_bam):
  idxstats_cmd=sh.samtools.idxstats(bam)
  idxstats_str = '\n'.join(idxstats)
  fields=['ref', 'ref_length', 'mapped', 'unmapped']
  idx_stats = pd.read_csv(StringIO(idxstats_str), sep='\t', header=None, names=fields)



