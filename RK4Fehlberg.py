def RK4implicit(h,t,xvec,f): #not a finite difference so no step in y
    k1= h*f(t,xvec)
    k2=h*f(t+h/4, xvec+k1/4)
    k3=h*f(t+3.*h/8,xvec+3.*k1/32+k2*9./32)
    k4=h*f(t+12.*h/13,xvec+1932.*k1/2197-7200.*k1/2197+7297.*k3/2197)
    k5=h*f(t+h, xvec+439./216.*k1-8.*k2+3680./513.*k3-845./4104*k4)
    k6=h*f(t+h/2.,xvec-8./27*k1+2.*k2-3544./2565.*k3+1859./4104*k4-11/40.*k5)
    result4 = xvec+16./135*k1+6656./128525.*k3+28561./56430*k4-9/50.*k5+2/55.*k6
    result5= xvec+25./216*k1+1408./2565*k3+2197./4104*k4-1./5*k5
    err = result5-result4
    return t+h, result4, result5, err
