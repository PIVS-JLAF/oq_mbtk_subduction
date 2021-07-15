import numpy

def write_mesh(smsh, key):
    edges_fname = './tmp/{:s}_edges.xyz'.format(key)
    fou = open(edges_fname, 'w')
    fou.write('>\n')
    for e in smsh:
        for i in numpy.nonzero(numpy.isfinite(e[:,2]))[0]:
            fou.write('{:.5f},{:.5f},{:.5f}\n'.format(e[i,0], e[i,1], e[i,2]))
        fou.write('>\n')
    fou.close()

    profiles_fname = './tmp/{:s}_profiles.xyz'.format(key)
    fou = open(profiles_fname, 'w')
    fou.write('>\n')
    last = -1
    cont = False
    for i in range(len(smsh[0])):
        fou.write('>\n')
        for e in smsh:   
            if numpy.all(numpy.isfinite(e[i])):
                fou.write('{:.5f},{:.5f},{:.5f}\n'.format(e[i,0], e[i,1], e[i,2]))
    fou.write('>\n')
    fou.close()
    return edges_fname, profiles_fname

def write_poly(smsh, key):
    poly_fname = './tmp/{:s}_poly.xyz'.format(key)
    fou = open(poly_fname, 'w')
    fou.write('>\n')
    for i1 in range(len(smsh)-1):
        for i2 in range(len(smsh[0])-1):
            if (numpy.all(numpy.isfinite(smsh[i1][i2,:])) and 
                numpy.all(numpy.isfinite(smsh[i1][i2+1,:])) and
                numpy.all(numpy.isfinite(smsh[i1+1][i2,:])) and
                numpy.all(numpy.isfinite(smsh[i1+1][i2+1,:]))):
                e = smsh[i1]
                f = smsh[i1+1]
                fou.write('{:.5f},{:.5f},{:.5f}\n'.format(e[i2,0], e[i2,1], e[i2,2]))
                fou.write('{:.5f},{:.5f},{:.5f}\n'.format(f[i2,0], f[i2,1], f[i2,2]))
                fou.write('{:.5f},{:.5f},{:.5f}\n'.format(f[i2+1,0], f[i2+1,1], f[i2+1,2]))
                fou.write('{:.5f},{:.5f},{:.5f}\n'.format(e[i2+1,0], e[i2+1,1], e[i2+1,2]))
                fou.write('{:.5f},{:.5f},{:.5f}\n'.format(e[i2,0], e[i2,1], e[i2,2]))
                fou.write('>\n')
    fou.close()
    return poly_fname