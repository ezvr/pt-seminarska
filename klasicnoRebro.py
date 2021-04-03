def izracunKlasicnegaRebra(material, nReber):
#%%
    from knjiznicaMaterialov import knjiznica 
    material = knjiznica('plastika')
#%%
    q = material['lambda'] + 2

#%%
    return q


# %%
