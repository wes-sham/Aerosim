# Simulation settings -- change values here, not in the other files.
 
NX, NY = 400, 100      # grid size (cells): width, height
U_IN = 0.1             # inflow speed in lattice units (keep below ~0.1)
VISCOSITY = 0.02       # lattice viscosity; lower = more interesting but less stable
 
TAU = 3 * VISCOSITY + 0.5   # relaxation time, derived from viscosity (must stay > 0.5)
 
STEPS = 20000          # total simulation steps
PLOT_EVERY = 25        # redraw the display every N steps