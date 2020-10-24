import numpy as np

#checks symmetry of orbit with respect to r,v, and a

def howSymmetric(npstar1x,npstar2x,npstar1a,npstar2a):
    npstar1xf=npstar1x.flatten()
    npstar2xf=npstar2x.flatten()
    npstar1af=npstar1a.flatten()
    npstar2af=npstar2a.flatten()
    alloppositex=True
    alloppositea=True
    allcancelsx=1e-14
    allcancelsa=1e-14
    for i in  np.arange(len(npstar1xf)):
        subx=npstar1xf[i]+npstar2xf[i]
        if np.abs(npstar1xf[i])>1e-14:
            cancelsx=np.abs((subx)/npstar1xf[i])
            if cancelsx>allcancelsx:
                allcancelsx=cancelsx
    for i in  np.arange(len(npstar1af)):
        suba=npstar1af[i]+npstar2af[i]
        if np.abs(npstar1af[i])>1e-14:
            cancelsa=np.abs((suba)/npstar1af[i])
            if cancelsa>allcancelsa:
                allcancelsa=cancelsa
    return allcancelsx,allcancelsa
