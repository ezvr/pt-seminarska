def izracunKlasicnegaRebra():
#%%
    from knjiznicaMaterialov import knjiznica 
    material = knjiznica('aluminij')

#%%
    
#%%
    import numpy as np

    k = material['k']
    d = 5e-3 # m, premer rebra
    T_b = 110 # °C, temp. baze
    T_inf = 20 # °C, fluida
    A_cs = np.pi * d**2 / 4 # m^2, precni presek
    P = np.pi * d # m, obseg
    h_povp = 100 # W/m^2K, povprecna prestopnost
    L = 0.05 # m, dolžina 
    TH_b = T_b - T_inf # theta baze

    #izracun m
    m = np.sqrt((h_povp * P) / (k * A_cs))

    # izracun M
    M = TH_b * np.sqrt(h_povp * P * k * A_cs)

    Q_f = M * ((np.sinh(m*L) + (h_povp / m*k)*np.cosh(m*L)) / (np.cosh(m*L) + (h_povp / m*k)*np.sinh(m*L))) 
    
    print(Q_f, m, M)
#%%
    return Q_f


# %%
