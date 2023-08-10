# Author: Vrishab Sathish Kumar
# Aim: This python script accepts bulkRNA sequencing TPM data in CSV file, performs rudimentary data QC,
#	 data transformations for clustering, and outputs new CSV file with results.

import sys

def myfunction(mystring):
    print(mystring)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
