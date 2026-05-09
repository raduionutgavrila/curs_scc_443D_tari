# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_finlanda as fin

TARI = {
    'finlanda': {
        'nume': 'Finlanda',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'finlanda': fin,
     #adauga 'tara_mea': prescurtare_tara_mea
}


