+++ 
title="Guide to Getting Started " 
date = "2018-11-22"

[[authors]] 
name = "Jeff Oishi" 
is_member = true 
link = "/jeff_oishi" 
+++

Welcome to the Bates Fluid Dynamics Group! Most of our work involves solving partial differential equations by computer. Typically, this means running simulations on supercomputers, most often the Leavitt cluster here at Bates.

# Using Linux  #

All of the group's software runs on Linux. You need to be familiar with the command line, and it helps to know a bit of bash shell scripting. We use the `git` version control system. Nearly all of our code, including our main simulation workhorse, [Dedalus](http://dedalus-project.org/), is written in Python. 

For writing theses, papers, and notes, we use the LaTeX typesetting system. 

All of this is taught in PHYS s10, but if you haven't taken it, don't fear! Here are some resources.

* [Intro to command line](https://snugug.github.io/Intro-Command-Line)
* [wikipedia](https://en.wikipedia.org/wiki/Template:Unix_commands) command line programs list. I still make reference to this on a regular basis.
* [Resources to learn git](https://try.github.io/)
* [The official python tutorial](https://docs.python.org/3/tutorial/index.html). If you're starting from zero programming, come see me first. If you know enough to be dangerous in another language, this is a good startingplace.
* [Getting Started with LaTeX](https://faculty.math.illinois.edu/~hildebr/tex/latex-start.html). This is a pretty comprehensive resource. 
* [Creating ssh keys](https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html) ssh keys are essential to secure access to many of the group's resource. They also allow you to do awesome stuff like caching your password so you don't have to type it everytime you want to access remote data on Leavitt.
* [sshfs tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh) Once you have an ssh key, you can use sshfs to "mount" your directory on Leavitt like it's a local disk on your Mac, Windows, or Linux laptop. Then you can edit scripts using whatever text editor you're most comfortable with.

You'll be doing a lot of text editing. This is like word processing, but without formatting. It's really important to get familiar with a text editor. There are many, and I'd ask around to see what your friends are using. Here's a few.

* [emacs](https://www.gnu.org/software/emacs/) the greatest editor ever. Also, somewhat hard to use. 
* [atom](https://atom.io/) has a lot of buzz. It seems pretty cool, is free and open-source. 
* [sublime text](https://www.sublimetext.com/) A widely used and much liked editor. It is proprietary and costs money, so I don't fully recommend it.

# Dedalus #

* [Dedalus Users Group](https://groups.google.com/dedalus-users/). 
A great place to start. Search the questions first! Often your question has already been answered. If you don't find an answer, send a message. There's over a hundred Dedalus users reading and mailing that list, so chances are someone will know the answer. 
* [Dedalus Tutorial Notebooks](https://dedalus-project.readthedocs.io/en/latest/getting_started.html#tutorial-notebooks) These tutorials go over the basics of how Dedalus works from the ground up.

# Local Bates Computing Resources #

* [Leavitt]( {{< ref "leavitt.md" >}} ) is our 476 core, 17 node compute cluster. Managed by the Bates High Performance Computing Center, it's where we do most of our smaller runs.
* `a23637.bates.edu` is our group workstation. It's available via ssh from on campus, and has 256 GB of memory for big data analysis and small runs. If you need an account on it, just ask Jeff.

# Fluid Dynamics #

I'll fill this section out over time, but for now, here are a few resources I've made use of in the past. 

## General Overviews ##
The first three are all available from the Bates Library for free as pdfs. 

* [An Introduction to Fluid Dynamics](http://cbbcat.net/record=b5188293), G. K. Batchelor. This is probably the most classic fluid dynamics textbook in English. It's not easy going, but well worth the effort.
* [Fluid Mechanics](http://farside.ph.utexas.edu/teaching/336L/Fluidhtml/Fluidhtml.html), a free textbook by University of Texas, Austin physics professor Richard Fitzpatrick.
* [Fluid Dynamics for Physicists](http://cbbcat.net/record=b5185188~S19), T. E. Faber. The first chapter of this book does a very nice job of covering the flavor.
* [FYFD](https://fyfluiddynamics.com/) will give you tons of inspiration!
* [Physical Fluid Dynamics](http://cbbcat.net/record=b1816114~S19), D. J. Tritton. This is only available in print at the Bates library. This was one of my favorites when I was a student.

## Instability ##
Understanding how fluid flows become unstable is a key part of our work.  Here are a few references on instability.

* The [National Committee for Fluid Mechanics Films on Flow Instability](https://youtu.be/yutbmcO5g2o) is a good place to start. It lays out what an instability is with several experimental examples. 
* Prof. V. Shankar's "Introduction to Hydordynamic Stability" course ([lecture notes](http://home.iitk.ac.in/~vshankar/files/VShankar_Stability_Intro.pdf), [video](https://www.youtube.com/watch?v=2BafIxhj3F0)) is a good overview.
* [An Introduction to Hydrodynamic Stability](https://cbbcat.net/record=b5188328~S19), P.G. Drazin. This is a very good book to get started with, though it presumes a bit of hydrodynamic knowledge. It is available as a PDF to download from the Bates Library.


# Learning MPI #

Dedalus is parallelized using the message passing interface (MPI) via the mpi4py python library. Here are a few resources on learning MPI

* [MPI tutorial](http://mpitutorial.com/) This is a very thorough introduction to MPI using C. 
* [Parallel Programming with MPI using Python and mpi4py](https://www.youtube.com/playlist?list=PL06051AE8DCFAF4F9) by Jeremy Bejarano. A video series teaching basic MPI concepts using mpi4py.

