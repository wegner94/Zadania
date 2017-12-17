from Bio import PDB
from Bio.PDB import PDBParser, NeighborSearch, Superimposer, PDBIO
from Bio.PDB.Atom import Atom 
from Bio.PDB.Residue import Residue
from Bio.PDB.Chain import Chain
from Bio.PDB.Model import Model
from Bio.PDB.Structure import Structure

parser = PDBParser()
st_1ehz = parser.get_structure('my structure','D:\\Python27\\Programs\\1EHZ.pdb')

for res in st_1ehz[0]['A']:
        if res.id[1] not in range(26,45):
                st_1ehz[0]['A'].detach_child(res.id)
out = PDBIO()
out.set_structure(st_1ehz)
out.save('1EHZ_anticodon.pdb')
