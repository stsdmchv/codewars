''' In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". '''


def DNA_strand(dna):
    text2 = "" 
    for symbol in symbols:
        if(symbol == "A"):
            text2 += "T"
        if(symbol == "T"):
            text2 += "A"
        if(symbol == "G"):
            text2 += "C"
        if(symbol == "C"):
            text2 += "G"
    return text2

def DNA_strand(dna):
    return dna.translate(string.maketrans('ATCG', 'TAGC'))


def DNA_strand(dna):
    return ''.join([{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[letter] for letter in dna])