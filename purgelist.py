import csv
import sys
import pandas as pd
from itertools import chain


# PURGE LIST (no extention input required)
# inFile: input CSV file
# ofList: suppression list CSV file (single column, header: email or EMAIL)
# resultFile: output CSV file - input minus all entries from suppression list

def purgelist(inFile, ofList, resultFile):

    # IMPORT SUPPRESS LIST FILE
    ofList = './' + ofList

    with open(ofList + '.csv', 'r') as suppress:
        reader = csv.reader(suppress)
        suppressList = list(chain(*reader))

    # IMPORT SEGMENT FILE
    originFile = pd.read_csv('./' + inFile + '.csv', index_col='EMAIL', encoding='ISO-8859-1', dtype='object')
    print(originFile)

    # DROP SUPPRESSED LIST FROM SEGMENT FILE
    originFile.drop(index=suppressList, inplace=True, errors='ignore')
    print(originFile)

    # EXPORT RESULTS to CSV
    originFile.to_csv('./' + resultFile + '.csv', header=True)

# PROCESS SYSTEM VARIABLES INPUT
if __name__ == "__main__":
    purgelist(sys.argv[1], sys.argv[2], sys.argv[3])
