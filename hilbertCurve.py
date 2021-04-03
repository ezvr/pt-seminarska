# https://github.com/galtay/hilbertcurve
# pip install hilbertcurve

def defineHilbertCurve(iteracij, dimenzij):
    # Imports
    from hilbertcurve.hilbertcurve import HilbertCurve
    import numpy as np
    # Helper function
    def Extract(lst,index):
        return [item[index] for item in lst]

    # Make the HilberCurve
    p=iteracij; n=dimenzij
    maxDist = 2**(p*n)
    hilbert_curve = HilbertCurve(p, n)
    distances = list(range(maxDist))
    points = hilbert_curve.points_from_distances(distances)

    delitev = 2**iteracij-1 # število delitev na osi
   # Determine points for graphing
    graphPoints = []
    for i in range(n):
        graphPoints.append(np.array(Extract(points,i)) / delitev)

    # Determine presek
    presek = 1/(delitev*4)

    # Vrni dolžino rebra, presek rebra, in točke za izris
    return (maxDist-1)/delitev, graphPoints, presek


