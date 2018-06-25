import pandas as pd
import numpy as np

def read_file(fname = 'fpga_in_47.csv'):
    df = pd.read_csv(fname, skiprows = [0])
    print(df)

if __name__ == '__main__':
    read_file()
