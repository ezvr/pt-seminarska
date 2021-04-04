#%%
#importing shit
def temperaturniProfil(material, L=0.02,d=0.005,):
    import numpy as np
    from knjiznicaMaterialov import knjiznica 
    
    material = knjiznica(material)
    k = material['k']
    T_b = 110 # °C, temp. baze
    T_inf = 20 # °C, fluida
    #L = 0.02 # m, SAMO TEST 
    #d = 0.005 #SAMO ZA TEST
    A_cs = (np.pi * d**2) / 4 # m^2, precni presek
    P = np.pi * d # m, obseg
    h_povp = 100 # W/m^2K, povprecna prestopnost


    m = np.sqrt((h_povp * P) / (k * A_cs))
    x = np.linspace(0, L, num=500)

    T_x = T_inf + (((np.cosh(m * (L-x)) + (h_povp / (m*k)) * np.sinh(m * (L-x))) / (np.cosh(m * L) + (h_povp / (m*k)) * np.sinh(m * L)))) * (T_b - T_inf)
    return x, T_x



# %%
import os
import matplotlib.pyplot as plt
material = 'ABS'
L = 0.02
x, T_x = temperaturniProfil(material, L)
# izris rezultatov
plt.plot(x, T_x, color ='maroon')

plt.xlabel("Dolžina [m]")
plt.ylabel("Temperatura [°C]")
plt.title("Temperaturni profil")
plt.axis([0, L, 0, 120])

dir_path = os.path.dirname(os.path.realpath(__file__))
plt.savefig(dir_path+'/fig1.png')  # Shranimo v to mapo
# %%
