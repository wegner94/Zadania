from Bio import PDB
from Bio.PDB import PDBParser, NeighborSearch, Superimposer, PDBIO
from Bio.PDB.Atom import Atom 
from Bio.PDB.Residue import Residue
from Bio.PDB.Chain import Chain
from Bio.PDB.Model import Model
from Bio.PDB.Structure import Structure

parser = PDBParser()
st_1ehz = parser.get_structure('my structure','D:\\Python27\\Programs\\1EHZ.pdb')

atom1 = st_1ehz[0]['A'][(' ',1,' ')]['P']
atom72 = st_1ehz[0]['A'][(' ',72,' ')]['P']
atom2 = st_1ehz[0]['A'][(' ',2,' ')]['P']
atom64 = st_1ehz[0]['A'][(' ',64,' ')]['P']
atom12 = st_1ehz[0]['A'][(' ',12,' ')]['P']
atom20 = st_1ehz[0]['A'][(' ',20,' ')]['P']

print '1-72: ',atom72-atom1
print '1-2: ',atom2-atom1
print '12-20: ',atom20-atom12
print '1-64: ',atom64-atom1
print '20-72: ',atom72-atom20
print '2-12: ',atom2-atom12 
