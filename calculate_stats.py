#
# After running `run_simulations.py`, use this file to generate a `stats.csv`
# file of summary statistics.
#

import os 
import csv 
import pandas 
import numpy as np 
import scipy.stats as sc
from run_simulations import files, aliases
import pdb

baseline_csv = '10_2_5.csv' # this is the baseline case

def main():
    table = []
    columns = ['num_applicants', 'fraction_applicants_no_interviews', 'match_rate']
    for column in columns:
        for i in range(0,len(files)):
            myfile = files[i]
            alias = aliases[i]
            alias = alias.replace('\n', ' ')
            df_baseline = pandas.read_csv(baseline_csv)
            df = pandas.read_csv(myfile)
            p_value = sc.ttest_ind(df[column], df_baseline[column], equal_var=False).pvalue
            results = [alias, column, df[column].mean(), df[column].median(), df[column].min(), 
                       df[column].max(), p_value]
            table.append(results)                
    with open('stats.csv', 'w', newline='') as outputfile:
        writer = csv.writer(outputfile)
        for i in range(0,len(table)):
            writer.writerow(table[i])
            
if __name__ == '__main__':
    main()
