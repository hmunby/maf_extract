## maf_extract
Command-line tool to extract alignment blocks in a particular region from a Multiple Alignment File. 
Any blocks covering the specified region are printed to standard output as they appear in the input MAF, including any commented lines. 
### Usage
`python3 ./maf_extract.py /path/to/alignment_file_to_be_searched.maf sequence_of_interest start end`
<br /> 
e.g. searching Ensembl 75 fish aligmnent for any blocks covering Astatotilapia calliptera chromosome 7:10,400,000-10,600,000
<br /> 
`python3 ./maf_extract.py 75_fish.epo_low_coverage.12_2.maf astatotilapia_calliptera.7 10400000 10600000`
<br />

Reference sequence for search can be any present in the alignment (i.e. doesn't have to be the same as the reference sequence for the alignment being searched), its name must be given as it appears in the MAF. 