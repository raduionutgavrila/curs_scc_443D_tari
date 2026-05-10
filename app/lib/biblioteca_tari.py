# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea
from app.lib import biblioteca_danemarca as dan

TARI = {
    'danemarca': {
        'nume': 'Danemarca',
    }

}

# Mapare tara -> biblioteca

BIBLIOTECI = {
    'danemarca': dan
}
