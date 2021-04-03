    
#%%
curve = defineHilbertCurve(2,2)
import matplotlib.pyplot as plt
plt.plot(curve[1][0], curve[1][1])
plt.show()
print(f'Dolzina je {curve[0]}')



# %%
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
curve = defineHilbertCurve(2,3)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(curve[1][0], curve[1][1],curve[1][2])
plt.show()
print(f'Dolzina je {curve[0]}')
# %%

