# 1
from re import *

dna = 'cgcgcATGcATGcgTGAcTAAcgTAGcgcgcgcgc'
dna = dna.lower()
orfpat = r'(?x) ( atg  (?: (?!tga|tag|taa) ... )*  (?:tga|tag|taa) )'
print findall(orfpat,dna)

# 2
from re import *

dna = 'cgcgcATGcATGcgTGAcTAAcgTAGcgcgcgcgc'
dna = dna.lower()
orfpat = r'(?x) (?= ( atg  (?: (?!tga|tag|taa) ... )*  (?:tga|tag|taa) ))'
s = findall(orfpat,dna)
if s:
     print ', '.join(s)
