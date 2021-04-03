def knjiznica(material):
    materiali = {
        'plastika': {
            'lambda' : 1, #j/kwK

        },
        'zelezo': {
            'lambda' : 1, #j/kwK
        }
    }

    if material in materiali:
        return(materiali[material])
    else:
        raise Exception('Sorry, material ne obstaja') 

