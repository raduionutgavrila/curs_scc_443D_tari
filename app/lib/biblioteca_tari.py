# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_namibia as namb
TARI = {
    'namibia': {
        'nume': 'Namibia',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'namibia': namb,
     #adauga 'tara_mea': prescurtare_tara_mea
}


