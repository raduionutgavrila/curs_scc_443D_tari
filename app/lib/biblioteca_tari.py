# Configuratie globala a proiectului

<<<<<<< HEAD
=======
#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
>>>>>>> 848735f0f1b7498f6758c47340b11e07e2b9e2b3


from app.lib import biblioteca_belgia as belg
from app.lib import biblioteca_coreea as sk
from app.lib import biblioteca_norvegia as nvg
from app.lib import biblioteca_romania as rou
from app.lib import biblioteca_brazilia as braz
from app.lib import biblioteca_japonia as jp
from app.lib import biblioteca_germania as germ
from app.lib import biblioteca_italia as ita
from app.lib import biblioteca_statele_unite as sua
from app.lib import biblioteca_estonia as esto
from app.lib import biblioteca_franta as franta
from app.lib import biblioteca_finlanda as fin
from app.lib import biblioteca_irlanda as irlanda


TARI = {
    'norvegia': {
        'nume': 'Norvegia',
    },
    'coreea': {
        'nume': 'Coreea de Sud',
    },

    'belgia': {
        'nume': 'Belgia',
    },

    'brazilia': {
        'nume': 'Brazilia',
    },
    

    "japonia": {
        "nume": "Japonia",
    },
        
    'italia': {
        'nume': 'Italia',
    },

    'sua': {
        'nume': 'Statele Unite ale Americii',

    'estonia': {
        'nume': 'Estonia',
    },
        
    'franta': {
        'nume': 'Republica Franceza',
    },
        
    # Mapare tara -> biblioteca
    'finlanda': {
        'nume': 'Finlanda',
    },
    'irlanda': {
        'nume': 'Irlanda',
    }

    





BIBLIOTECI = {
    'belgia': belg,
    'coreea': sk,
    'norvegia': nvg,
    'romania': rou,
    'brazilia': braz,
    "japonia": jp,
    'italia': ita,
    'germania': germ,
    'sua': sua,
    'estonia': esto,
    'franta': franta,
    'finlanda': fin,
    'irlanda': irlanda,
}



