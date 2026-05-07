# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_estonia as esto

TARI = {
    'estonia': {
        'nume': 'Estonia',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'estonia': esto,
     #adauga 'tara_mea': prescurtare_tara_mea
}


