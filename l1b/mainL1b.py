# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r"/home/cole/uc3m/earth_observation"
indir = r"/home/cole/uc3m/earth_observation/input"
outdir = r"/home/cole/uc3m/earth_observationy/outputs"

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
