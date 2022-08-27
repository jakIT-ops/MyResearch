## A brief history of the PBS

Before the emergence of clusters, the Unix-based Network Queuing System (NQS) from NASA Ames Research Center was a commonly used batch-queuing system. Then with the emergence of parallel distributed system, NQS began to show its limitations. Consequently, Ames then led an effort to develop requirements and specifications for a newer, cluster-compatible system. With NASA’s funding this efforts resulted into PBS in the early 1990s. In 2003, PBS was acquired by Altair Engineering and is now marketed as PBS Pro by Altair Grid Technologies, a subsidiary of Altair Engineering.

### PBS Pro’s key features

* Scalability: supports millions of cores with fast job dispatch and minimal latency; tested beyond 50,000 nodes

* Policy-Driven Scheduling: meets unique site goals and SLAs by balancing job turnaround time and utilization with optimal job placement

* Resiliency: includes automatic fail-over architecture with no single point of failure – jobs are never lost, and jobs continue to run despite failures

* Flexible Plugin Framework: simplifies administration with enhanced visibility and extensibility; customize implementations to meet complex requirements

* Health Checks: monitors and automatically mitigates faults with a comprehensive health check framework

## PBS basic commands

From the user’s perspective, the PBS allows to perform three actions:

* Add a job to the queue;
* Remove a job from the queue; and
* See where is your job is in the queue (stat).

https://www.youtube.com/watch?v=b0KDSKSN2Yc&feature=emb_title

## PBS Matlab example

MATLAB (matrix laboratory) is a multi-paradigm numerical computing environment and fourth-generation programming language. A proprietary programming language developed by MathWorks, MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages. To run, Matlab program codes in a HPC environment, first load the relevant module:

`module load matlab`

Consider the following Matlab code:

```matlab
% MATLAB M-file example to approximate a sawtooth
% with a truncated Fourier expansion.
%
nterms=5;
fourbypi=4.0/pi;
np=100;
y(1:np)=pi/2.0;
x(1:np)=linspace(-2.0*pi,2*pi,np);
for k=1:nterms
   twokm=2*k-1;
   y=y-fourbypi*cos(twokm*x)/twokm^2;
end;
plot(x,y);
print -deps matlab_test_plot.ps;
quit;
```


```MatLab
#!/bin/bash -l

#### job name
#PBS -N matlab_test
#
#### select resources
#PBS -l walltime=10:00:00
#PBS -l nodes=1:ppn=1
#
#### mail Options
#PBS -m abe
#PBS -M ruser@usq.edu.au
#
#### set journal options
#PBS -j oe
#
#### select queue
#PBS -q standard
#

#### load matlab module
module load matlab

#### cd to the directory where the job was submitted
cd $PBS_O_WORKDIR

# Run MATLAB
matlab -nodisplay -nodesktop -nosplash -r matlab_test
```
