import numpy as np
import pandas as pd
# import dataframe_image as dfi
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

#https://cduvallet.github.io/posts/2018/03/slopegraphs-in-python


def preparing_the_data(df):
    first_slope_graph = df.loc[(df['Year'] >= '1990') & (df['Year'] <= '2000')]
    second_slope_graph = df.loc[(df['Year'] >= '2000') & (df['Year'] <= '2010')]
    third_slope_graph = df.loc[(df['Year'] >= '2010') & (df['Year'] <= '2020')]

    number_of_rows = first_slope_graph.shape[0]

    # Retrieving the last row and the first row
    first_slope_graph_filtered = first_slope_graph.iloc[[0, number_of_rows - 1], :]
    second_slope_graph_filtered = second_slope_graph.iloc[[0, number_of_rows - 1], :]
    third_slope_graph_filtered = third_slope_graph.iloc[[0, number_of_rows - 1], :]

    first_slope_graph_filtered = first_slope_graph_filtered.T
    second_slope_graph_filtered = second_slope_graph_filtered.T
    third_slope_graph_filtered = third_slope_graph_filtered.T
    print('*')
    result_1 = first_slope_graph_filtered.rename(columns={204: 'first_day_1990', 335: 'last_day_2000'}, inplace=False)
    result_2 = second_slope_graph_filtered.rename(columns={204: 'first_day_2000', 335: 'last_day_2010'}, inplace=False)
    result_3 = third_slope_graph_filtered.rename(columns={204: 'first_day_2010', 335: 'last_day_2020'}, inplace=False)
    df_numeric = result_1.apply(pd.to_numeric, errors='coerce')
    result = result_1.dropna()
    print('*')
    return result_1 , result_2 , result_3


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

    preparing_the_data(df)
    print('*')