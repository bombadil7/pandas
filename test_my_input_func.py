import pandas as pd
import numpy as np

def read_file(fname = 'fpga_in_47.csv'):
    df = pd.read_csv(fname, skiprows = [0], 
            names = list(map(str, range(128))))
    print(df.head(2))
    df.rename(columns={'0':'One'}, inplace=True)
    print(df.head(2))
    print(df.One)

if __name__ == '__main__':
    read_file()
