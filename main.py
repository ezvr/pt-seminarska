# MANJKA:
# KNJIŽNJICA MATERIALOV
# PROGRAM ZA KLASIČEN IZRAČUN REBRA
#
# https://github.com/galtay/hilbertcurve


#%%
def izrisKlasicnihReber():
    materiali = Q_f()[0]
    Q_f_materiali = Q_f()[1]

    round_to_tenths = [round(num,3) for num in Q_f_materiali]

    for i,num in enumerate(round_to_tenths):
        print(f'Q materiala: {materiali[i]} je {num}')

    # importing modules
    import matplotlib.pyplot as plt
    # izris rezultatov
    plt.bar(materiali, Q_f_materiali, color ='maroon', width = 0.4)

    plt.xlabel("Različni materiali")
    plt.ylabel("Prenos toplote [W]")
    plt.title("Prenos toplote v okolico skozi rebra")
    plt.show()

#%%
def Q_f():
    from klasicnoRebro import izracunKlasicnegaRebra 

    # definiranje materialov, ki nas zanimajo
    materiali = ['PMMA','ABS', 'aluminij', 'zelezo', 'baker']
    # izračun za vsak material
    Q_f_materiali = []
    for material in materiali:
        Q_f_materiali.append(izracunKlasicnegaRebra(material, 0.2, 0.005))
    return materiali, Q_f_materiali

#%%
izrisKlasicnihReber()

#%%
Q_f()

#%%
#def Primerjava():
Q_materiali = Q_f()[1]
Q_max = max(Q_materiali)

for 











# %%
