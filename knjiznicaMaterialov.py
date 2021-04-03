def knjiznica(material):
    materiali = {
        'plastika': {
            'lambda' : 1, #W/mK
            'cp' : 1, #J/kgK
            

        },
        'zelezo': {
            'lambda' : 1, #W/mK
            'cp' : 1, #J/kgK
        }

        ,
        'zelezo': {
            'lambda' : 1, #W/mK
            'cp' : 1, #J/kgK
        }
    }

    if material in materiali:
        return(materiali[material])
    else:
        raise Exception('Sorry, material ne obstaja') 

