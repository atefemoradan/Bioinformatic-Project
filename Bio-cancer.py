import GEOparse
gse = GEOparse.get_GEO(geo="GSE2034", destdir="/home/atefeh/Desktop/Bio")
dfg=gse.pivot_samples("VALUE")
dfg=dfg.T