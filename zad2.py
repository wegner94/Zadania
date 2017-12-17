# nie jestem pewien dlaczego to nie działa. Pojawia się błąd:
# AttributeError: 'module' object has no attribute 'array'

from Bio import PDB
from Bio.PDB import PDBParser, NeighborSearch, Superimposer, PDBIO
from Bio.PDB.Atom import Atom 
from Bio.PDB.Residue import Residue
from Bio.PDB.Chain import Chain
from Bio.PDB.Model import Model
from Bio.PDB.Structure import Structure

my_structure = Structure('Cytosine')
my_model = Model(0)
my_chain = Chain('A')
my_residue  = Residue((' ',1,' '), 'C', ' ')
atoms = [
{'name': 'N1',  'coord': PDB.Atom.array([64.612, 45.818, 10.877],'f'), 'bfactor': 42.59, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'N1', 'serial_number': 1},
{'name': 'C2',  'coord': PDB.Atom.array([65.472, 46.868, 10.634],'f'), 'bfactor': 44.48, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'C2', 'serial_number': 2},
{'name': 'O2',  'coord': PDB.Atom.array([64.981, 47.978, 10.348],'f'), 'bfactor': 42.73, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'O2', 'serial_number': 3},
{'name': 'N3',  'coord': PDB.Atom.array([66.821, 46.659, 10.722],'f'), 'bfactor': 42.28, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'N3', 'serial_number': 4},
{'name': 'C4',  'coord': PDB.Atom.array([67.275, 45.452, 11.056],'f'), 'bfactor': 43.75, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'C4', 'serial_number': 5},
{'name': 'N4',  'coord': PDB.Atom.array([68.586, 45.272, 11.180],'f'), 'bfactor': 44.57, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'N4', 'serial_number': 6},
{'name': 'C5',  'coord': PDB.Atom.array([66.402, 44.364, 11.291],'f'), 'bfactor': 44.20, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'C5', 'serial_number': 7},
{'name': 'C6',  'coord': PDB.Atom.array([65.095, 44.589, 11.192],'f'), 'bfactor': 44.33, 'occupancy': 1.0, 'altloc': ' ', 'fullname': 'C6', 'serial_number': 8}
]
my_structure.add(my_model)
my_model.add(my_chain)
my_chain.add(my_residue)

for atom in atoms:
	my_atom = Atom(atom['name'], atom['coord'], atom['bfactor'], atom['occupancy'], atom['altloc'], atom['fullname'], atom['serial_number'] )
	my_residue.add(my_atom)

out = PDBIO()
out.set_structure(my_structure)
out.save('my_new_structure.pdb')
