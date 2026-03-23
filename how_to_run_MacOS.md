## hole.inp

```sh
COORD hOAT1-OF_TFV_017.pdb
RADIUS /Users/tongyidou/miniforge3/envs/hole_env/share/hole2/rad/simple.rad
SAMPLE 0.1
ENDRAD 5.0
sphpdb spherical.sph
ignore HOH CL
!cpoint -10.42 -5.92 19.01 
cvect 0.0 0.0 1.0
```

## Run hole:
```sh
hole < hole.inp > hole_out.txt

sph_process -sos -dotden 15 -color spherical.sph  hole_out.sos

sos_triangle -s < hole_out.sos > hole_surface.vmd
```

## Visualize using VMD:

```sh
load PDB model
load spherical.sph

source hole_surface.vmd ! in 
```
