from os import listdir

from Bio import PDB
from Bio.PDB import PDBParser, NeighborSearch, Superimposer, PDBIO

filelist = listdir('D:\Python27\Programs\pdb_structures')
parser = PDBParser()
i=0
struct_list = []
for file in filelist:
	i=i+1
	struct_list.append(parser.get_structure(i,'D:\\Python27\\Programs\\pdb_structures\\'+file))

resolution=struct_list[2].header['resolution']

for struct in struct_list:
	if struct.header['resolution']<=2:
		print(struct.header['name'])
		print(struct.header['resolution'])

