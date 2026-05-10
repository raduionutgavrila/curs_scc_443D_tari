# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_belgia as belg
from app.lib import biblioteca_coreea as sk

TARI = {
    'belgia': {
        'nume': 'Belgia',
    },
    'coreea': {
        'nume': 'Coreea de Sud',
    }
from app.lib import biblioteca_canada as cana

TARI = {
    'canada': {
        'nume': 'Canada',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}


}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'coreea': sk
    'canada': cana,
    'belgia': belg,

}


