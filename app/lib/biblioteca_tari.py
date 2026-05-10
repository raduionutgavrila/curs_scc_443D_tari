# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 

from app.lib import biblioteca_belgia as belg
from app.lib import biblioteca_coreea as sk
from app.lib import biblioteca_norvegia as nvg
from app.lib import biblioteca_romania as rou


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
    'romania': {
        'nume': 'România',
    }
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}


}


BIBLIOTECI = {

    'belgia': belg,
    'coreea': sk,
    'norvegia': nvg,
    'romania': rou,
     #adauga 'tara_mea': prescurtare_tara_mea
}


