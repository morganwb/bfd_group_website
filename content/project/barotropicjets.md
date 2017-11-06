+++
date = "2017-10-29T16:10:22+02:00"
description = ""
external_link = ""
image = ""
project_id = ""
short_description = ""
title = "Barotropic Jet Formation on the 2-Sphere using Spin Spherical Harmonics"
[[participants]]
    name = "Jeff Oishi"
    id = "jsoishi"
    is_member = true
[[participants]]
    name = "Matt Goldberg"
    id = "mgoldbe2"
    is_member = true
+++

## Motivation

The [Dedalus Collaboration](http://dedalus-project.org) is developing a sparse discretization of vector fields in spherical geometry. Key to this process is the understanding that vector components, as opposed to scalars, do not have the same regularities as the standard spherical harmonics. However, by using a basis that *does* have the right regularity, we can construct a sparse matrix solution to differential equations in curvilinear geometries. This basis is the *spin-weighted* spherical harmonics, constructed from Jacobi polynomials. 

We are interested in testing and optimizing the implementation of spin spherical Barotropic Jet formation is a well-studied process in atmospheric dynamics.

