def knjiznica(material):
    materiali = {
        'PMMA': {
            'k': 0.193,  # W/mK
            'cp': 1450,  # J/kgK


        },
        'ABS': {
            'k': 0.24,  # W/mK
            'cp': 1675,  # J/kgK
        },
        'aluminij': {
            'k': 240,  # W/mK
            'cp': 910,  # J/kgK
        },
        'zelezo': {
            'k': 65,  # W/mK
            'cp': 450,  # J/kgK
        },
        'baker': {
            'k': 392,  # W/mK
            'cp': 390,  # J/kgK
        }
    }

    if material in materiali:
        return(materiali[material])
    else:
        raise Exception('Sorry, material ne obstaja')
