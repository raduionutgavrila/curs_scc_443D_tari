# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_china as china

TARI = {
    'China': {
        'nume': 'China',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'China': china,
     #adauga 'tara_mea': prescurtare_tara_mea
}
