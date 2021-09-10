
import fuzzySearch 


print(fuzzySearch.hammingDist("GCGTATGCCGCTAACC","TATTGGCTATACGGTT"))

#print(fuzzySearch.editDistRecur("Shakespeare", "shake spear"))
print(fuzzySearch.editDistOptm("Shakespeare", "shake spear"))
print(fuzzySearch.funzzyEditDist("GCGTATGC","TATTGGCTATACGGTT"))
