# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_statele_unite as sua

TARI = {
    'sua': {
        'nume': 'Statele Unite ale Americii',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'sua': sua,
     #adauga 'tara_mea': prescurtare_tara_mea
}


