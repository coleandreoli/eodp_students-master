# MAIN FUNCTION TO CALL THE L1B MODULE

import os
from l1b.src.l1b import l1b

# Get directories from environment variables
try:
    auxdir = os.environ["EODP_AUXDIR"]
    indir = os.environ["EODP_INDIR"]
    outdir = os.environ["EODP_OUTDIR"]
except KeyError as e:
    missing_var = e.args[0]
    print(f"Error: Environment variable {missing_var} is not set.")
    print("Please set the following environment variables:")
    print("  export EODP_AUXDIR=/path/to/earth_observation")
    print("  export EODP_INDIR=/path/to/earth_observation/input")
    print("  export EODP_OUTDIR=/path/to/earth_observation/outputs")
    exit(1)

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
