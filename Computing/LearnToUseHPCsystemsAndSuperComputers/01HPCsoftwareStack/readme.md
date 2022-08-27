# Access to HPCs

To access the HPC systems at your institution, you generally need an account which your HPC authority would create for you.

## Accessing HPC systems on campus

Linux: To connect to the HPC from a Linux based computer, open a terminal window and simply type ssh hpc-login-node-name and then press enter.

```bash
ssh username@login-hostname
```

## HPC Login Demo

https://www.youtube.com/watch?v=llsufECHqfg&feature=emb_title

# Data Transfer

On HPC systems, we can interact with the command line over SSH. We can also create and move file and directories. We can run a program and get some output. But the question is how can we

* Upload files, say our datasets, to the HPC machine?

* Download files, say the results of our analysis, from the HPC machine for further analysis locally?

There are two popular methods to do these:

* FTP = File Transfer Protocol; and

* SCP = Secure Copy

## FTP file transfer

You need an FTP client, such as FileZilla. You tell the client which server to connect to e.g,: [hpc.yourinstitution.edu](http://hpc.yourinstitution.edu/) and port: 22. You then authenticate with your username and password. Note that All FTP communication to the HPC machine will be 100% secure.

# HPC software list

Your institute may have a different list of software, but following are commonly available software that should be readily available on any HPC systems and may loaded through software modules (see the next section). The commercial software are noted with a ©:

## Programming Language Compilers

* GNU compilers (gnu-c, gnu-cpp ForTran, etc.)

* JDK (java)

* Intel compilers (c++, ForTran, etc.) ©

* SolarisStudio

## Scripting

* Guile

* Perl

* Python

* Tcl/Tk

* Bash

* Zsh

## File Formats and Data Management

* HDF

* netCDF

## Astronomy and Astrophysics

* IDL ©
* Tecplot ©
* DS9
* IRAF
* Figaro
* Rebound

## CFD & Engineering and Modelling

* COMSOL ©
* ANSYS Fluent software ©
* APSIM
* Cantera
* Converge CFG
* Eilmer


## Climate Modelling

* GMT
* Opengrads

## Mathematics and Statistics

* Matlab ©
* R and RStudio
* Scilab
* Numpy
* Scipy

## Graphics

* Ferret
* Gnuplot
* Paraview
* Atlas
* NCL
* Wine
* NetworkX
* Gephi
* yED

## Editors

* Vim
* EMACS
* Atom

## Parallel Programming Libraries/Tools

* Intel MPI ©
* Open MPI
* MPICH
* CUDA Toolkit

## Schedulers (any one)

* PBS
* PBS Pro
* Slurm

## Utils

* SFTP
* SSH
* sZip

Note that a commercially purchased software may be controlled by their license keys that can either limit the number of concurrent users or the toolboxes/modules available for use (e.g., Matlab toolbox). Please contact your institutions HPC authority for further information regarding the availability of a specific software of your need.

# HPC software modules

On a HPC system, the user environment is setup using `environment` modules. By default, a number of `modules` are automatically loaded to configure the environment to allow running of applications and the submission of jobs to the cluster.

https://www.youtube.com/watch?v=sDuPTndkj7U&feature=emb_title

## What is an environment Module?

On a HPC system, it is necessary to make available a wide choice of software packages in multiple versions, it can be quite difficult to set up the user environment so as to always find the required executables and libraries.

This is particularly true where different implementations or versions use the same names for files. Environment modules provide a way to selectively activate and deactivate modifications to the user environment which allow particular packages and versions to be found.

## Using modules in batch files

To use software package xxx in a batch job script it is a simple matter of specifying module load xxx See the appropriate packages entry in the software page (and the output of the module list) for details of the expected package name for this flag.

## Creating your own modules

Apart from the available system environment modules, you can define your own modules and load module load use.own. This will set up the $HOME/privatemodules directory with an initial module file called null. It will also change your MODULEPATH environment variable to ensure that the module command looks for the modules in your home directory. See man modulefile for further information on writing your own modules.

# Job Schedulers

## What is a HPC Job?

In the arena of HPC, we talk a lot about jobs, these are simply commands we wish to run and requests for resources (e.g. `compute time`, `disk space`, `memory amount`, `software environments` etc.). HPC jobs are generally time consuming and resource intensive run non-interactively. However, they can be run interactively, but mainly for testing purposes.You need add your jobs to a queue and when machines have free resources jobs run.

Some widely used cluster batch systems are:

* Portable Batch System (PBS)
* Simple Linux Utility for Resource Management (SLURM)
* Moab
* Univa Grid Engine
* LoadLeveler, Condor
* OpenLava
* IBM’s Platform LSF

## What is the PBS?

Portable Batch System (PBS) is the name of computer software that performs job scheduling. Its primary task is to allocate computational tasks, i.e., batch jobs, among the available computing resources. The following versions of PBS are currently available:

* OpenPBS

* TORQUE

* PBS Professional (PBS Pro)
