def to_rna(strand):
    dna_list = list()
    rna_list= list()
    dna=['A','T','C','G']

    for i in strand:
        if i in dna:
            dna_list.append(i)
        else:
            return ""

    for each in dna_list:
    	if each == "A":
    		rna_list.append("U")
    	elif each == "T":
    		rna_list.append("A")
    	elif each == "C":
    		rna_list.append("G")
    	elif each == "G":
    		rna_list.append("C")
    	else:
    		return ""

    rna = "".join(rna_list)
    return rna

to_rna('XXX')
to_rna('ACGTXXXCTTAA')
to_rna('G') #C