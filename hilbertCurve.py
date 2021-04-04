# https://github.com/galtay/hilbertcurve
# pip install hilbertcurve

def defineHilbertCurve(iteracij, dimenzij):
    # Imports
    from hilbertcurve.hilbertcurve import HilbertCurve
    import numpy as np

    # Edge case: if iteracij = 1, straight line
    if iteracij == 1:
        import numpy as np
        b = np.ones(dimenzij)
        a = np.zeros_like(b)
        dist = np.linalg.norm(a-b)
        c = np.column_stack((a,b))
        return dist, c, 0.5
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
    presek = 1/(delitev*2)

    # Vrni dolžino rebra, presek rebra, in točke za izris
    return (maxDist-1)/delitev, graphPoints, presek


