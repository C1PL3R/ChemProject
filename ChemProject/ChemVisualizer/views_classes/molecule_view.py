from django.shortcuts import render, redirect
from django.views import View
from core.models import Molecule

from rdkit import Chem
from rdkit.Chem import AllChem
import pubchempy as pcp

class MoleculeView(View):
    def get(request):
        name = request.COOKIES.get('moleculeName')
        smiles = request.COOKIES.get('moleculeSmiles')

        results = pcp.get_compounds(name, 'name')

        if results:
            compound = results[0]
            smiles = compound.isomeric_smiles
            molecular_formula = compound.molecular_formula
            molecular_weight = compound.molecular_weight
            exact_mass = compound.exact_mass
            iupac_name = compound.iupac_name
            aids = compound.aids if compound.aids else []
            sids = compound.sids if compound.sids else []   
            synonyms = compound.synonyms if compound.synonyms else []     

        mol = Chem.MolFromSmiles(smiles)
        mol = Chem.AddHs(mol)

        # Генеруємо 3D координати
        AllChem.EmbedMolecule(mol)
        block = Chem.MolToMolBlock(mol)

        try:
            if name and name.strip():
                created = Molecule.objects.get_or_create(smiles=smiles, defaults={'name': str(name).capitalize()})
        except Exception as e:
            print(f"Error creating molecule: {e}")

        try:
            context = {
                'mol_block': block, 
                'name': name,
                'molecular_formula': molecular_formula,
                'molecular_weight': molecular_weight,
                'exact_mass': exact_mass,
                'iupac_name': iupac_name,
                'aids': aids[0],
                'sids': sids[0],
                'synonyms': f"{synonyms[0]}, {synonyms[1]}, {synonyms[3]}",
            }
        except IndexError:
            context = {
                'mol_block': block, 
                'name': name,
                'molecular_formula': molecular_formula,
                'molecular_weight': molecular_weight,
                'exact_mass': exact_mass,
                'iupac_name': iupac_name,
                'synonyms': f"{synonyms[0]}, {synonyms[1]}, {synonyms[3]}",
                'aids': None,
                'sids': None,
            }

        response = render(request, 'ChemVisualizer/molecule.html', context)
        # response.delete_cookie('moleculeName', path='/')
        # response.delete_cookie('moleculeSmiles', path='/')
        return response
