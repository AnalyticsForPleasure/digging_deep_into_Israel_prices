import numpy as np
import pandas as pd
# import dataframe_image as dfi
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.lines as mlines



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)
    #df['Year_month'] = df['Year'].str.cat(df['Month'], sep=' - ')
    df['Year_month'] = df['Year'] + df['Month']
    print('(')

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)


    # Now let's transpose the dataframe, it will be easier working on lt
    df_traspose = df.T
    print('*')
