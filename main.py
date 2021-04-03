# MANJKA:
# KNJIŽNJICA MATERIALOV
# PROGRAM ZA KLASIČEN IZRAČUN REBRA
#
# https://github.com/galtay/hilbertcurve


#%%
def izrisKlasicnihReber():
    # importing modules
    import matplotlib.pyplot as plt
    from klasicnoRebro import izracunKlasicnegaRebra 

    # definiranje materialov, ki nas zanimajo
    materiali = ['plastika','zelezo']
    
    # izračun za vsak material
    q_materiali = []
    for material in materiali:
        q_materiali.append(izracunKlasicnegaRebra('plastika'))

    # izris rezultatov
    plt.bar(materiali, q_materiali, color ='maroon', width = 0.4)
 
    plt.xlabel("Različni materiali")
    plt.ylabel("Prenos toplote")
    plt.title("Prenos toplote v okolico skozi rebra")
    plt.show()



#%%
izrisKlasicnihReber()





# %%
