import numpy as np
import pandas as pd
# import dataframe_image as dfi
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    # In order to concanate the 2 column of the "Year" and "Month" we need to convert to string if needed
    df['Year'] = df['Year'].astype(str)
    df['Month'] = df['Month'].astype(str)

    # very important - # Combine 'Year' and 'Month' columns to create a datetime index
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    print('*')

    #1) What are the top 5 items that experienced a more significant decrease in prices compared to increases during the 90s and 2000s?

    df_filtered = df.loc[(df['Year'] >= '2000') & (df['Year'] <= '2010')]
    print('*')
    number_of_rows = df_filtered.shape[0]

    #Retrieving the last row and the first row
    df_filtered = df_filtered.iloc[[0, number_of_rows - 1], :]
    df_filtered = df_filtered.T
    df_filtered = df_filtered.dropna()
    #df_filtered_cleaner = df_filtered.dropna()
    result = df_filtered.rename(columns={204: 'first_day_2000', 335: 'last_day_2010'},inplace=False)
    df_numeric = df_filtered.apply(pd.to_numeric, errors='coerce')
    df_filtered = result.dropna()
    print('*')