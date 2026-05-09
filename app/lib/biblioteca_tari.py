# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
<<<<<<< HEAD
from app.lib import biblioteca_coreea as sk

TARI = {
    'coreea': {
        'nume': 'Coreea de Sud',
    }
=======
from app.lib import biblioteca_canada as cana

TARI = {
    'canada': {
        'nume': 'Canada',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}
>>>>>>> origin/dev_roseanu_vlad

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
<<<<<<< HEAD
    'coreea': sk
=======
    'canada': cana,
     #adauga 'tara_mea': prescurtare_tara_mea
>>>>>>> origin/dev_roseanu_vlad
}


