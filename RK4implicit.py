def RK4implicit(h,t,xvec,f): #not a finite difference so no step in y
    k1= h*f(t,xvec)
    k2=h*f(t+h/2, xvec+h*k1/2)
    k3=h*f(t+h/2,xvec+h*k2/2)
    k4=h*f(t+h,xvec+h*k3)
    return t+h, xvec+1/6.*(k1+ 2.*k2 + 2.*k3 + k4)
