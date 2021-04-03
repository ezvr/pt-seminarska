# https://github.com/galtay/hilbertcurve

#%%
def defineHilbertCurve():
    return null

#%%
def Extract(lst,index):
    return [item[index] for item in lst]
#%%
from hilbertcurve.hilbertcurve import HilbertCurve
# %%    
p=2; n=3
maxDist = 2**(p*n)
hilbert_curve = HilbertCurve(p, n)
distances = list(range(maxDist))
points = hilbert_curve.points_from_distances(distances)
x = Extract(points,0)
y = Extract(points,1)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

# %%
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
Axes3D.plot(xs, ys, *args, **kwargs)
# %%
