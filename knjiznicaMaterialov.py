def knjiznica(material):
    materiali = {
        'PMMA': {
            'lambda': 0.193,  # W/mK
            'cp': 1450,  # J/kgK


        },
        'ABS': {
            'lambda': 0.24,  # W/mK
            'cp': 1675,  # J/kgK
        },
        'aluminij': {
            'lambda': 240,  # W/mK
            'cp': 910,  # J/kgK
        },
        'zelezo': {
            'lambda': 65,  # W/mK
            'cp': 450,  # J/kgK
        },
        'baker': {
            'lambda': 392,  # W/mK
            'cp': 390,  # J/kgK
        }
    }

    if material in materiali:
        return(materiali[material])
    else:
        raise Exception('Sorry, material ne obstaja')
