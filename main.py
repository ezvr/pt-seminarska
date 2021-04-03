# MANJKA:
# KNJIŽNJICA MATERIALOV
# PROGRAM ZA KLASIČEN IZRAČUN REBRA
#
# https://github.com/galtay/hilbertcurve


#%%
def izrisKlasicnihReber():
#%%     
    # importing modules
    import matplotlib.pyplot as plt
    from klasicnoRebro import izracunKlasicnegaRebra 
    
    # definiranje materialov, ki nas zanimajo
    materiali = ['PMMA','ABS', 'aluminij', 'zelezo', 'baker']
    # izračun za vsak material
    Q_f_materiali = []
    for material in materiali:
        Q_f_materiali.append(izracunKlasicnegaRebra(material))
#%%
    # izris rezultatov
    plt.bar(materiali, Q_f_materiali, color ='maroon', width = 0.4)

    plt.xlabel("Različni materiali")
    plt.ylabel("Prenos toplote")
    plt.title("Prenos toplote v okolico skozi rebra")
    plt.show()



#%%
izrisKlasicnihReber()





# %%
