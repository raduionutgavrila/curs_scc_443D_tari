# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_romania as rou

TARI = {
    'romania': {
        'nume': 'România',
    }
}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'romania': rou,
     #adauga 'tara_mea': prescurtare_tara_mea
}


