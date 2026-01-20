#!/usr/bin/env python
import sys
import os

# Change to the topsis directory
os.chdir(r'c:\Users\DELL\Desktop\Predictive Analysis\topsis')

# Add the package directory to path
sys.path.insert(0, r'c:\Users\DELL\Desktop\Predictive Analysis\topsis\TOPSIS-KRISH-MAHAJAN')

# Now execute the topsis1 module directly
if __name__ == "__main__":
    sys.argv = ['topsis1.py', 'example_data.csv', '2,1,2,2', '-,+,+,+', 'example_results.csv']
    
    import pandas as pd
    import numpy as np
    
    # Import the functions from topsis1.py
    exec(open(r'c:\Users\DELL\Desktop\Predictive Analysis\topsis\TOPSIS-KRISH-MAHAJAN\topsis1.py').read())
