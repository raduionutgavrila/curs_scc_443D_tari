# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_japonia as jp

TARI = {
    "japonia": {
        "nume": "Japonia",
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    "japonia": jp,
     #adauga 'tara_mea': prescurtare_tara_mea
}


