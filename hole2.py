import MDAnalysis as mda

u = mda.Universe("1grm_single.pdb")

protein = u.select_atoms("protein")

print(f"Load protein with {len(protein)} atoms.")

from MDAnalysis.analysis import hole2

path_to_hole = "/Users/tongyidou/miniforge3/envs/hole_env/bin/hole"

with hole2.HoleAnalysis(u, executable=path_to_hole) as h2:
  h2.run()
  h2.create_vmd_surface(filename="pore.md")
