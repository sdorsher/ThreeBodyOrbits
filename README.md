# KeplerianOrbits
I would like to highlight 

EsplitEL vs t convergence plot.ipynb

which demonstrates that energy is transferred between the outer planet and the inner binary and back again, and that this is not an artifact of the error introduced by the numerical integration scheme, since neither the behavior nor the amplitude of the energy transfer depends on step size of the numerical integration

Data is fed to this analysis routine by a previous piece of code




Two Stars One Planet.ipynb

has a nice plot of the three body orbit, where the center two stars spiral about the slighly offset center of mass and the outer planet travels roughly in an ellipse but seems to spiral somewhat


If I were to continue to improve upon this I would:

1) generalize the analysis pipeline so that analysis was not specific to two or three stars. More general visualizations, metrics, or even i/o would be necessary.

2) actually set G=6.67e-11 instead of 1. I have always been aware that 1 is physically inappropriate but it was a simple way to begin and I was lazy about reading very small/large numbers

3) try to speed up computational time?
4) clean this archive up omg
5) extend to many bodies
