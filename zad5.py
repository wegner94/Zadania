from Bio import PDB
from Bio.PDB import PDBParser, NeighborSearch, Superimposer, PDBIO
from Bio.PDB.Atom import Atom 
from Bio.PDB.Residue import Residue
from Bio.PDB.Chain import Chain
from Bio.PDB.Model import Model
from Bio.PDB.Structure import Structure

parser = PDBParser()
st_1ehz = parser.get_structure('my structure','D:\\Python27\\Programs\\1EHZ.pdb')

atoms_list = []
at_gen = st_1ehz.get_atoms()

# Z jakiegoś powodu jednokrotne usunięcie atomów nie eliminuje wszystkich. Stąd pętla while która pracuje tak długo aż pozostaną tylko pożądane atomy
counter = 0
next = 'true'
while next == 'true':
    counter = counter +1
    next = 'false'
    for res in st_1ehz[0]['A']:
        for at in res:
            if at.get_name() not in ['P', 'OP1', 'OP2', "O5'", "C5'", "C4'", "O4'", "C1'", "C2'", "O2'", "C3'", "O3'" ]:
                next = 'true'
                id = at.id
                res.detach_child(id)

out = PDBIO()
out.set_structure(st_1ehz)
out.save('1EHZ_backbone.pdb')
