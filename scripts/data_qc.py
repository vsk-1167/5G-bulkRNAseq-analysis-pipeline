# Author: Vrishab Sathish Kumar
# Aim: This python script accepts bulkRNA sequencing TPM data in CSV file, performs rudimentary data QC,
#	 data transformations for clustering, and outputs new CSV file with results.

import sys
import pandas as pd
import numpy as np
import argparse
from pathlib import Path


#TODO: Add new data to specified 5G dataset 
#      --> designated dataset transformation? (avg_stdscaled_log_ratio, etc.) 
#      --> new experimental condition labels? (no, yes)
def addData(datasetPath, datasetTransformation, newExpConditions, newDatasetName = "not_specified"):
   print(datasetPath  + " " + datasetTransformation  + " " + newExpConditions + " " +  newDatasetName)



#TODO: Analyze entirely new dataset


def myfunction(mystring):
    print(mystring)

if __name__ == '__main__':
   # globals()[sys.argv[1]](sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] )
	parser = argparse.ArgumentParser()
	parser.add_argument("path")
	args = parser.parse_args()	
	target_dir = Path(args.path)

	if not target_dir.exists():
    		print("The target directory doesn't exist")
    		raise SystemExit(1)

	for entry in target_dir.iterdir():
    		print(entry.name)
