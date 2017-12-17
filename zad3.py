from Bio import PDB
from Bio.PDB import PDBParser, NeighborSearch, Superimposer, PDBIO
from Bio.PDB.Atom import Atom 
from Bio.PDB.Residue import Residue
from Bio.PDB.Chain import Chain
from Bio.PDB.Model import Model
from Bio.PDB.Structure import Structure

parser = PDBParser()
st_1ehz = parser.get_structure('my structure','D:\\Python27\\Programs\\1EHZ.pdb')

PDB.extract(st_1ehz, 'A', 26, 44, 'D:\\Python27\\Programs\\1EHZ_anticodon.pdb')
