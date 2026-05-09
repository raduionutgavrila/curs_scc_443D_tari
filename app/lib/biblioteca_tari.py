# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_norvegia as nvg

TARI = {
    'norvegia': {
        'nume': 'Norvegia',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'norvegia': nvg,
     #adauga 'tara_mea': prescurtare_tara_mea
}


