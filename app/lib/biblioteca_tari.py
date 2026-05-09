# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_italia as ita

TARI = {
    'italia': {
        'nume': 'Italia',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'italia': ita,
     #adauga 'tara_mea': prescurtare_tara_mea
}
