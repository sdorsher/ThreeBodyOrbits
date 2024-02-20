# KeplerianOrbits
I would like to highlight 

EsplitEL vs t convergence plot.ipynb

which demonstrates that energy is transferred between the outer planet and the inner binary and back again, and that this is not an artifact of the error introduced by the numerical integration scheme, since neither the behavior nor the amplitude of the energy transfer depends on step size of the numerical integration

Data is fed to this analysis routine by a previous piece of code, 

TwoStarsOnePlanet_convergenceTest-ELpvst.ipynb


which also contains some analysis. It is important to use the version with the "p" for momentum because I caught an error between the 

TwoStarsOnePlanet_Esplit.ipynb with
TwoStarsOnePlanet_convergence.ipynb data

and the more recent correct version

However, if you would like to see my thought process with some ultimately inaccurate results, it displays nicely in the 

TwoStarsOnePlanet_Esplit.ipynb version






Two Stars One Planet.ipynb

has a nice plot of the three body orbit, where the center two stars spiral about the slighly offset center of mass and the outer planet travels roughly in an ellipse but seems to spiral somewhat

So what else is here?

I began by writing the code simplistically with just two stars and no generalization using the most basic RK4. I tested circles, unequal masses, ellipses, hyperbolas. I checked the numerical convergence of my code. I explored recovery of initial parameters (a couple percent) using fits to the ellipse. I confirmed symmetry and minima and maxima. These routines seem to work but unfortunately I left many of the parameters set oddly when I moved on. 

I added generalizations to many bodies in the integration (vector) or 3 bodies in the analysis. I added an adaptive RK4 which I discarded because it was more helpful to be able to do convergence analyses. 

I added initial conditions for a three body orbit with a planet distantly located from an equal mass binary star on a quasi-circular orbit. I did not try to account for the planets effect on the center of mass. The orbit evolved as described above. Linear momentum was conserved. 

If I were to continue to improve upon this I would:

1) generalize the analysis pipeline so that analysis was not specific to two or three stars. More general visualizations, metrics, or even i/o would be necessary.

2) actually set G=6.67e-11 instead of 1. I have always been aware that 1 is physically inappropriate but it was a simple way to begin and I was lazy about reading very small/large numbers

3) try to speed up computational time?
4) clean this archive up omg
5) extend to many bodies
