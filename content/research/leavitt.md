+++ 
title="Using Leavitt" 
date = "2018-11-22" 

[[authors]] 
name = "Jeff Oishi" 
is_member = true 
link = "/jeff_oishi" 
+++
# Basics

When you log in to leavitt via `ssh`, you will be on the "head node". This node is identical to the other nodes. It has 28 cores and 128 GB of memory. This machine is for doing small analysis tasks and submitting jobs. **DO NOT RUN DEDALUS ON THE HEAD NODE**. Instead, use a job script to submit runs to the compute nodes.

# Modules System
Leavitt uses modules to manage various software packages. A quick intro to using modules on Leavitt is on the main [Leavitt documentation page](https://www.bates.edu/research-resources/leavitt-hpc-cluster/running-jobs/) You should add 

```
module load slurm intel-mpi hdf5 ffmpeg

export PATH=$PATH:/home/joishi/build/bin

# PNG encoding with ffmpeg
# Example use: png2mp4 “frames/*" frames.mp4 30

# Options:
#   -y                  Overwrite output
#   -f image2pipe       Input format
#   -vcodec png         Input codec
#   -r $3               Frame rate
#   -i -                Input files from cat command
#   -f mp4              Output format
#   -vcodec libx264     Output codec
#   -pix_fmt yuv420p    Output pixel format
#   -preset slower      Prefer slower encoding / better results
#   -crf 20             Constant rate factor (lower for better quality)
#   -vf "scale..."      Round to even size
#   $2                  Output file
function png2mp4(){
    cat $1 | ffmpeg \
        -y \
        -f image2pipe \
        -vcodec png \
        -r $3 \
        -i - \
        -f mp4 \
        -vcodec libx264 \
        -pix_fmt yuv420p \
        -preset slower \
        -crf 20 \
        -vf "scale=trunc(in_w/2)*2:trunc(in_h/2)*2" \
        $2
}
```

to your `.bashrc` file. The `export PATH=` line you only need if you want to use software I've installed. You don't need it if we haven't talked about it. The last part gives you a little function called `png2mp4` which you can use to make movies from the `.png` frames we make with our visualization scripts. The example usage is right up there in the comments.

# Sample Dedalus Run Script
Run scripts are lists of commands to run on the nodes with some metadata stored in comments at the top of the file. These scripts are done using In order to run a job, you submit a script to a queue, by doing 

```
$ sbatch run_growth_11.sh
```

where `run_growth_11.sh` is a bash script that contains this:


```
#!/usr/bin/bash
#SBATCH --partition=defq
#SBATCH --time=5-0
#SBATCH --nodes=3

conda activate dedalus

date
mpirun -np 64 python3 bioflow.py runs/growth_11.cfg
date
```

All of the lines at the top starting with `#SBATCH` are commands to SLURM. The first, `--partition=defq`, sets the partition, which is the queue you are submitting your job. Each partition has certain time limits and numbers of nodes you can submit to. You may not be able to use all of the partitions. The default, called `defq`, allows you to run on up to 15 nodes (at the moment; there are actually 17 nodes but as of today, two are down) for up to 5 days. If this isn't enough time, email me. If this isn't enough nodes, we'll have to move to bigger compute resources. 

You can see all the partitions by running `sinfo`.

```
$ sinfo
PARTITION   AVAIL  TIMELIMIT  NODES  STATE NODELIST
defq*          up 5-00:00:00     15   idle node[001-007,009-016]
contributor    up   infinite     15   idle node[001-007,009-016]
faculty        up 15-00:00:0     15   idle node[001-007,009-016]
phi            up   infinite      1  down* node017
```

The next SLURM command, `--time=5-0`, says this will run for five days, zero hours. The [SLURM manual](https://slurm.schedmd.com/sbatch.html) gives the following date formats you can use:

> Acceptable time formats include "minutes", "minutes:seconds", "hours:minutes:seconds", "days-hours", "days-hours:minutes" and "days-hours:minutes:seconds".

Finally, there's the number of nodes, `--nodes=3`. Each node on Leavitt currently has 28 cores. **You are responsible for making sure the number of cores you want is less than 28 times this number** 

After the comments at the top, the batch script is just a regular bash script with a list of commands. You should always use the `source /home/joishi/build/dedalus_intel_mpi/bin/activate` as is, unless you have your own install of Dedalus on Leavitt. This activates the Dedalus environment. 

The last 3 commands are the `mpirun` sandwiched in between two calls to date. This just allows us to get a quick feel for how long the code ran. `mpirun` is the command that launches Dedalus on `-np X` number of cores. `X` here is 64, and 64/28 ~ 2.3, which is greater than 2, so we need 3 nodes. 
