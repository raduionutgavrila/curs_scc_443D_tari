# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_brazilia as braz

TARI = {
    'brazilia': {
        'nume': 'Brazilia',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'brazilia': braz,
     #adauga 'tara_mea': prescurtare_tara_mea
}


