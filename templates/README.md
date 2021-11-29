1. Make APD phase correction (see `phase_correction.sh`)
2. Make templates (interactively through `corrected_template.py` or on condor - see `sumbit_template.sh`)
3. `hadd <path/to/templates>/corrected_template.root <path/to/templates>/corrected_template_*.root`
4. Make smooth templates (see `smooth_template.py`)