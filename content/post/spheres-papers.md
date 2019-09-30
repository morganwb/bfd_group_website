+++
date = "2019-09-29T15:01:00Z"
title = "Papers published!"
[[authors]]
    name = "Jeffrey S. Oishi"
    is_member = true
    link = "/jeff_oishi"

+++

I'm excited to annouce that our two papers on spin-weighted spherical harmonics are finally published in the Journal of Computational Physics X. The [first paper](https://doi.org/10.1016/j.jcpx.2019.100013) covers the mathematical formalism, while the [second paper](https://doi.org/10.1016/j.jcpx.2019.100012) demonstrates its performance in a number of test problems, including a fully convective, rotating dynamo problem:

![spherical dynamo](/img/1-s2.0-S2590055219300289-gr010.jpg)

On the right is the radial velocity while the left shows magnetic field lines, visualized using Vapor.

The most significant part of this research, aside from the fact that we have sparse, efficient spectrally accurate spherical basis functions in Dedalus, is that by using spin-weighted spherical harmonics, one can implement equations on the sphere directly in vector form:

![equations](/img/2019-09-29-204108_1325x457_scrot.png)

Previously, one would have to write equations in poloidal-toridal form in order to expand them in spherical harmonics. By constructing spectrally accurate solutions for vector partial differential equations on the sphere, we can now get ready for a lot of exciting research on the sphere!
