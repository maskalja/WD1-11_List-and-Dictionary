
with open("dna.txt", "r") as dna:
    genes = dna.read()
    # print(genes)

gene_pool = {"black_hair": "CCAGCAATCGC", "brown_hair": "GCCAGTGCCG", "blonde_hair": "TTAGCTATCGC",
             "square_face": "GCCACGG", "round_face": "ACCACAA", "oval_face": "AGGCCTCA",
             "blue_eyes": "TTGTGGTGGC", "green_eyes": "GGGAGGTGGC", "brown_eyes": "AAGTAGTGAC",
             "male": "TGCAGGAACTTC" , "female": "TGAAGGACCTTC",
             "white_race": "AAACCTCA", "black_race": "CGACTACAG", "asian_race": "CGCGGGCCG"}
# print(gene_pool["black_hair"])

if gene_pool["female"] and gene_pool["white_race"] and gene_pool["blonde_hair"] and gene_pool["blue_eyes"] and gene_pool["oval_face"] in genes:
    print("It was Eva!")
elif gene_pool["female"] and gene_pool["white_race"] and gene_pool["brown_hair"] and gene_pool["brown_eyes"] and gene_pool["oval_face"] in genes:
    print("It was Larisa!")
elif gene_pool["male"] and gene_pool["white_race"] and gene_pool["black_hair"] and gene_pool["blue_eyes"] and gene_pool["oval_face"] in genes:
    print("It was Matej!")
elif gene_pool["male"] and gene_pool["white_race"] and gene_pool["brown_hair"] and gene_pool["green_eyes"] and gene_pool["square_face"] in genes:
    print("It was Miha!")


print("---------------------------------")
print ("Argumentation:")

if gene_pool["female"] in genes:
    print("Suspect is female.")
else:
    print("Suspect is male.")

if gene_pool["white_race"] in genes:
    print("Suspect's race is white.")
elif gene_pool["black_race"] in genes:
    print("Suspect's race is black.")
else:
    print("Suspect's race is asian.")

if gene_pool["black_hair"] in genes:
    print("Suspect has black hair.")
elif gene_pool["brown_hair"] in genes:
    print("Suspect has brown hair.")
else:
    print("Suspect has blonde hair.")

if gene_pool["square_face"] in genes:
    print("Suspect has square face.")
elif gene_pool["round_face"] in genes:
    print("Suspect has round face.")
else:
    print("Suspect has oval face.")

if gene_pool["blue_eyes"] in genes:
    print("Suspect has blue eyes.")
elif gene_pool["green_eyes"] in genes:
    print("Suspect has green eyes.")
else:
    print("Suspect has brown eyes.")

print("---------------------------------")