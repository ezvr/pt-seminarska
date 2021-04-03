    
def calculate2Dpath(iteracij=2,material):
    # 2D PRIKAZ
#%%
    iteracij=1
    material='baker'
    #Imports
    from hilbertCurve import defineHilbertCurve 
    import matplotlib.pyplot as plt
    from klasicnoRebro import izracunKlasicnegaRebra 

    # Define path
    dolzina, tocke, presek = defineHilbertCurve(iteracij,2)

    # Calculate Q
    Q = izracunKlasicnegaRebra(material, dolzina/1000, presek/1000) #mat, L, D

    # Plot path
    plt.plot(tocke[0], tocke[1])
    plt.show()

    print(f'Dolzina je {dolzina} mm')
    print(f'Q je {Q}')
#%%

def calculate3Dpath(iteracij=2):
#%%
    #Imports
    from hilbertCurve import defineHilbertCurve 
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Define path
    curve = defineHilbertCurve(iteracij,3)

    # Plot path
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(curve[1][0], curve[1][1],curve[1][2])
    plt.show()
    print(f'Dolzina je {curve[0]}')
    # %%

