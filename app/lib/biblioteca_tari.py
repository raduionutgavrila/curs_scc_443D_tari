# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_franta as franta

TARI = {
    'franta': {
        'nume': 'Republica Franceza',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'franta': franta,
     #adauga 'tara_mea': prescurtare_tara_mea
}


