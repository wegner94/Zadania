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
backbone_list = []
backbone2_list = []

# Z jakiegoś powodu jednokrotne usunięcie atomów nie wystarcza: tzn wciąż pewne zostają. Kilkukrotne powtórzenie usuwania eliminuje problem, stąd pętla

for i in range(1,5):
    for res in st_1ehz[0]['A']:
        for at in res:
            if at.get_name() not in ['P', 'OP1', 'OP2', "O5'", "C5'", "C4'", "O4'", "C1'", "C2'", "O2'", "C3'", "O3'" ]:
                backbone_list.append(at.name)
                id = at.id
                res.detach_child(id)
    print backbone_list.index('N3')
    backbone_list = []


out = PDBIO()
out.set_structure(st_backbone)
out.save('1EHZ_backbone.pdb')
