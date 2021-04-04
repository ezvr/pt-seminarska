    
#%%
class Heatsink:
    
    def __init__(self, material, dimensions):
        self.material = material
        self.dimensions = dimensions
        self.presek = 15/1000 #m
        self.definePaths(dimensions)
    
    def definePaths(self, dimensions):
        from hilbertCurve import defineHilbertCurve 
        if dimensions == 2 or dimensions == 3 :
            self.paths = [defineHilbertCurve(iteracija, dimensions) for iteracija in range(1,7,1)]
        else:
            raise Exception('Dimenzije morajo biti 2 ali 3.')

    def drawPathGraphs(self):
        import matplotlib.pyplot as plt
        import os
        paths = [path[1] for path in self.paths]
        dir_path = os.path.dirname(os.path.realpath(__file__))

        try:
            os.mkdir(dir_path + f'/paths/{self.material}/')
        except OSError as error:
            print(error)   

        for index,tocke in enumerate(paths):

            #Priprava podatkov
            x, T_x = self.getGradients()[index]
            aQs = [self.Qs[index] for x in x]
            qMax = max(self.Qs)
            xQs = range(0, len(self.Qs))
            dolzine = [path[0]/50 for path in self.paths]
            
            # Zagon grafa
            plt.figure(figsize=(8,8))
 
            # Graf 1, skupni toplotni tok
            ax1 = plt.subplot(212)
            ax1.plot(dolzine,self.Qs, color="orange", label="Toplotni tok reber")
            ax1.plot(dolzine[index], self.Qs[index], 'bo', linewidth=4, label=f'Trenutni toplotni tok ({round(self.Qs[index],1)} W)')
            ax1.set(xlabel='Dolžina [m]', ylabel='Toplotni tok [W]')
            ax1.legend()

            # Graf 2, temperaturni gradient
            ax2 = plt.subplot(221)
            ax2.plot(x, T_x, label="Temperaturni gradient [°C]", color="green")
            ax2.set(xlabel='Dolžina [m]', ylabel='Temperatura[°C]')
            ax2.set_ylim([15,125])
            ax2.legend()

            # Graf 3, trenutni toplotni tok 
            #ax3 = ax2.twinx()
            #ax3.plot(x,aQs, color='red', label="Toplotni tok [W]")
            #ax3.set_ylim([0,qMax+qMax*0.2])
            #ax3.set(ylabel='Toplotni tok [W]',)
            # Graf 3 legend fix
            #lines, labels = ax2.get_legend_handles_labels()
            #lines2, labels2 = ax3.get_legend_handles_labels()
            #ax2.legend(lines + lines2, labels + labels2, loc=0)


            # Graf 4, oblika rebra 
            ax4 = plt.subplot(222)
            ax4.plot(tocke[0]/50, tocke[1]/50, linewidth=3, color="maroon", label=f'Dolžina rebra ({round(dolzine[index]*1000,1)} mm)')
            ax4.axes.get_yaxis().set_visible(False)
            ax4.axes.get_xaxis().set_visible(False)
            ax4.set_title('Oblika rebra')
            ax4.margins(0.2, 0.2)
            ax4.legend()

            # Print graf
            plt.tight_layout()
            plt.savefig(dir_path+f'/paths/{self.material}/path{index}.png')  # Shranimo v to mapo
            plt.close()
        
    def drawGradientGraphs(self):
        return null

    def calculateQs(self):
        from klasicnoRebro import izracunKlasicnegaRebra 
        self.Qs = [izracunKlasicnegaRebra(self.material, iteracijaPath[0]/50, self.presek) for iteracijaPath in self.paths]
    
    def calculateA(self):
        import numpy as np
        self.As = [ np.pi *iteracijaPath[0]/50 * self.presek for iteracijaPath in self.paths]

    def getLengths(self):
        return [iteracija[0]/50 for iteracija in self.paths]

    def getGradients(self):
        from temperaturniProfili import temperaturniProfil 
        return  [temperaturniProfil(self.material, iteracijaPath[0]/50, self.presek) for iteracijaPath in self.paths]


#y.show()
#%%
        

def calculate2Dpath(iteracij=2,material='PMMA'):
    # 2D PRIKAZ
    #Imports
    from hilbertCurve import defineHilbertCurve 
    import matplotlib.pyplot as plt
    from klasicnoRebro import izracunKlasicnegaRebra 

    # Define path
    dolzina, tocke, presek = defineHilbertCurve(iteracij,2)

    # Calculate Q

    presek = 1
    Q = izracunKlasicnegaRebra(material, dolzina/50, presek/1000) #mat, L, D

    # Plot path
    plt.plot(tocke[0], tocke[1], linewidth=7)
    #plt.plot([0,presek/1000],[-presek/1000,0])
    plt.show()

    import numpy as np
    print(f'Dolzina je {dolzina/50} m')
    print(f'Q je {Q}')
    print(f'presek je {presek/1000} m')
    print(f'Plašč je {np.pi * presek/1000 * dolzina/50}')
#%%

def calculate3Dpath(iteracij):
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

def doCalculationForSeries():
#%%
    #Imports
    from knjiznicaMaterialov import knjiznica 

    materials = list(knjiznica('all').keys())
    for material in materials:
        h = Heatsink(material,2)
        h.calculateQs()
        h.calculateA()
        h.drawPathGraphs()

# %%
