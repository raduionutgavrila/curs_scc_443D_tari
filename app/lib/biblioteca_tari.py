# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_canada as cana

TARI = {
    'canada': {
        'nume': 'Canada',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'canada': cana,
     #adauga 'tara_mea': prescurtare_tara_mea
}


