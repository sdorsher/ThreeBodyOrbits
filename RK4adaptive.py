import RK4implicit
import numpy as np

def RK4adaptive(h,dtmax,dtmin,t,xvec,f,delta):
    t1,x1=RK4implicit.RK4implicit(h,t,xvec,f)
    t2,x2=RK4implicit.RK4implicit(2*h,t,xvec,f)
    #print((t2-t1)/h)
    diffx=x1-x2
    diffxxvals=diffx[0,:3]
    diffxsq=diffxxvals**2
    sumsq=np.sum(diffxsq)
    magdiff=np.sqrt(sumsq)
    #print(h)
    #print(diffxxvals)
    #print(diffxsq)
    #print(sumsq)
    #print(magdiff)
    rho=30*delta/magdiff #30*h*delta/magdiff
    repeat=False
    hnew=h
    epsilon=1e-10
    if np.abs(np.abs(rho)-1)<epsilon:
        repeat=False
    elif np.abs(rho)>1:
        repeat=False
        #print(rho, "False")
    elif np.abs(rho)<1:
        repeat=True
        #print(rho, "True")

    hnew*=rho**.25
    if hnew<dtmin+epsilon:
        repeat=False
        hnew=dtmin
    if hnew>=dtmax-epsilon:
        repeat=False
        hnew=dtmax
    hnew*=0.9
    tfinal = t1
    xfinal = x1
    if repeat:
        tfinal =t
        xfinal = xvec
    err = 1./30.*magdiff
    return repeat, hnew, h, tfinal, xfinal, rho,err
